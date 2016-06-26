#!usr/bin/python3

import socket
from thread import *
import sys

HOST = ''
PORT = 8481

Name = []
conn = [] 
nclnt = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
        s.bind((HOST,PORT))
except s.error as error:
        print 'Socket Binding error'
        sys.exit()
print 'Welcome to Server\nServer is now started\n'
s.listen(10)

def clientfunc (connt):
        connt.send('Enter your Name:')
        myname = connt.recv(1024)
        Name.append(myname)
        print ''
        print Name
        connt.send('Welcome to chat Server!\n')
        for i in range(len(conn)):
                conn[i].send('\nA new user have come to Chat server!\nAvailable users are:')
                for j in xrange(len(conn)):
                        conn[i].send('\n'+str(j+1) + '-' + Name[j])
        while True:
                connt.send('\nWrite a Message to send...')
                data = connt.recv(1024)
                if data == 'exit()' or data == 'quit()' :
                        break
                if ':' in data:
                        try:
                                nm = data[:data.index(':')]
                                index = Name.index(nm)
                                conn[index].send(myname+data[data.index(':'):len(data)])
                        except:
                                connt.send('No person found! Enter correct Name..!')
                else:
                        for i in range(len(conn)):
                                conn[i].send(myname+':' + data)

        print myname +' has disconnected from server'
        Name.remove(myname)
        conn.remove(connt)
        for i in range(len(conn)):
                conn[i].send('\nA  user has left Chat server!\nAvailable users are:')
                for j in xrange(len(conn)):
                        conn[i].send('\n'+str(j+1) + '-' + Name[j])
        connt.close()




while True:
        con ,addr = s.accept()
        print 'Server Connected' , addr
        conn.append(con)
        nclnt = nclnt + 1
        start_new_thread(clientfunc,(con,))
s.close()

