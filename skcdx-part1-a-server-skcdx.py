import socket

#socket host and port number for different machine
host_ip = '' 
port = 5000

# initializing socket
s = socket.socket()
#s.bind –> This method binds host address and port number
s.bind((host_ip, port))
#s.listen –> This method starts TCP listner
s.listen(1)
#s.accept –> This method accepts client connection
conn, addr = s.accept()
print("Connection from: " + str(addr))

while True:
    data = conn.recv(1024).decode()
    if data == "Bye from Client-Sowmya":
        print(data)
        #This method sends TCP message
        conn.send(str.encode("Bye from Server-Sowmya"))
        break
    elif data == "Hello from Client-Sowmya":
        print(data)
        conn.send(str.encode("Hello from Server-Sowmya"))
    else:
        print(data)
        conn.send(data.encode())
conn.close()