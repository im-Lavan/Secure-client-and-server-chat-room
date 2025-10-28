# 💬 Network-Based Chat Application

> 🧑‍💻 *This is my **Year 1 Programming project**. It demonstrates a basic client–server chat application with user authentication, database integration, and message broadcasting.*

## 🧰 Tech Stack
- **Language:** Python 3
- **Modules:**
  - socket – networking
  - threading – concurrent connections
  - sqlite3 – user credential database
  - hashlib – password hashing

## 📂 Project Structure
```
├── Database.py   # Handles SQLite database and user credential storage
├── server.py     # Runs the chat server, manages connections and authentication
├── client.py     # Runs the chat client, connects to server and sends messages
├── staffdata.db  # SQLite database generated at runtime
└── README.md
```

## 🔑 Features
- Client–Server Architecture: Multiple clients connect to one server.
- Authentication: Login required with username and password (stored securely in SQLite).
- Threading: Concurrent message send/receive for smooth real-time chat.
- Broadcasting: All messages sent by one client are shared with everyone in the room.
- Nickname Support: Clients can choose a display name on entry.
- Password Security: SHA-256 hashing ensures no plain text storage.

## 🧪 Predefined Credentials
| Username   | Password              |
|------------|------------------------|
| Azer1215   | Bananafromsky1089     |
| Zander     | zander_xm             |
| Andrew     | andrew1000           |
| James      | Jamesbrain80         |

## ⚙️ Installation
1. Clone the repository:
```bash
git clone https://github.com/im-lavan/Secure-client-and-server-chat-room.git
cd Secure-client-and-server-chat-room
```

2. Run the database setup:
```bash
python Database.py
```

3. Start the server:
```bash
python server.py
```

4. Start the client (in a new terminal):
```bash
python client.py
```

> 📌 Start the server before launching any clients. Use the same port for both.

## 🖥️ How It Works
1. Server runs and listens for connections.
2. Clients connect and enter:
   - Username and Password (must match database).
   - Nickname for chat display.
3. Server verifies credentials:
   - Valid → joins chat.
   - Invalid → denied access.
4. Messages are broadcast to all active clients in real time.

## 🛡️ Security Notes
- Passwords are hashed using SHA-256 before storage.
- Duplicate logins with the same account are blocked.
- Invalid attempts are logged on the server side.

## 🚀 Future Improvements
- Save chat history per client.
- Add GUI.
- Enable mobile access.
- Multi-room support.
- Icon picker for nicknames.

## 📝 Acknowledgements
- Project developed for the **Year 1 Programming Module** at NTU.
- All usernames and passwords used here are for demonstration only.
