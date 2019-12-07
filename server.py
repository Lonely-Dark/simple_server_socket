#Python3.8.0
#Made by Lonely_Dark

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 8080)) # bind (ip,port)
s.listen()

while True:
	sock_client, address=s.accept() # wait for connection

	header='HTTP/1.1 200 OK\n' # header
	request=sock_client.recv(4096) # get request from the client
	request=request.decode('utf-8') # decode request from the client
	request_split=request.split(' ') # split request from the client

	print('Connection from: '+address[0])

	if request_split[1]=='/':
		filename='index.html'
		header += 'Content-Type: '+'text/html'+'\n\n'
		header=header.encode('utf-8')

		with open(filename, 'rb') as file:
			response=file.read()

		final=header
		final+=response


	else:
		header='HTTP/1.1 404 Not Found\n\n'.encode('utf-8') # header with 404
		response='<html><head><title>File not found</title></head><body><h1>Error 404, file not found.</h1></html>'.encode('utf-8') # response(html code)
		print('Send '+ address[0] + ' '+ '404 code, not found')
		
		final=header
		final+=response
		
	sock_client.send(final) # send header and response(html code)
	sock_client.close() # close connection
