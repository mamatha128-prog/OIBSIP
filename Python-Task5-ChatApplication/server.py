import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000

clients = {}
lock = threading.Lock()


def timestamp():
    return datetime.now().strftime("%H:%M")


def broadcast(message, sender_socket=None):
    with lock:
        for client_socket in list(clients.keys()):
            if client_socket != sender_socket:
                try:
                    client_socket.send(message.encode())
                except:
                    pass


def handle_client(client_socket, address):
    try:
        username = client_socket.recv(1024).decode()

        with lock:
            clients[client_socket] = username

        print(f"{username} connected from {address}")

        join_message = f"[{timestamp()}] {username} joined the chat."
        print(join_message)
        broadcast(join_message, client_socket)

        while True:
            data = client_socket.recv(1024)

            if not data:
                break

            message = data.decode()

            if message.lower() == "/quit":
                break

            chat_message = f"[{timestamp()}] {username}: {message}"

            print(chat_message)
            broadcast(chat_message, client_socket)

    except ConnectionResetError:
        pass

    finally:
        with lock:
            username = clients.pop(client_socket, "Unknown")

        client_socket.close()

        leave_message = f"[{timestamp()}] {username} left the chat."
        print(leave_message)
        broadcast(leave_message)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print("=" * 40)
    print("      CHAT APPLICATION SERVER")
    print("=" * 40)
    print(f"Server started on {HOST}:{PORT}")
    print("Waiting for clients...")
    print("Press Ctrl+C to stop the server.")

    try:
        while True:
            client_socket, address = server.accept()

            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address),
                daemon=True
            )
            thread.start()

    except KeyboardInterrupt:
        print("\nServer stopped.")

    finally:
        server.close()


if __name__ == "__main__":
    start_server()
