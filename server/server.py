import socket
import threading

host = "127.0.0.1"
port = 14169

s = socket.socket()
s.bind((host, port))
s.listen()

clients: list[socket.socket] = []
nicknames: dict[socket.socket, str] = {}

# def broadcast():


def handle(client: socket.socket):
    while True:
        try:
            message = client.recv(1024)
            # do something with the message
        except:
            index = clients.index(client)
            nickname = nicknames[client]
            clients.remove(client)
            nicknames.pop(client)
            print(f"{nickname} has disconnected.")
            client.close()
            break


def receive():
    while True:
        client, (addr, port) = s.accept()
        print(f"{addr}:{port} has connected.")
        nicknames[client] = "Un humain"

        client.send("Vous êtes connecté au service des Communications Electroniques de la France. Bienvenue.".encode())
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()

