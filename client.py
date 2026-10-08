import socket
from tcp import send_message, rec_message

def client(HOST = "127.0.0.1", PORT = 9000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((HOST, PORT))
    print("Conectado ao servidor!")

    while True:
        print("\n========== Chat ==========\n")
        print('Para enviar uma mensagem digite: /msg "mensagem"')
        print('Para solicitar o horário atual digite: /hora')
        print('Para sair do chat digite: /sair')
        message = input()

        if message == "/sair":
            print("Saindo...")
            break
        
        send_message(client_socket, message)
        
        response = rec_message(client_socket)
        
        if response == "Comando Inválido":
            print("Comando Inválido")
        else:
            print(f"Servidor respondeu: {response}")

        print("\n==========================\n")

    client_socket.close()

client()