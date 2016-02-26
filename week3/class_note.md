# **Networked Programs**
## Communicate with Internet
 - Transport Control Protocol (TCP)
    - App (Client) -> Transport (Client)  -> Transport (Server) -> App (Server) -> Transport (Server) -> Transport (Client) -> App (Client)
 - 簡言之!
    - App (Client) -> Socket -> App (Server) -> Socket -> App (Client)

## Common TCP
 - Telnet (23) Login
 - SSH (22) Secure Login
 - HTTP (80)
 - HTTPS (443) Secure
 - SMTP (25) Mail
 - IMAP (143/220/993) Mail Retrieval
 - POP (109/110) Mail Retrieval
 - DNS (53) Domain Name
 - FTP (21) File Transfer

## [Socket](https://docs.python.org/2/library/socket.html) in Python
> Python has built-in support for TCP Sockets

    import socket
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect( ('www.py4inf.com', 80) )

## What We Say to Socket
    http://www.dr-chunk.com/page1.html

|          |       URL components  |
|----------|--------------------|
| protocol | "http"             |
| host     | "www.dr-chunk.com" |
| document | "page1.html"       |

 - Request-Response Cycle:
    - (Click) -> "GET" Request another document to web server -> Retrieve Data
 - Make an HTTP Request


    GET http://www.dr-chunk.com/page1.htm HTTP/1.0
## Build a Web Browser using Python
    import socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect( ('www.py4inf.com', 80) )

    # What Python will type in terminal
    mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

    while True:
        # receive up to 512 characters at a time
        data = mysock.recv(512)
        if ( (len(data)<1) ):
            break
            print data
    mysock.close()

而得到的回應是:

    ⇒  python socket_example.py
    HTTP/1.1 200 OK
    Date: Fri, 26 Feb 2016 05:39:25 GMT
    Server: Apache
    Last-Modified: Fri, 04 Dec 2015 19:05:04 GMT
    ETag: "e103c2f4-a7-526172f5b5d89"
    Accept-Ranges: bytes
    Content-Length: 167
    Cache-Control: max-age=604800, public
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Headers: origin, x-requested-with, content-type
    Access-Control-Allow-Methods: GET
    Connection: close
    Content-Type: text/plain

    But soft what light through yonder window breaks
    It is the east and Juliet is the sun
    Arise fai
    r sun and kill the envious moon
    Who is already sick and pale with grief

## Making HTTP Easier With [urllib](https://docs.python.org/2/library/urllib.html)
Turn URL as a file.

    import urllib
    fhand = urllib.urlopen('http://example.com/document.htm')

    for line in fhand:
        print line.strip()
結果:

    But soft what light through yonder window breaks
    It is the east and Juliet is the sun
    Arise fair sun and kill the envious moon
    Who is already sick and pale with grief
