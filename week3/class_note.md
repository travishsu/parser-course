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

## Socket in Python
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
