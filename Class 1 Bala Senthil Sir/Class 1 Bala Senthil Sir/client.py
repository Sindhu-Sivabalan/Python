import socket
import time
import threading





sk=socket.socket()
sk.connect((socket.gethostname(),1234))
print('connected to server ')

while True:
    cmd=input('enter the command to do ')
    sk.send(cmd.encode())
    if cmd.upper()=='END':
        break
    
    
