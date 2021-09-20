#TCP Client Transmission Control Protocol
import socket

target_host = "www.google.com"
target_port = 80

#creates a socket object 1
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client 2
client.connect((target_host,target_port))

#send some data  3
client.send(b" / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data 4
response = client.recv(4096)

print(response.decode())
client.close()