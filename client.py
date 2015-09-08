#!/usr/bin/env python
# Simple socket client. Sends filename to port and ip.

import socket


HOST = '127.0.0.1'    

PORT = 35536              
FILE_NAME='test .txt\n'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

try:
	s.sendall(FILE_NAME)
	data = s.recv(1024)
	print 'Received', repr(data)

finally:
	s.close()