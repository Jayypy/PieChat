import socket
from threading import Thread
from clint.textui import colored

s = socket.socket()                                             
port = int(input("Port: "))  
name = input("Your Name: ")                                   
s.bind(('', port))                                                
s.listen(5)                                                     
c, addr = s.accept()   
c.send(name.encode())                                                
print ("Connection found",addr)
cname = c.recv(1024).decode()
print("ClientName: " + colored.red(cname) + "\n") 

def receive():
    while 1:
        rcvdData = c.recv(1024).decode()                                    
        print (colored.red("\n" + cname + ": "), rcvdData)
        print("")
        if(rcvdData == "bye" or rcvdData == "Bye"):
            print("\n+++++++++++++++++++++++++++++++++++")
            print(colored.blue("Connection ended (Press Enter to exit)"))    
            print("+++++++++++++++++++++++++++++++++++\n")
            break
    c.close()

def send():
    while 1:
        sendData = input()                                         
        c.send(sendData.encode())                                         
        if(sendData == "Bye" or sendData == "bye"): 
            print("\n++++++++++++++++++++++")
            print(colored.blue("Connection ended"))    
            print("++++++++++++++++++++++\n")
            break                      
    c.close()

def main():
    Thread(target=receive).start()
    Thread(target=send).start()

if __name__ == '__main__':
    main()
