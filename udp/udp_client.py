import socket
import threading
import random

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("0.0.0.0", 9000))

name = input("Nickname: ")

def receive():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except:
            pass

t = threading.Thread(target=receive)
t.start()

client.sendto(f"SIGNUP_TAG:{name}".encode(), ("192.168.1.110", 9000))

while True:
    message = input("")
    if message == "!q":
        exit()
    else:
        client.sendto(f"[{name}] {message}".encode(), ("192.168.1.110", 9000))