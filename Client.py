import socket

s = socket.socket()                                  #Create a Socket
server_ip = input("Server IP: ")                     #ip adress of server
server_port = int(input("Server Port: "))            
s.connect((server_ip, server_port))                  #Connect to the server
while True:
    str = input("Send: ")                            #write a message
    s.send(str.encode())                             #send the message
    if(str == "Bye" or str == "bye"):                #Codeword to end conversation
        break
    print ("Recieve:",s.recv(1024).decode())         #Recieve a message
s.close()                                            #close the socket 