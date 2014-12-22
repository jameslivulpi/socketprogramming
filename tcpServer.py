#!/usr/bin/env python

#o----------------------------------------------------------------------------o
# UDP Ping Client
# Author: James Livulpi & Sapoon Dutta
# Description: This server talks to a client and carries out a point of sale
# protocol. It receives data from the client via command line arguments and
# talks to this server which uses random numbers to simulate unsuccessful
# transactions 2-5 percent of the time which will send to the client if it
# fails or is OK. When the trasaction is successful the server prints out the
# store name, credit card number, amount, and tip that the client sent. If the
# transaction is unsuccessful the serve will wipe the data sent from client.
#o----------------------------------------------------------------------------o

import socket
import random
import sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#Allows re-using socket
    s.bind(('localhost', 23481))
    s.listen(5)#Listening for connections
    conn, addr = s.accept()
    print("Connection address:", addr)#Prints clients IP address
    while True:
        try:#Try-Except for unsuccessful transaction case
            handShake = conn.recv(2048)
            conn.send(("SESSION STARTED").encode('UTF-8'))
            storeNameData = conn.recv(2048)
            conn.send(("OK").encode('UTF-8'))
            creditCardData = conn.recv(2048)
            rand = random.randint(0,100)       
            if rand <= 5:
                conn.send(("OK").encode('UTF-8'))
            else:
                conn.send(("Invalid card number entered").encode('UTF-8'))
                conn.close()
            expirationData = conn.recv(2048)
            if rand <= 98:
                conn.send(("OK").encode('UTF-8'))
            else:
                conn.send(("Credit Card is expired").encode('UTF-8'))
                conn.close()
            amountData = conn.recv(2048)
            rand = random.randint(0,100)
            if rand <= 95:
                conn.send(("OK").encode('UTF-8'))
            else:
                conn.send(("Insufficient Credit to process transaction").encode('UTF-8'))
                conn.close()
            tipData = conn.recv(2048)
            rand = random.randint(0,100)
            if rand <= 97:
                conn.send(("OK").encode('UTF-8'))
            else:
                conn.send(("Insufficient Credit to process tip").encode('UTF-8'))
            closeSession = conn.recv(2048)
            conn.send(("SESSIONCLOSED").encode('UTF-8'))
            #Prints sessions data if successful 
            print((storeNameData).decode('UTF-8'))
            print((creditCardData).decode('UTF-8'))
            print((amountData).decode('UTF-8'))
            print((tipData).decode('UTF-8'))
        except:
            sys.exit()#Wipes data from server if unsuccessful
main()
            
            
       
        
   
        
       
  
        
    

