#!usr/bin/python3

from socket import *

HOST = ''
PORT = 8086
s = socket(AF_INET,SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)

conn1 , addr1 = s.accept()
print 'Server Connected' , addr1
conn2 , addr2 = s.accept()
print 'Server Connected' , addr2

while (conn1 and conn2):
	data = conn1.recv(1024)
	conn2.send(data)
	data = conn2.recv(1024)
	conn1.send(data)	

conn1.close()
conn2.close()
s.close()
	
