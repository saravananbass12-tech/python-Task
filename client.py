import socket

x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 50000

x.connect((host, port))
x.sendall(b'hello saravanan')
print("message sent")
x.close()