import socket

HOST = 'IP_ADDRESS'
PORT = 1020

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Test message").encode('utf-8')
print(socket.recv(1024).decode('utf-8'))
