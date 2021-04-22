import socket
from threading import Thread
from clint.textui import colored

def makesocket():
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

    Thread(target=receive, args={c, cname}).start()
    Thread(target=send, args=c).start()

def receive(c, cname):
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

def send(c):
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
    makesocket()

if __name__ == '__main__':
    main()
