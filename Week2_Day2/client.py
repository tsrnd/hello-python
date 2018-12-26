import socket               # Import socket module

s = socket.socket()         # Tao mot doi tuong socket
host = socket.gethostname()  # Lay ten thiet bi local
port = 12345                # Danh rieng mot port cho dich vu cua ban.

s.connect((host, port))
print(s.recv(1024).decode())
s.close                     # Dong socket
