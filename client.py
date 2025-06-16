import socket

HOST = '127.0.0.1'  # IP do servidor
PORT = 65432 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        mensagem = input("[CLIENTE] Digite a mensagem para o servidor: ")
        s.sendall(mensagem.encode())
        data = s.recv(1024)
        if mensagem == "Sair" or mensagem == "sair":
            print("[Cliente] Conexão fechada!")
            exit(1)
