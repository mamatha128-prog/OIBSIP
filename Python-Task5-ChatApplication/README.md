# Python Chat Application

## Oasis Infobyte SIP – Python Programming Task 5

### Task: Chat Application

## Objective

The objective of this project is to build a simple real-time chat application using Python sockets.

The application allows two users to connect to a server and exchange messages in real time.

## Technologies Used

- Python
- Socket Programming
- Threading
- DateTime

## Features

- Real-time two-way messaging
- Client-server communication
- Supports two users
- Displays timestamps with messages
- Handles client connection and disconnection
- Graceful disconnection using `/quit`
- Runs locally using `localhost`

## Project Structure

```text
Python-Task5-ChatApplication/
│
├── server.py
├── client.py
├── requirements.txt
├── README.md

## Example Working

### Server Terminal

```text
CHAT APPLICATION SERVER

Server started on 127.0.0.1:5000
Waiting for clients...

Mamatha connected
Friend connected


CLIENT 1 – MAMATHA:

Enter your name: Mamatha

Connected to the chat!

You: Hello!
You: How are you?


CLIENT 2 – FRIEND:

Enter your name: Friend

Connected to the chat!

[12:40] Mamatha: Hello!
You: Hi Mamatha!

[12:41] Mamatha: How are you?
You: I am fine!


WHEN A USER LEAVES:

You: /quit

Disconnected from chat.


SERVER:

[12:42] Mamatha left the chat.


FEATURES DEMONSTRATED:

1. Two users can connect to the server.
2. Users can send messages to each other.
3. Messages are displayed in real time.
4. Messages include timestamps.
5. Users can disconnect using /quit.
6. The server handles users joining and leaving the chat.
