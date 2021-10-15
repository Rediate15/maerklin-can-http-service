import socket
from asyncio import Lock


IP = "10.0.0.2"
PORT = 15731

udp_lock = Lock()

async def send(message):
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
    sock.connect((IP, PORT))

    sock.sendall(message)

    sock.close()

async def recv():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
    sock.connect((IP, PORT))
    
    data = sock.recv(13)
    
    sock.close()

    return data