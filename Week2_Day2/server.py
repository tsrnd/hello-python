import socket               # Import socket module

s = socket.socket()         # Tao mot doi tuong socket
host = socket.gethostname()  # Lay ten thiet bi local
port = 12345                # Danh rieng mot port cho dich vu cua ban.
s.bind((host, port))        # Ket noi toi port

s.listen(5)                 # Doi 5 s de ket noi voi client.
while True:
    c, addr = s.accept()     # Thiet lap ket noi voi client.
    print('Da ket noi voi', addr)
    c.send('Cam on ban da ket noi'.encode())
    c.close()                # Ngat ket noi
