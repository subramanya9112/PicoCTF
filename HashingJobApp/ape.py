import socket
import hashlib
import time


def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))

    data = ""
    try:
        while True:
            time.sleep(2)
            data = s.recv(1024).decode("utf-8")
            data = data.split("'")[1]
            result = hashlib.md5(data.encode()).hexdigest()
            time.sleep(2)
            s.send(result.encode())
            time.sleep(2)
            data = s.recv(1024)
            s.send("\n".encode())
    except Exception as e:
        pass
    finally:
        s.shutdown(socket.SHUT_WR)
        s.close()
        print(data.split("\n")[2])


hostname = "saturn.picoctf.net"
port = 57689
netcat(hostname, port)
