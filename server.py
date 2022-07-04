import socket
import threading
import os

HOST = ""
PORT = 5050
ADDR = (HOST, PORT)
FORMAT = "utf-8"
HEADER = 1024
CLIENTS = {}
DISCONNECT_MESSAGE = "quit!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def accepting_clients():
    while True:
        client_socket, address = server.accept()
        print(f"{address} has joined")
        client_socket.send("*Salutations weary traveler, and welcome to the inn!*\nWhat be your name around these parts: ".encode(FORMAT))
        CLIENT_THREAD = threading.Thread(target=client_handle, args=(client_socket,))
        CLIENT_THREAD.start()

 
def client_handle(client):
    username = client.recv(HEADER).decode(FORMAT)
    client.send(f"\n*Welcome {username}!\n*If you desire exit type 'quit!'".encode(FORMAT))

    message = f"*{username}* has joined the party!"
    CLIENTS[client] = username
    
    global_message(message)

    

    while True:
        try: 
            message = client.recv(HEADER).decode(FORMAT)

            if message != DISCONNECT_MESSAGE:
                global_message(username, message)
            else:
                client.close()
                del CLIENTS[client]
                print(f"{username} has left the inn")
                break
                

        except:
            continue
        



def server_commands():
    pass



def global_message(username, message=""):
    try:
        for member in CLIENTS:
            member.send(f"\n[{username}]: {message}")
    except:
        pass

def Main():
    server.listen(4)
    ACCEPT_THREAD = threading.Thread(target=accepting_clients)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    server.close()

if __name__ == '__main__':
    clear()
    print("Welcome to the inn tavernkeeper!")
    Main()