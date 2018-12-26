import socket
s = socket.socket()
s.bind((socket.gethostname(), 1234))
s.listen(5)
con, address = s.accept()
print("Seen ", address)
con.send(b'Thank for connect')
con.close()
