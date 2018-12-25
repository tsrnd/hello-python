            # Day la server.py file

import socket               # Import socket module

s = socket.socket()         # Tao mot doi tuong socket
host = '127.0.0.1' # Lay ten thiet bi local
port = 8888                # Danh rieng mot port cho dich vu cua ban.
print (host)
s.bind((host, port))        # Ket noi toi port

s.listen(5)                 # Doi 5 s de ket noi voi client.
while True:
   c, addr = s.accept()     # Thiet lap ket noi voi client.
   print ('Da ket noi voi', addr)
   c.send('Cam on ban da ket noi')
   c.close()                # Ngat ket noi