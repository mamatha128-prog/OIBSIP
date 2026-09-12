import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                print("\nDisconnected from server.")
                break

            print(f"\n{message}")
            print("You: ", end="", flush=True)

        except:
            print("\nConnection closed.")
            break


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))

        print("=" * 40)
        print("       PYTHON CHAT APPLICATION")
        print("=" * 40)

        username = input("Enter your name: ").strip()

        while not username:
            print("Name cannot be empty.")
            username = input("Enter your name: ").strip()

        client_socket.send(username.encode())

        receive_thread = threading.Thread(
            target=receive_messages,
            args=(client_socket,),
            daemon=True
        )
        receive_thread.start()

        print("\nConnected to the chat!")
        print("Type your message and press Enter.")
        print("Type /quit to leave the chat.\n")

        while True:
            message = input("You: ")

            if message.lower() == "/quit":
                client_socket.send("/quit".encode())
                break

            if message.strip():
                client_socket.send(message.encode())

    except ConnectionRefusedError:
        print("Error: Server is not running.")
        print("Please start server.py first.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()
        print("Disconnected from chat.")


if __name__ == "__main__":
    start_client()
