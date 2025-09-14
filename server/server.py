import socket
import threading
import pickle
import sqlite3
from util_functions import parse_msg
from logger import log, warn, error, success, message

HOST = "localhost"
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
    log(f"received credentials {user}-{pwd}")
    db_entry = cur.execute(f"select * from users where user='{user}'").fetchall()
    if len(db_entry) != 0:
        client.send("USER_EXISTS".encode())
        error(f"user {user} already exists.")
        return
    client.send("SUCCESS".encode())
    cur.execute(f'insert into users values("{user}", "{pwd}")')

    user_db.commit()
    return user


def login_user(client: socket.socket):
    user_db = sqlite3.connect("user.db")
    cur = user_db.cursor()

    client.send("OK".encode())
    log("sent OK, waiting for response")
    response = client.recv(1024)
    user, pwd = pickle.loads(response)

    # check cred validity

    log(f"received credentials {user}-{pwd}")

    db_entry = cur.execute(f"select * from users where user='{user}'").fetchall()

    if len(db_entry) == 0:
        error(f"user '{user}' doesnt exist.")
        client.send("INV_USR".encode())
        return

    if pwd != db_entry[0][1]:
        error(f"invalid password (correct pwd is {db_entry[0][1]})")
        client.send("INV_PWD".encode())
        return

    client.send("SUCCESS".encode())
    success(f"{user} has logged in.")

    return user


def handle_connection(client: socket.socket):

    # acknowledge the connection
    client_ip = client.getpeername()
    log(f"{client_ip} has connected.")

    # receive greet and perform reg/log
    greet = client.recv(1024).decode()
    if greet == "REG":
        log(f"{client_ip} has requested to register")
        user = register_user(client)
        if user is None:
            client.close()
            return
        clients[user] = client
    elif greet == "LOG":
        log("client has requested to log in")
        user = login_user(client)
        if user is None:
            client.close()
            return
        clients[user] = client
    else:
        warn("client has sent an invalid greet, closing connection")
        client.close()
        return

    while True:
        try:
            message = client.recv(1024)
            if message.decode() in KNOWN_WORDS:
                KNOWN_WORDS[message.decode()](client)
                continue
            else:
                forward_message(message)
            if len(message) == 0:
                raise ValueError
        except:
            clients.pop(user)
            warn(f"{user} has disconnected.")
            client.close()
            return


def send_user_list(client: socket.socket):
    log("user has requested user list")
    user_db = sqlite3.connect("user.db")
    cur = user_db.cursor()
    users = cur.execute(f"select user from users").fetchall()
    user_list = []
    for i in users:
        user_list.append(i[0])
    log(f"sending {user_list}")
    client.send(pickle.dumps(user_list))


def forward_message(msg: bytes):
    sender, receiver, content = parse_msg(msg)
    message(f"{sender}->{receiver}: {content}")
    try:
        clients[receiver].send(msg)
    except:
        error(f"error: {receiver} is away")


def receive():
    success(f"Server is listening on {HOST}:{PORT}")
    while True:
        client, (addr, port) = s.accept()
        thread = threading.Thread(target=handle_connection, args=(client,))
        thread.start()


KNOWN_WORDS = {
    "GET_USERS": send_user_list,
}

receive()
