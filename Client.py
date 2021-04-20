import socket
from threading import Thread
from clint.textui import colored

s = socket.socket()                               
server_ip = input("Server IP: ")                    
server_port = int(input("Server Port: "))            
s.connect((server_ip, server_port))          

def receive():
    while 1:
        rcvdData = s.recv(1024).decode()
        print (colored.red("\nFrom: "),rcvdData)
        print("")
        if rcvdData == "Bye" or rcvdData == "bye":
            print("\n+++++++++++++++++++")
            print(colored.blue("Connection ended"))    
            print("+++++++++++++++++++\n")
            break
    s.close()

def send():
    while 1:
        str = input()                            
        s.send(str.encode())                            
        if(str == "Bye" or str == "bye"):  
            print("\n+++++++++++++++++++")
            print(colored.blue("Connection ended"))    
            print("+++++++++++++++++++\n")          
            break
    s.close()

def main():
    Thread(target=receive).start()
    Thread(target=send).start()

if __name__ == '__main__':
    main()
