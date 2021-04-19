import socket

s = socket.socket()                                                     #create socket
port = int(input("Port: "))                                             #initialise port 
s.bind(('', port))                                                      #bind port to socket
s.listen(5)                                                             #listen for connection
c, addr = s.accept()                                                    #accept connection
print ("Socket Up and running with a connection from",addr)             
while True:                                                             
    rcvdData = c.recv(1024).decode()                                    #decode recieved data
    print ("Received:",rcvdData)                                        #print received data               
    sendData = input("Send: ")                                          #write message
    c.send(sendData.encode())                                           #send message
    if(sendData == "Bye" or sendData == "bye"):                         #keyword to close connection
        break
c.close()                                                               #close connection