import socket
#socket host and port number
host = socket.gethostbyname("192.168.1.222")
port = 5000
def connect(host,port):
	# initializing socket
	s=socket.socket()
	#s.connect –> This method initiates TCP connection
	s.connect((host, port))
	return s

def transfer_data(fname,s):
	while True:
		if fname == "quit":
			#s.send –> This method sends TCP message
			s.send(str.encode(fname))
			#s.recv –> This recieves TCP message
			data=str(s.recv(2048).decode())
			print(data)
			break
		else :  
			#opens file fname
			f = open(fname,'rb')
			#reads file f
			l = f.read(1024)
			print("data sending ", end =" ")
			while (l):
				print(".", end =" ")
				#s.send –> This method sends TCP message
				s.send(l)
				l = f.read(2048)
			f.close()
			s.send(str.encode("File transfer complete"))
			print("\n")

			while True:
				#s.recv –> This recieves TCP message
				data = s.recv(1024)
				if str(data).find("File sent back from server") != -1:
					break
				print(data)
			print("File received back\n")
			fname= input("Enter another file name or type exit/quit : ")
		
def main():
	s=connect(host, port)
	fname=input('Enter file name')
	transfer_data(fname,s)
	s.close()

if __name__== "__main__":
    main()