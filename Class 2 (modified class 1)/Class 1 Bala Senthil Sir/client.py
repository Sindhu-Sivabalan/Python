import socket
import time
import threading
import tkinter



wn=tkinter.Tk()
sk=socket.socket()



def connecttoserver():
    sk.connect((socket.gethostname(),1234))


def sendmsg():
    sk.send(t1.get().encode())
    
b1=tkinter.Button(wn,text='Connect',command=connecttoserver,font=(16))
b1.pack()

t1=tkinter.Entry(wn,font=(16))
t1.pack()

b2=tkinter.Button(wn,text='Send',font=(16),command=sendmsg)
b2.pack()


