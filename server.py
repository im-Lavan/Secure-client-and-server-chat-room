# import statements.
# Import the threading module to handle concurrent tasks
# Import the socket module to create network connections
# Import the sqlite3 module to interact with a SQLite database
# Import the hashlib module to perform secure hashing of passwords
import threading
import socket
import sqlite3
import hashlib

# assigning Local IP, port
host = "127.0.0.1"
port = 37

# creating a server socket and start listening from connections.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# create an empty list to get clients and nick_names.
clients = []
nick_Names = []


# defining functions that I use in this code.
# broadcast the message to other active clients in run time.
def broadcast(message):
    for client in clients:
        client.send(message)


## function to handle clients connection
def handle_clients(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                index = clients.index(client)
                nickname = nick_Names[index]
                broadcast(f"{message.decode('utf-8')}".encode("utf-8"))
        except:
            index = clients.index(client)
            disconnected_nickname = nick_Names[index]
            clients.remove(client)
            client.close()
            nick_Names.remove(disconnected_nickname)
            print(f"{disconnected_nickname} left the chat room.")
            broadcast(f"{disconnected_nickname} has left the chat.".encode("utf-8"))
            break


# main function to receive the clients connection
# print welcome message
def receive():
    while True:
        print("Server is Listening....🦻🏼")
        client, address = server.accept()

        # Handle login process
        # check username and password
        # save the password use hashlib to save from threats.
        print("Database is connected successfully.")
        client.send("username:".encode())
        username = client.recv(1024).decode()
        client.send("password:".encode())
        password = client.recv(1024)
        password = hashlib.sha256(password).hexdigest()

        # connect the sqlite database and check the user's credentials.
        conn = sqlite3.connect("staffdata.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM staffdata WHERE username = ? AND password = ?", (username, password))
        if cur.fetchall():

            # Check if the username is already logged in
            # if yes broadcast to server about their entry
            # close connection with them.
            if username in nick_Names:
                print(
                    f"Someone trying to re-enter into chat room by {username}'s username from this address: {address}.".encode())
                client.send("You are already logged in. Please try a different account.".encode())
                client.close()
                continue

            client.send("Login Successful".encode())

            # Proceed with chatroom process
            # adding nicknames to the list
            # broadcast message to the client and server about new entered and exit clients.
            client.send("Nick Name?".encode("utf-8"))
            nick_Name = client.recv(1024)
            nick_Names.append(username)
            clients.append(client)
            print(f" {username}; joined in The chat as {nick_Name}".encode("utf-8"))
            client.send("You are connected.\n".encode("utf-8"))
            broadcast(f"{nick_Name} has connected in this chat.".encode("utf-8"))

            thread = threading.Thread(target=handle_clients, args=(client,))
            thread.start()
        else:
            # broadcast to server if anyone try to get in to the room.
            print(f"Anonymous encountered blocked by server from: {address}")
            client.send("Login Failed".encode())
            client.close()


# start the main server loop to receive and handle client connections.
receive()
