# Socket_Programming
 Readme text file for client program created and programmed by KAWLE Shreyash Sanjay.
The client program was created using python programming language on Visual Studio Code. 


Steps to compiling and running the code:
1. Download the server and client codes and place them in the same folder.
2. Open both programs and start compiling server .py code first. Then, compile client .py code. 
3. Input the IP address of a server in dotted decimal notation format, and port number. 
   If the connection is successful, program prints "Connection status: SUCCESS".
   If the input of IP address/port number is incorrect, or connection failure occurs, program prints "Connection status: FAILURE". Then repeat step 3. 
4. When the program successfully accepts and outputs "command: ", input command (UPLOAD, DOWNLOAD, RETRIEVE) and filename (xxxx.txt) required for action.
   If filename is not given, program prints "ERROR: please provide file name". Then repeat step 4.
   Step 4 will be repeated until step 5 is completed.
   4-1. UPLOAD: First checks for file existence. Then, uploads the file line by line until last line is reached. 
                Error reached when file given does not exist. 
   4-2. DOWNLOAD: First checks for file existence. Then, store the file line by line until last line is reached. 
                  Error reached when file already exists in client.
   4-3. RETRIEVE: Checks for existence of a text file (with file name) on server. 
                  Prints "YES" when file is already on server, and "NO" when file isn't on server.
5. Input "EXIT" to close socket and end program. 
