import socket
from threading import Thread
from clint.textui import colored

def makesocket():
    s = socket.socket()          
    name = input("Your Name: ")                   
    server_ip = input("Server IP: ")                    
    server_port = int(input("Server Port: "))            
    s.connect((server_ip, server_port))
    cname = s.send(name.encode())     
    sname = s.recv(1024).decode()
    print("Server name: " + colored.red(sname) + "\n")

    Thread(target=receive, args={s, sname}).start()
    Thread(target=send, args=s).start()

def receive(s, sname):
    while 1:
        rcvdData = s.recv(1024).decode()
        print (colored.red("\n" + sname + ": "),rcvdData)
        print("")
        if rcvdData == "Bye" or rcvdData == "bye":
            print("\n+++++++++++++++++++++++++++++++++++")
            print(colored.blue("Connection ended (Press Enter to exit)"))    
            print("+++++++++++++++++++++++++++++++++++\n")
            break
    s.close()

def send(s):
    while 1:
        str = input()                            
        s.send(str.encode())                            
        if(str == "Bye" or str == "bye"):  
            print("\n++++++++++++++++++++++")
            print(colored.blue("Connection ended"))    
            print("++++++++++++++++++++++\n")         
            break
    s.close()

def main():
    makesocket()

if __name__ == '__main__':
    main()
