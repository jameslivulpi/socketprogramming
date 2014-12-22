#!/usr/bin/env python

#o----------------------------------------------------------------------------o
# TCP Client
# Author: James Livulpi & Sapoon Dutta
# Description: This client talks to the server we have implemented for a point
# of sale protocol. This client takes 4 command line arguments to carry out the
# session. In the event of an unsuccessful transaction the client will close
# without error and server will wipe the data received from this client.
#o----------------------------------------------------------------------------o

import socket
import sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: #Try-Except for unsuccessful transaction case
        s.connect(('localhost', 23481))
        s.send(("STARTSESSION").encode('UTF-8'))
        handShake = s.recv(2048)
        print("received data:", handShake.decode('UTF-8'))
        s.send((sys.argv[1]).encode('UTF-8'))#Argument 1
        storeNameData = s.recv(2048)
        print("received data:", storeNameData.decode('UTF-8'))
        s.send((sys.argv[2]).encode('UTF-8'))#Argument 2
        creditCardData = s.recv(2048)
        print("received data:", creditCardData.decode('UTF-8'))
        s.send((sys.argv[3]).encode('UTF-8'))#Argument 3
        expirationData = s.recv(2048)
        print("received data:", expirationData.decode('UTF-8'))
        s.send((sys.argv[4]).encode('UTF-8'))#Argument 4
        amountData = s.recv(2048)
        print("received data:", amountData.decode('UTF-8'))
        s.send(("$1.00").encode('UTF-8'))
        tipData = s.recv(2048)
        print("received data:", tipData.decode('UTF-8'))
        s.send(("CLOSESESSION").encode('UTF-8'))
        closeSession = s.recv(2048)
        print("received data:", closeSession.decode('UTF-8'))
    except:
        s.close()#Closes without error
main()
