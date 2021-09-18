#!/usr/bin/python3

map_shell_count = {}
map_user_UID = {}
map_group_UIDs = {}
map_UID_PGID = {}

output_file = open('output.txt', 'w+')

with open('/etc/passwd', 'r') as passwd_fr:
    line_passwd = passwd_fr.readline().strip()
    while line_passwd:
        param_list_passwd = line_passwd.split(':')
        key_shell = param_list_passwd[6].strip()
        username = param_list_passwd[0].strip()
        UID = param_list_passwd[2].strip()
        PGID = param_list_passwd[3].strip()
        map_UID_PGID.update({UID: PGID})
        map_user_UID.update({username: UID})
        if key_shell not in map_shell_count.keys():
            i = 1
        else:
            i = map_shell_count.get(key_shell) + 1
        map_shell_count.update({key_shell: i})
        line_passwd = passwd_fr.readline().strip()

with open('/etc/group', 'r') as group_fr:
    line_group = group_fr.readline().strip()
    list_of_UID = list(map_UID_PGID.keys())
    list_of_PGID = list(map_UID_PGID.values())
    while line_group:
        param_list_group = line_group.split(':')
        key_group = param_list_group[0].strip()
        GID = param_list_group[2].strip()
        value_group = param_list_group[3].split(',')

        i = 0
        while i < len(value_group):
            user_element = value_group[i].strip()
            UID = map_user_UID.get(user_element)
            if UID is None:
                UID = ''
            else:
                value_group[i] = int(UID)
            i += 1

        j = 0
        while j < len(map_UID_PGID.values()):
            if list_of_PGID[j] == GID:
                if value_group[0] == '':
                    value_group[0] = int(list_of_UID[j])
                k = 0
                while k < len(value_group):
                    if value_group[k] != '':
                        value_group[k] = int(value_group[k])
                    k += 1
                value_group.append(int(list_of_UID[j]))
            j += 1

        set_of_value_group = set(value_group)
        list_of_value_group = list(set_of_value_group)
        map_group_UIDs.update({key_group: list_of_value_group})

        line_group = group_fr.readline().strip()

output_file.write("\nNumber of users (UIDs) using all available shell interpreters:\n")
for key, value in map_shell_count.items():
    output_file.write(key + ' - ' + str(value) + '\n')

output_file.write("\nLinux system groups and UIDs of users in this groups:\n")
for key, value in map_group_UIDs.items():
    result_str = ""
    if len(value) > 1:
        m = 0
        str_value_m = ""
        while m < len(value):
            if m == len(value)-1:
                str_value_m = str(value[m])
                result_str = result_str + str_value_m
                m += 1
            else:
                str_value_m = str(value[m])
                result_str = result_str + str_value_m + ","
                m += 1
    else:
        result_str = result_str + str(value[0])
    output_file.write('' + key + ": " + result_str + '\n')

output_file.close()
