import socket
import threading
import pickle
import sqlite3
import secrets
import hashlib

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
    #check cred validity
    print(f"received credentials {user}-{pwd}")
    cur.execute(f'insert into users values("{user}", "{pwd}")')
    user_db.commit()
    return user

def login_user(client: socket.socket):
    print("sending OK")
    client.send("OK".encode())
    user, pwd = pickle.loads(client.recv(1024))
    #check cred validity
    print(f"received credentials {user}-{pwd}")
    db_entry = cur.execute(f"select * from users where user='{user}'").fetchall()

    if len(db_entry) == 0:
        print(f"user '{user}' doesnt exist.")
        client.send("INV_USR".encode())
        return
    
    if pwd != db_entry[0][1]:
        print(f"invalid password (correct pwd is{db_entry[0][1]})")
        client.send("INV_PWD".encode())
        return
    
    print(f"{user} has logged in.")
        
    return user


def handle_connection(client: socket.socket):
    try:
        #acknowledge the connection
        client_ip = client.getpeername()
        print(f"{client_ip} has connected.")
        client.send("youve connected to the host".encode())
        
        #receive greet and perform reg/log
        greet = client.recv(1024).decode()
        if greet == "REG":
            print(f"{client_ip} has requested to register")
            user = register_user(client)
            if user is None:
                client.close()
                return
        elif greet == "LOG":
            print("client has requested to log in")
            user = login_user(client)
            if user is None:
                client.close()
                return
        else:
            print("client has sent an invalid greet")
            client.close()
            return
    except:
        print(f"{client_ip} has disconnected.")
    
    while True:
        try:
            message = client.recv(1024)
            if len(message) == 0:
                raise ValueError
            print(message, "its me")
        except:
            # nickname = nicknames[client]
            clients.remove(client)
            # nicknames.pop(client)
            print(f"{user} has disconnected.")
            client.close()
            return


def receive():
    while True:
        client, (addr, port) = s.accept()
        clients.append(client)
        thread = threading.Thread(target=handle_connection, args=(client,))
        thread.start()


receive()

