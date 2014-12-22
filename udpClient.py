#!/usr/bin/python

#o----------------------------------------------------------------------------o
# UDP Ping Client
# Author: James Livulpi & Sapoon Dutta
# Description: This program sends and receives UDP packets using a server
# provided by the textbook manufacturer (Computer Networking: Kurose/Ross
# 6th Ed.) The client asks for X amount of packets to be sent and sends them to
# to the server via UDP which then turns around and sends back the packets to
# the client. This program counts the round trip time for each packet along
# with the average of successful packets received. In the case of a packet lost
# the client will timeout and print accordingly.
#o----------------------------------------------------------------------------o
import time
from socket import *

def main():
    serverName = 'localhost'
    serverPort = 12026                       
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = 'PING'   
    print("RUNNING! \n")
    #Number of packets to be sent chosen by user for better tests of RTT
    numberOfPackets = int(input("Enter amount of packets to send: "))
    #Accumulator to be used for calculating average RTT
    sum = 0.0
    rcvPackets = 0
    lossRate = 0
    seqNumber = 0 
    while seqNumber < numberOfPackets:
        startTime = time.time() #Time when packet is sent
        clientSocket.sendto(message.encode('UTF-8'),(serverName, serverPort))
        clientSocket.settimeout(1) #Timeout = 1 second
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            roundTripTime = time.time() - startTime #Calculates RTT
            rcvPackets += 1
            print(seqNumber)
            print(modifiedMessage.decode('UTF-8'))
            print("RTT for this packet equals: ", (roundTripTime * 1000))
            sum = sum + (roundTripTime * 1000)
        #Exception is raised when a timeout occurs on a socket
        except timeout:
            lossRate += 1
            print(seqNumber)
            print("Timeout")
        seqNumber += 1
    print("There were", lossRate, "packet(s) lost in transit")
    print("There were", rcvPackets, "packet(s) successfully received")
    print("The average RTT of", rcvPackets, "packets is: ", (sum/rcvPackets))
 
    clientSocket.close()
    

if __name__== '__main__':
    main()

    
        

 
