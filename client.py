import threading
import socket

# Ask the user to enter username
username = input('Enter a username >>>')

# Create the socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))  # Ensure the server is running on this IP and port

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "username?":
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except ConnectionResetError:
            print('Connection closed by the server.')
            client.close()
            break
        except Exception as e:
            print(f'Error: {e}')
            client.close()
            break

def client_send():
    while True:
        message = f'{username}: {input("")}'
        try:
            client.send(message.encode('utf-8'))
        except Exception as e:
            print(f'Error: {e}')
            client.close()
            break


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()


send_thread = threading.Thread(target=client_send)
send_thread.start()
