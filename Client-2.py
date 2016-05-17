#!usr/bin/python3

from socket import *

HOST = ''
PORT = 8086

s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST,PORT))

while True:
	Reply = s.recv(1024)
	print 'Received:', (Reply)
	Message = raw_input('Send:')
	s.send(Message)
	

s.close()
