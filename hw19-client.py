#!/usr/bin/python3

import socket

host = 'localhost'
port = 9090
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    client_input = input("Request: ")
    if client_input.upper() == "EXIT":
        client.close()
        break
    else:
        client.sendto(client_input.encode(), (host, port))
        input_data = client.recvfrom(1024)
        print('Server response: ' + input_data[0].decode())
