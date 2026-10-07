
def rec_message(client_connection):
    data = client_connection.recv(1024)
    
    if data:
        return data.decode("utf-8").rstrip("\n")

    return None

def send_message(client_connection, message):
    client_connection.sendall((message + "\n").encode("utf-8"))