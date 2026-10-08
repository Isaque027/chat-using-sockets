import socket
from datetime import datetime
from tcp import rec_message, send_message

def run_server(HOST = "127.0.0.1", PORT = 9000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (HOST, PORT)
    server.bind(server_address)

    server.listen()
    print(f"Servidor escutando no endereço {HOST}:{PORT}")
    
    client_connection, client_addres = server.accept()
    print(f"Conexão com cliente aceita: {client_addres}!")

    while True:
        message = rec_message(client_connection)
        if message is None:
            print("Cliente fechou conexão!")
            break
        if message.startswith("/msg "):
            print(f"Cliente: {message[5:]}")
            response = input("Digite uma resposta:\n")
            send_message(client_connection, response)
        elif message.startswith("/hora"):
            print("Cliente pediu horário")
            response = datetime.now().strftime("%H:%M")
            send_message(client_connection, response)
        elif message.startswith("/sair"):
            print("Cliente encerrou o chat")
            response = "/sair"
            send_message(client_connection, response)
            break
        else:
            print("Cliente digitou um comando inválido")
            response = "Comando Inválido"
            send_message(client_connection, response)
        

    client_connection.close()
    print("Conexão encerrada!")

run_server()

