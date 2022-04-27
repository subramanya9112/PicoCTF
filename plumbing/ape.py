import socket
import hashlib
import time


def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))

    data = ""
    while True:
        data = s.recv(1024).decode("utf-8")
        if data.find("pico") != -1:
            data = data.split("\n")
            for p in data:
                if p.find("pico") != -1:
                    print(p)
            break
    s.shutdown(socket.SHUT_WR)
    s.close()


hostname = "jupiter.challenges.picoctf.org"
port = 14291
netcat(hostname, port)
