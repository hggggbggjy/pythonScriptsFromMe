import socket, platform, os

server address = ""  #insert address
server port =        #insert port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #get ipv4 address and TCP connection
s.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #validating address and assinging intiger 
s.bind ((SRV_ADDR, SRV_PORT)) #binding all to server address and port
listen(1)
connection, address = s.accept() #send and recive info 

while 1:
    try:
        data = connection.recv(1024) #buff size of data being recived
    except:continue

    if(data.decode('utf-8') == '1'): #first if statement eing dealt with
        tosend = platform.platform() + " " + platform.machine()
        connection.sendall(tosend.encode())
    elif(data.decode('utf-8') == '2'): # first if else statement 
        data = connection.recv(1024)
        try:
            filelist = os.listdir(data.decode('utf-8')) #getting file lists
            tosend = ""
            for x in filelist:
                tosend += "," + x

            except: #error 
                tosend = " youre not on the right path bud "
            connection.sendall(tosend.encode())
        elif(data decode ('utf-8' ) == ""): 
            connection.close()
            connection, address = s.accept()
