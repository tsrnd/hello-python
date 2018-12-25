  # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Tao mot doi tuong socket
host = socket.gethostname() # Lay ten thiet bi local
port = 8888                # Danh rieng mot port cho dich vu cua ban.

s.connect(('127.0.0.1', port))
print (s.recv(1024))
s.close                     # Dong socket