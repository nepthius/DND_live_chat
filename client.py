import socket
import threading
from _thread import *
import os

HOST = "localhost"
PORT = 5050
ADDR = (HOST, PORT)
FORMAT = "utf-8"
HEADER = 1024
CLIENTS = {}
DISCONNECT_MESSAGE = "quit!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def client_to_server():
    #print("in the client_to_server!")
    Connection = False

    try:
        client.connect(ADDR)
        Connection = True

    except:
        print("The tavern is busy or undergoing maintence, check in later!")
        client.close()

    if Connection:
        #print("in connection!")
        print("*Welcome to the inn laddy!")
        print("*Press enter to enter the inn...")
        RECIEVE_THREAD = threading.Thread(target=receive_messages)
        RECIEVE_THREAD.start()



def receive_messages():
    
    MESSAGE_LOG = ""

    SEND_THREAD = threading.Thread(target = send_message)
    SEND_THREAD.start()

    while True:
        try:
            message = client.recv(HEADER).decode(FORMAT)
            MESSAGE_LOG += message

            if message != DISCONNECT_MESSAGE:
                clear()
                print(MESSAGE_LOG)
            
            else:
                client.close()
                break


        except OSError:
            break




def send_message():
    while True:
        message = input(">>")
    
        try:
            if message != DISCONNECT_MESSAGE:
                client.send(message.encode(FORMAT))
            else:
                client.send(message.encode(FORMAT))
                break

        except:
            print("Connection has been disrupted. Tavern is closed, sorry!")
            break


def Main():
    clear()
    client_to_server()

if __name__ == '__main__':
    Main()