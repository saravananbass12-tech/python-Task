import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 50000

s.bind((host, port))
s.listen(1)

print("server waiting...", flush=True)
con, addr = s.accept()
print("connected from", addr, flush=True)

data = con.recv(1024)
print("received:", data.decode(), flush=True)

con.close()
s.close()