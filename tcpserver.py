#TCP Server Creation Transmission Control Protocal server
import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT)) #Ip address port for server to listen on 
    server.listen(5) #telling server to start listening 
    print(f'[*] Listening on {IP}:{PORT}')
    #when client connects the client socket gets stored in the client variable and remote connection is in the address variable 
    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()#Now loop is ready to handle another connection 
        
def handle_client(client_socket): #sends simple message back to the client in utf-8 format 
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')
        
if_name_ == '_main_':
    main()