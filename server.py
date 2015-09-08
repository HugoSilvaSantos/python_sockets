#!/usr/bin/env python
'''
Socket server. Listen port and ip. 
Receives string from client: file_name extension\n
Read and return to the client file contents. Create new file if doesnt exist
To run: $python server.py
'''

import socket

print('Waiting Client Connection...')

HOST = '' # localhost
PORT = 35536

# Socket s is created
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
	conn, addr = s.accept()

	try:
		print 'Connected to: ', addr

		data = conn.recv(1024)
		data_concat=data.replace(" ", "").strip(' \t\n\r')	# Remove space and \n
		print 'File Name: ', data_concat

		if data_concat: 
			try:
				with open(data_concat, 'r') as f: #Read the file
					text = f.read()
					print 'Text: ', text
					conn.sendall(text)
					f.close()
			except IOError:
				with open(data_concat, 'w+') as f: # Create if doesnt exist 
					text = f.read()
					print 'Text: ', text
					conn.sendall(text)
					f.close()
		else:
			break

	finally:
		conn.close()