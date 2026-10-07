import socket
from tcp import rec_message, send_message

def run_server(HOST = "127.0.0.1", PORT = 9002):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (HOST, PORT)
    server.bind(server_address)

    server.listen()
    print(f"Servidor escutando no endereço: {HOST}, porta {PORT}")
    
    client_connection, client_addres = server.accept()
    print(f"Conexão com cliente aceita: {client_addres}!")

    while True:
        message = rec_message(client_connection)
        if message is None:
            print("Cliente fechou conexão!")
            break

        print(f"Mensagem recebida: {message}")
        response = input("Digite uma resposta:\n")

        send_message(client_connection, response)

    client_connection.close()
    print("Conexão encerrada!")

run_server()

