import socket
import threading
import time


sk=socket.socket()
# print(socket.gethostname())
# print(socket.gethostbyname('www.google.com'))
def readmessage():
    while True:
        txt=csk.recv(1024)
        txt=bytes.decode(txt)
        print(txt)
        if txt.upper()=='END':
            break
        time.sleep(1)


sk.bind((socket.gethostname(),1234))
sk.listen()
csk,addr=sk.accept()
print('client connected....')
t1=threading.Thread(target=readmessage)
t1.start()
