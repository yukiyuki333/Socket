import socket
SERVER=socket.gethostbyname(socket.gethostname())
PORT=7000
ADDR=(SERVER,PORT)
FORMAT="utf-8"
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(ADDR)
def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connect=True
    while connect:
        msg=conn.recv(1024).decode(FORMAT)
        print("Recieve ",msg)
        if msg=="quit":
            connect=False
    conn.close()
    s.close()
def start():
    s.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    conn,addr=s.accept()
    handle_client(conn,addr)
print("start")
start()



