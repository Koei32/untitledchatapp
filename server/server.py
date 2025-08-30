import socket
import threading
import pickle
import sqlite3


host = "koei.hackclub.app"
port = 14169

s = socket.socket()
s.bind((host, port))
s.listen()

clients: list[socket.socket] = []
nicknames: dict[socket.socket, str] = {}

# def broadcast():

user_db = sqlite3.connect("user.db")
cur = user_db.cursor()
def register_user(client: socket.socket):
    print("sending OK")
    client.send("OK".encode())
    user, pwd = pickle.loads(client.recv(1024))
    print(f"received credentials {user}-{pwd}")
    cur.execute(f'insert into users values("{user}", "{pwd}")')
    user_db.commit()
    return user

def handle(client: socket.socket, user: str):
    print(f"{user} has connected ({client.getpeername()}).")
    client.send("youve connected.".encode())
    while True:
        try:
            message = client.recv(1024)
            print(message)
        except KeyboardInterrupt:
            client.close()
            return
        except:
            nickname = nicknames[client]
            clients.remove(client)
            nicknames.pop(client)
            print(f"{nickname} has disconnected.")
            client.close()
            s.close()
            break


def receive():
    while True:
        client, (addr, port) = s.accept()
        clients.append(client)
        greet = client.recv(1024).decode()
        if greet == "REG":
            print("client has requested to register")
            user = register_user(client)
        thread = threading.Thread(target=handle, args=(client, user))
        thread.start()
    
receive()

