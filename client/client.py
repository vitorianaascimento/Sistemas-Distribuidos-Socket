import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 12000))
print('Conectado!\n')

client.send('Olá'.encode())
msm = client.recv(1024).decode()

if not msm:
    print("Nenhuma mensagem!")
else:    
    print(msm)

file = str(input("Insira o nome do arquivo: "))

client.send(file.encode())
with open(file, 'wb') as f:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        f.write(data)

print(f'{file} recebido com sucesso!')