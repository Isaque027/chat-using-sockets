
def rec_message(client_connection):
    data = client_connection.recv(1024)
    
    if data:
        return data.decode("utf-8")

    return None

def send_message(client_connection, message):
    client_connection.sendall(message.encode("utf-8"))