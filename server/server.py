import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 12000))
server.listen(1)

connection, address = server.accept()

print('conectado!')

msm1 = connection.recv(1024).decode()


if msm1:

    mensagem = 'Arquivos disponiveis: Nota10.txt e Porque-nota10.jpeg'

    connection.sendto(mensagem.encode(), address)

file = connection.recv(1024).decode()

with open(file, 'rb') as f:
    for data in f.readlines():
        connection.send(data)

    print('Arquivo enviado com sucesso!')