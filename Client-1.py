import socket               # Import socket module
from thread import *

s = socket.socket()         
host = socket.gethostname()
port = 8281                # Reserve a port for your service.
s.connect((host, port))




def recvthread (null):
        while True:
                Reply = s.recv(1024)
                print  Reply

start_new_thread(recvthread,(0,))
while True:
        Message = raw_input()
        s.send(Message)
        if Message.lower() == 'quit()' or Message.lower() == 'exit()' :
                break

s.close()
