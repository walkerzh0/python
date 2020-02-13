import socket
s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
# print('From server received:', s.recv(1024).decode())
print('From server received:', s.recv(1024).decode())