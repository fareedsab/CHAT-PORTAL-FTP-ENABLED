import socket
import time
from http import server
import os
import socket
import threading
PORT = 5080
temp = 'false'
SIZE = 1024
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
clients, names = [], []
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDRESS)
def startserver():
    print("server is working on " + SERVER)
    server.listen()
    while True:
        conn, addr = server.accept()
        conn.send("NAME".encode(FORMAT))
        name = conn.recv(1024).decode(FORMAT)
        names.append(name)
        clients.append(conn)
        print(f"Name is :{name}")
        startchat(conn,addr,name)
        print(f"active connections {threading.active_count()}")
        
def handle_client(conn,addr):
    temp= False
    if temp==False:
        print('hello')
        file_name =conn.recv(100).decode(FORMAT)
        print(file_name)
        print('decode')
        file_size = os.path.getsize(file_name)
        print(file_size)
        conn.send(file_name.encode(FORMAT))
        print('hello33333')
        conn.send(str(file_size).encode(FORMAT))
        print('file size and name encode')
        with open(file_name, "rb") as file:
            c = 0
            start_time = time.time()
            while c <= file_size:
                data = file.read(4000)
                if not (data):
                    break
                conn.sendall(data)
                c += len(data)
                print(c,file_size)
            end_time = time.time()
            print("------------------server")
            # conn.send('19k0267'.encode('utf-8'))
            print("File Transfer Complete.Total time: ", end_time - start_time)
        #conn.close()
    #startserver()
def startchat(conn,addr,name):
    broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))
    conn.send('Connection successful!'.encode(FORMAT))
    thread = threading.Thread(target=handle,args=(conn, addr))
    thread.start()
def handle(conn, addr):
    print(f"new connection {addr}")
    connected = True
    while connected:
        message = conn.recv(1024)
        if  "band" in str(message):
            print("mil gaya")
            handle_client(conn,addr)
            #print(message)
        else:
            print(str(message))
            broadcastMessage(message)
            #print(message)
            print("haan1")
    conn.close()
def broadcastMessage(message):
    for client in clients:
        client.send(message)
startserver()