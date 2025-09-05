import socket
import threading
import pickle
import sqlite3
from client.util_functions import parse_msg

HOST = "koei.hackclub.app"
PORT = 14169

s = socket.socket()
s.bind((HOST, PORT))
s.listen()

clients: dict[str, socket.socket] = {}


def register_user(client: socket.socket):
    user_db = sqlite3.connect("user.db")
    cur = user_db.cursor()

    client.send("OK".encode())
    user, pwd = pickle.loads(client.recv(1024))
    print(f"received credentials {user}-{pwd}")

    # check cred validity

    db_entry = cur.execute(f"select * from users where user='{user}'").fetchall()
    if len(db_entry) != 0:
        client.send("USER_EXISTS".encode())
        print(f"user {user} already exists.")
        return
    client.send("SUCCESS".encode())
    cur.execute(f'insert into users values("{user}", "{pwd}")')

    user_db.commit()
    return user


def login_user(client: socket.socket):
    user_db = sqlite3.connect("user.db")
    cur = user_db.cursor()

    client.send("OK".encode())
    print("sent OK, waiting for response")
    response = client.recv(1024)
    user, pwd = pickle.loads(response)

    # check cred validity

    print(f"received credentials {user}-{pwd}")

    db_entry = cur.execute(f"select * from users where user='{user}'").fetchall()

    if len(db_entry) == 0:
        print(f"user '{user}' doesnt exist.")
        client.send("INV_USR".encode())
        return

    if pwd != db_entry[0][1]:
        print(f"invalid password (correct pwd is {db_entry[0][1]})")
        client.send("INV_PWD".encode())
        return

    client.send("SUCCESS".encode())
    print(f"{user} has logged in.")

    return user


def handle_connection(client: socket.socket):

    # acknowledge the connection
    client_ip = client.getpeername()
    print(f"{client_ip} has connected.")

    # receive greet and perform reg/log
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
        clients[user] = client
    else:
        print("client has sent an invalid greet")
        client.close()
        return

    while True:
        try:
            message = client.recv(1024)
            forward_message(message)
            if len(message) == 0:
                raise ValueError
            print(f"{user}:\t {message}")
        except:
            clients.pop(user)
            print(f"{user} has disconnected.")
            client.close()
            return


def forward_message(msg: bytes):
    sender, receiver, content = parse_msg(msg)
    print(f"{sender} wants to send '{content}' to {receiver}")
    try:
        clients[receiver].send(msg)
    except:
        print(f"error: {receiver} is not connected to the server.")



def receive():
    print(f"Server is listening on {HOST}:{PORT}")
    while True:
        client, (addr, port) = s.accept()
        thread = threading.Thread(target=handle_connection, args=(client,))
        thread.start()


receive()
