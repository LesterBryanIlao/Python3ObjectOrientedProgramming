from socket import socket, AF_INET, SOCK_STREAM


def respond(client):
    response = input('Enter a value: ')
    client.send(bytes(response, 'utf8'))
    client.close()


server = socket(AF_INET, SOCK_STREAM)
server.bind(("localhost", 2401))
server.listen(1)

try:
    while True:
        client, addr = server.accept()
        respond(client)
finally:
    server.close()
