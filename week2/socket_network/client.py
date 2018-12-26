import socket

stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
server_address = ((host, port))
print('connecting')
stream_socket.connect(server_address)
message = 'message'
stream_socket.sendall(message.encode())
data = stream_socket.recv(10)
print(data.decode())
print('socket closed')
stream_socket.close()
