#creating a UDP client User Datagram Protocol
import socket

target_host = "127.0.0.1"
target_port = 9997

#Create a socket object 1
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Send some data 2
client.sendto(b"AAABBBCCC",(target_host,target_port))

#receive some data 3
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()