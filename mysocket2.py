import socket

SVR_ADDR = input ("Type the server IP address")
SVR_PORT = int(input("Type the server port"))

s = socket.socket(socket.AF_INET, socket.SOCKET_STREAM
connect ((SRV_PORT, SVR_PORT))
s.listen(1)
print("Server started! Waiting for connection...")
connection, address = s.accept()
print('Client connected with address: ', address)
while 1:
        data = connection.recv(1024)
        if not data: break
        connection.sendall(b'-- Message Recived --\n')
        print(data.decode('utf-8'))
connection.close()                   
