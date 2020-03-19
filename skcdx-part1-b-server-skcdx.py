import socket

#socket host and port number for different machine
host = ''
port = 5000

def bind(host,port):
	# initializing socket
	s=socket.socket()
	#s.bind –> This method binds host address and port number
	s.bind((host, port))
	print('server listening ...')
	#s.listen –> This method starts TCP listner
	s.listen(1)
	#s.accept –> This method accepts client connection
	c,addr = s.accept()
	return c

def transfer_data(c):
	while True:
		#c.recv –> This recieves TCP message
		data=c.recv(2048)
		if str(data.decode()) == "quit":
			#c.send –> This method sends TCP message
			c.send(str.encode("server exit"))
			print(str(data.decode()))
			break		
		else:
			with open('output.txt', 'wb') as fp:
				while True:
					print(data)
					#this writes data into file
					fp.write(data)
					if str(data).find("File transfer complete") != -1:
						fp.write(str.encode("\n This is new line added by the server\n"))
						print("\n This line is added by me in the Server !!! \n")
						break
					data = c.recv(2048)

			fp = open('output.txt','rb')
			chunk = fp.read(2048)
			while (chunk):
				c.send(chunk)
				chunk = fp.read(2048)
			fp.close()
			c.send(str.encode("File sent back from server"))

def main():
	c=bind(host, port)
	transfer_data(c)
	c.close()

if __name__== "__main__":
	main()