import tkinter
import socket
import time
import threading


mywindow=tkinter.Tk()
mywindow.title('Server-Client ')
mywindow.geometry('600x400')
allclients=[]
allmsg=tkinter.StringVar()

class ReadMessage:
    def __init__(self,client):
        self.socket=client
        t1=threading.Thread(target=self.readdata)
        t1.start()

    def readdata(self):
        while True:
            txt=self.socket.recv(1024)
            allmsg.set(bytes.decode(txt))

def dummy():
    msg.set('Hello python')
def startserver():
    
    sk=socket.socket()
    sk.bind((socket.gethostname(),1234))
    sk.listen()
    while True:
        csk,addr=sk.accept()
        x=ReadMessage(csk)
        allclients.append(csk)
        msg.set(str(len(allclients))+ 'Connected ....')
        
def serv():
    t1=threading.Thread(target=startserver)
    t1.start()
msg=tkinter.StringVar()
msg.set('helolo')
tkinter.Button(mywindow,text='Start Server',command=serv).pack()

tkinter.Label(mywindow,textvariable=msg).pack()
tkinter.Label(mywindow,textvariable=allmsg).pack()

mywindow.mainloop()
