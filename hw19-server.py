#!/usr/bin/python3

import socket

dns_table = {'example.com': '192.168.1.1'}

host = 'localhost'
port = 9090
timeout = 120
address = (host, port)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(address)

while True:
    server.settimeout(timeout)
    try:
        input_data = server.recvfrom(1024)
    except socket.timeout:
        break
    input_string = str(input_data[0].decode()).split(' ')
    if input_string[0] == 'ADD':
        domain_name_and_ip = input_string[1].strip().split(':')
        if domain_name_and_ip[0] not in dns_table:
            dns_table.update({domain_name_and_ip[0].strip(): domain_name_and_ip[1].strip()})
            server.sendto(str('Domain name ' + domain_name_and_ip[0] +
                          ' with IP ' + domain_name_and_ip[1] + ' address added successfully.')
                          .encode(), input_data[1])
        else:
            dns_table.update({domain_name_and_ip[0].strip(): domain_name_and_ip[1].strip()})
            server.sendto(str('Domain name ' + domain_name_and_ip[0] +
                          ' with IP ' + domain_name_and_ip[1] + ' address updated successfully.')
                          .encode(), input_data[1])
    else:
        if input_string[0].strip() in dns_table:
            server.sendto(dns_table.get(input_string[0]).encode(), input_data[1])
        else:
            server.sendto(str('Domain name ' + input_string[0] + ' is not found.').encode(), input_data[1])

server.close()
