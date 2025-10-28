# import statements.
# Import the threading module to handle concurrent tasks
# Import the socket module to create network connections
import threading
import socket

# getting nickname for this chat
nick_name = input("Give a name for you in this chat.. ")

# create a client socket and connect to the server.
# assigning Local IP, port.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 37))


# Handle login process for the client
# receive username from server.
# send the user's username to the server.
# receive password from the user
# send the user's password to the server.
client.recv(1024).decode()
client.send(input("Username: ").encode())
client.recv(1024).decode()  # Receive "password:"
client.send(input("Password: ").encode())
login_status = client.recv(1024).decode()
# check the login status and handle the different scenarios.
if login_status == "Login Failed":
    print("Login failed. Exiting...")
    client.close()
    exit()
elif login_status == "You are already logged in. Please try a different account.":
    print("This user is already logged in the room.")
    client.close()
    exit()


# functions for receive message from the server.
def client_receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "Nick Name?":
                client.send(nick_name.encode("utf-8"))
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break

# functions for send message to the server.
def client_send():
    while True:
        message = f"{nick_name}: {input('')}"
        client.send(message.encode("utf-8"))


# create and start threads for receiving and sending message.
receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()