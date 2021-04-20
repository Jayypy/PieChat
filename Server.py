import socket
from threading import Thread
from clint.textui import colored

s = socket.socket()                                             
port = int(input("Port: "))                                     
s.bind(('', port))                                                
s.listen(5)                                                     
c, addr = s.accept()                                                   
print ("Socket Up and running with a connection from",addr)

def receive():
    while 1:
        rcvdData = c.recv(1024).decode()                                    
        print (colored.red("\nFrom: "), rcvdData)
        print("")
        if(rcvdData == "bye" or rcvdData == "Bye"):
            print("\n+++++++++++++++++++")
            print(colored.blue("Connection ended"))    
            print("+++++++++++++++++++\n")
            break
    c.close()

def send():
    while 1:
        sendData = input()                                         
        c.send(sendData.encode())                                         
        if(sendData == "Bye" or sendData == "bye"): 
            print("\n+++++++++++++++++++")
            print(colored.blue("Connection ended"))    
            print("+++++++++++++++++++\n")
            break                      
    c.close()

def main():
    Thread(target=receive).start()
    Thread(target=send).start()

if __name__ == '__main__':
    main()
