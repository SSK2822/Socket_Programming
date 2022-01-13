# Created and Programmed by
# KAWLE Shreyash Sanjay 

#Importing all neccessary libraries
from socket import * 
import sys
import time
import os
from server import BUFFER_SIZE

soc = socket(AF_INET, SOCK_STREAM)
IP = input("IP Address: ")
PORT = int(input("Port Number: "))
BUFF_SIZE = 2048
SENDING_COOLDOWN = 0.1 #As per server file

uploading = False
inputLines = [] #Input storage of download
storedFiles = [] #Storing file

print("IP Adderess: ", IP, '\t', "Port Number: ", PORT)
#Connection Checking
try:
    soc.connect((IP, PORT))
    print("Connect status: SUCCESS")
except ConnectionRefusedError:
    print("Connect status: FAIL")
    sys.exit()

while True:
    #Taking in user input command
    while True:
        try:
            command = input("command: ")
            cmdParts = command.split(" ")
            file = cmdParts[1]
            break
        except IndexError:
            print("ERROR: please provide file name")

    #Exit Socket
    if command == 'EXIT':
        soc.close()
        break
    
    #Uploading file
    elif 'UPLOAD' in command:
        #Checking if the file exists
        if (os.path.exists(file)):
            soc.sendall(command.encode())
            #Recieving Server response
            data = soc.recv(1024)
            print(data.decode())

            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    soc.sendall(line.encode())
                    print("Line Sent: ", line.rstrip())
                    time.sleep(SENDING_COOLDOWN) #Cooldown timing
                    reply = soc.recv(BUFF_SIZE).decode() #Receiving Acknowledgement
        else:
            print("FILE NOT FOUND IN CLIENT")

    #Downloading File
    elif 'DOWNLOAD' in command:
        #Checking if the file exits
        if(os.path.exists(file)):
            print("FILE ALREADY EXISTS IN CLIENT")
        else:
            soc.sendall(command.encode()) 
            reply = soc.recv(BUFF_SIZE).decode() #Server Response

            #If File exists on server
            if(reply == "SUCCESS"):
                inp = ""
                while(True):
                    inp = soc.recv(BUFFER_SIZE).decode()
                    if(inp == "#"):
                        break
                    else:
                        inputLines.append(inp)
                        print("Line Recieved: ", inp.rstrip()) #Print input line recieved
                        soc.sendall(inp.encode()) 
                        time.sleep(SENDING_COOLDOWN)

                with open(file, 'w', encoding = 'utf-8') as f:
                    f.writelines(inputLines)
                    inputLines = []
                    storedFiles.append(file) #Storing files in memory
            else:
                print(reply)

    #Retriving File
    elif 'RETRIEVE' in command:
        soc.sendall(command.encode())
        reply = soc.recv(BUFF_SIZE).decode() #Server Response
        print(reply) #Print's YES/NO
