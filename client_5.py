import socket
sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
user_message = ''
for i in range(0,2):
	user_message += input('Input 4 elements please: ') + ' '
sock.send(user_message.encode())
print(sock.recv(1024).decode())

