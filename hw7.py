#!/usr/bin/python3

map_shell_count = {}
map_user_UID = {}
map_group_UIDs = {}


with open('/etc/passwd', 'r') as passwd_fr:
    line_passwd = passwd_fr.readline().strip()
    while line_passwd:
        param_list_passwd = line_passwd.split(':')
        key_shell = param_list_passwd[6]
        username = param_list_passwd[0]
        UID = param_list_passwd[2]
        map_user_UID.update({username: UID})
        if key_shell not in map_shell_count.keys():
            i = 1
        else:
            i = map_shell_count.get(key_shell) + 1
        map_shell_count.update({key_shell: i})
        line_passwd = passwd_fr.readline().strip()

with open('/etc/group', 'r') as group_fr:
    line_group = group_fr.readline().strip()
    while line_group:
        param_list_group = line_group.split(':')
        key_group = param_list_group[0]
        value_group = param_list_group[3].split(',')

        i = 0
        while i < len(value_group):
            user_element = value_group[i].strip()
            UID = map_user_UID.get(user_element)
            if UID is None:
                UID = ''
            value_group[i] = UID
            i += 1

        map_group_UIDs.update({key_group: value_group})
        line_group = group_fr.readline().strip()

print("\nNumber of users (UIDs) using all available shell interpreters:")
for key, value in map_shell_count.items():
    print(key, '-', value)

print("\nLinux system groups and UIDs of users in this groups:")
for key, value in map_group_UIDs.items():
    print(key + ":", ",".join(value))
