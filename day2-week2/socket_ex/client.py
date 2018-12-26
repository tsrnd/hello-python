import socket
import time

s = socket.socket()
try:
    s.connect((socket.gethostname(), 1234))
    print(s.recv(1024))
except Exception as e:
    print("Fail to connect", e)
finally:
    s.close()
