import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('www.py4inf.com', 80) )

# What Python will type
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    # receive up to 512 characters at a time
    data = mysock.recv(512)
    if ( (len(data)<1) ):
        break
    print data
mysock.close()
