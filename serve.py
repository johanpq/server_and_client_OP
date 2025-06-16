import socket

HOST = '127.0.0.1'
PORT = 65432

# Cria o socket do servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVIDOR] Aguardando conexões em {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[SERVIDOR] Conectado por {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("[SERVIDOR] Conexão encerrada pelo cliente.")
                    exit(1)

                mensagem = data.decode().strip()
                print(f"[SERVIDOR] Recebido: {mensagem}")

                if mensagem.lower() == "sair":
                    print("[SERVIDOR] Cliente solicitou saída.")
                    exit(1)

                resposta = "Mensagem recebida com sucesso!"
                conn.sendall(resposta.encode())