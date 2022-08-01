import socket
import threading
from tkinter import *
from tkinter import font
from tkinter import ttk
import os
#import server as sv
import time
temp=1
PORT = 5080
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
SIZE = 1024
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()
        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)
        self.pls = Label(self.login,text="Please login to continue",justify=CENTER,font="Helvetica 14 bold")
        self.pls.place(relheight=0.15,relx=0.2,rely=0.07)
        self.labelName = Label(self.login,text="Name: ",font="Helvetica 12")
        self.labelName.place(relheight=0.2,relx=0.1,rely=0.2)
        self.entryName = Entry(self.login,font="Helvetica 14")
        self.entryName.place(relwidth=0.4,relheight=0.12,relx=0.35,rely=0.2)
        self.entryName.focus()
        self.go = Button(self.login,text="START CHAT",font="Helvetica 14 bold",command=lambda: self.goAhead(self.entryName.get()))
        self.go.place(relx=0.4,rely=0.55)
        self.Window.mainloop()
    def goAhead(self, name):
        self.login.destroy()
        
        self.layout(name)
        rcv = threading.Thread(target=self.receive)
        rcv.start()
    def receive(self):
        while True:
            try:
                print(temp)
                if temp==1:
                    message = client.recv(1024).decode(FORMAT)
                    if message=='NAME':
                        client.send(self.name.encode(FORMAT))
                    elif temp==0:
                        pass
                    else:
                        self.textCons.config(state=NORMAL)
                        self.textCons.insert(END,message+"\n\n")
                        self.textCons.config(state=DISABLED)
                        self.textCons.see(END)
                else:
                    pass
            except:
                print("An error occured!")
                client.close()
                break
    def sendButton(self, msg):
        self.textCons.config(state=DISABLED)
        self.msg = msg
        self.entryMsg.delete(0, END)
        snd = threading.Thread(target=self.sendMessage)
        snd.start()
    def layout(self, name):
        self.name = name
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width=False,height=False)
        self.Window.configure(width=470,height=550,bg="#17202A")
        self.labelHead = Label(self.Window,bg="#17202A",fg="#EAECEE",text=self.name,font="Helvetica 13 bold",pady=5)
        self.labelHead.place(relwidth=1)
        self.line = Label(self.Window,width=450,bg="#ABB2B9")
        self.line.place(relwidth=1,rely=0.07,relheight=0.012)
        self.textCons = Text(self.Window,width=20,height=2,bg="#17202A",fg="#EAECEE",font="Helvetica 14",padx=5,pady=5)
        self.textCons.place(relheight=0.745,relwidth=1,rely=0.08)
        self.labelBottom = Label(self.Window,bg="#ABB2B9",height=80)
        self.labelBottom.place(relwidth=1,rely=0.825)
        self.entryMsg = Entry(self.labelBottom,bg="#2C3E50",fg="#EAECEE",font="Helvetica 13")
        self.entryMsg.place(relwidth=0.74,relheight=0.06,rely=0.008,relx=0.011)
        self.entryMsg.focus()
        self.buttonMsg = Button(self.labelBottom,text="get files",font="Helvetica 10 bold",width=20,bg="#ABB2B9",command=lambda: self.create(1,name))
        self.buttonMsg.place(relx=0.77,rely=0.055,relheight=0.02,relwidth=0.22)
        self.buttonMsg = Button(self.labelBottom,text="Send",font="Helvetica 10 bold",width=20,bg="#ABB2B9",command=lambda: self.sendButton(self.entryMsg.get()))
        self.buttonMsg.place(relx=0.77,rely=0.0085,relheight=0.02,relwidth=0.22)
        self.buttonMsg = Button(self.labelBottom,text="upload file",font="Helvetica 10 bold",width=20,bg="#ABB2B9",command=lambda: self.create(2,name))
        self.buttonMsg.place(relx=0.77,rely=0.035,relheight=0.02,relwidth=0.22)
        self.textCons.config(cursor="arrow")
        scrollbar = Scrollbar(self.textCons)
        scrollbar.place(relheight=1,relx=0.974)
        scrollbar.config(command=self.textCons.yview)
        self.textCons.config(state=DISABLED)
    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        while True:
            message = (f"{self.name}: {self.msg}")
            client.send(message.encode(FORMAT))
            print("haan")
            break
    def create(self,num,name2):
        self.win = Toplevel()
        #self.Win.configure(width=470,height=550,bg="#17202A")
        if num ==1:
            self.win.title('Get files')
            self.win['bg'] = '#154360'
            self.win
            self.win.geometry("400x400")
            self.mylistbox=Listbox(self.win,width=50, height=10)
            self.mylistbox.pack(pady=20)
            self.mylistbox.insert(END,"List of files")
            self.mylistbox.insert(END,"")
            parent_dir=os.getcwd()
            print(parent_dir)
            # path = os.path.join(parent_dir,"server")
            # print(path)
            # os.chdir(path)
            # print(os.getcwd())
            self.myList = os.listdir(os.getcwd())
            for file in self.myList:
                if os.path.isfile(file):
                    self.mylistbox.insert(END, file)
            os.chdir(parent_dir)
            print(os.getcwd())
            self.labelName = Label(self.win,text="Enter The File Name: ",font="Helvetica 13",background='#154360',foreground='white')
            self.labelName.place(relheight=0.1,relx=0.0,rely=0.7)
            self.entryName = Entry(self.win,font="Helvetica 14")
            self.entryName.place(relwidth=0.5,relheight=0.1,relx=0.4,rely=0.7)
            self.entryName.focus()
            self.go = Button(self.win,text="GET A FILE",font="Helvetica 10 bold",width=20,bg="white",command=lambda: self.request1(self.entryName.get(),name2))
            self.go.place(relx=0.7,rely=0.85,relheight=0.02,relwidth=0.22,height=30)
        elif num ==2:
            self.win.title('upload files')
    def request(self,name1,oname):
        thread3=threading.Thread(target=self.request1,args=(name1,oname))
        thread3.start()
    def request1(self,name1,oname):
        client.send('band'.encode(FORMAT))
        client.send(name1.encode(FORMAT))
        # print("ahsan")
        try:
            os.mkdir(oname)
        except:
            pass
        # print("ahsan1")
        parent_dir=os.getcwd()
        path = os.path.join(parent_dir,oname)
        os.chdir(path)
        # file_name = client.recv(100).decode()
        # file_size = client.recv(100).decode()
        # print(file_name)
        # print(file_size)
        # file_name = client.recv(100).decode(FORMAT)
        # print(file_name)
        file_size = client.recv(100).decode(FORMAT)
        print(file_size)
        with open(name1, "wb") as file:
            c = 0
            start_time = time.time()
            temp=int(file_size)/4000
            print(temp)
            while c <= int(file_size):
                if c<=25:
                    data = client.recv(4000)
                else:
                    break
                # if(data.decode('utf-8')=='19k0267'):
                #     break
                if not (data):
                    break
                file.write(data)
                c += len(data)
                print(c,file_size)
        print("------------------client")
        end_time = time.time()
        os.chdir(parent_dir)
        print("File transfer Complete.Total time: ", end_time - start_time)
        # client.close()
        #rec(client,ADDRESS)
        print('complete')
        temp=0
        client.send(f"{name1} has joined the chat!".encode(FORMAT))
        self.win.destroy()
        
def rec(sock,addr):
    file_name = sock.recv(100).decode()
    file_size = sock.recv(100).decode()
    print(file_name)
    print(file_size)
    with open(file_name, "wb") as file:
        c = 0
        start_time = time.time()
        while c <= int(file_size):
            data = sock.recv(4000)
            if not (data):
                break
            file.write(data)
            c += len(data)
        end_time = time.time()
    print("File transfer Complete.Total time: ", end_time - start_time)
    sock.close()
    
def connect(client,PORT,SERVER):
    client.connect((SERVER,PORT))
connect(client,PORT,SERVER)
g=GUI()