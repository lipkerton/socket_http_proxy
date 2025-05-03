'''Client realisation for test.'''
import time

from gevent import socket


server_address = ('127.0.0.1', 6789)
client = socket.socket()
client.connect(server_address)

client.sendall(b'Hey!')
time.sleep(5)
client.sendall(b'Hey after five seconds!')
data = client.recv(1024)
print(data)
client.close()
