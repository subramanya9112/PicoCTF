import socket


def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    data = s.recv(1024)
    s.shutdown(socket.SHUT_WR)
    s.close()
    return data.decode("utf-8")


hostname = "saturn.picoctf.net"
port = 51109
data = netcat(hostname, port)
exec("print(" + data + ")")
