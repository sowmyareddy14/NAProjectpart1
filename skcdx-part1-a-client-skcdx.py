import socket
#socket host and port number
host_ip = socket.gethostbyname("192.168.1.222") 
port = 5000
# initializing socket
s = socket.socket()
#s.connect –> This method initiates TCP connection
s.connect((host_ip, port))
msg = input(" Enter Input-> ")

while True:
    if msg == "Bye from Client":
        #s.send –> This method sends TCP message
        s.send(msg.encode())
        #s.recv –> This recieves TCP message
        data = s.recv(1024).decode()
        print(data)
        if(data == "Bye from Server-Sowmya"):
            break

        else:
            msg=input("Enter another input")            
    else:
        s.send(msg.encode())
        data = s.recv(1024).decode()
        print(data)
        msg = input("Enter Input")
#s.close – This closes socket
s.close()