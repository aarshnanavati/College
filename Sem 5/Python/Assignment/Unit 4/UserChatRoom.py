# Build a Python program for a multi-user chat application using object-oriented programming. 
# Create classes for User and ChatRoom. Ensure proper error handling when sending messages to non-existing 
# users or empty rooms.

# ------------------ User Class ------------------
class User:
    def __init__(self, username):
        self.username = username

    def receive_message(self, sender, message):
        print(f"[{sender}] → {self.username}: {message}")


# ------------------ ChatRoom Class ------------------
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = {}

    def add_user(self, user):
        if user.username in self.users:
            print(f"⚠️ {user.username} is already in the chat room.")
        else:
            self.users[user.username] = user
            print(f"✅ {user.username} joined '{self.room_name}'.")

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            print(f"🚪 {username} left the chat room.")
        else:
            print(f"⚠️ No such user '{username}' in the chat room.")

    def send_message(self, sender_name, message):
        try:
            # Check if room is empty
            if not self.users:
                raise ValueError("Cannot send message. The chat room is empty!")

            # Check if sender exists
            if sender_name not in self.users:
                raise ValueError(f"User '{sender_name}' not found in chat room!")

            # Deliver message to all except sender
            sender = self.users[sender_name]
            for username, user in self.users.items():
                if username != sender_name:
                    user.receive_message(sender.username, message)

        except ValueError as e:
            print(f"⚠️ Error: {e}")

    def show_users(self):
        if self.users:
            print("👥 Users in chat room:")
            for u in self.users:
                print(" -", u)
        else:
            print("⚠️ No users currently in the chat room.")


# ------------------ Main Program ------------------
def main():
    print("===== Multi-User Chat Application =====")
    room = ChatRoom("Python Room")

    while True:
        print("\n1. Add User")
        print("2. Remove User")
        print("3. Show Users")
        print("4. Send Message")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter username: ")
            user = User(name)
            room.add_user(user)

        elif choice == '2':
            name = input("Enter username to remove: ")
            room.remove_user(name)

        elif choice == '3':
            room.show_users()

        elif choice == '4':
            sender = input("Enter sender name: ")
            msg = input("Enter message: ")
            room.send_message(sender, msg)

        elif choice == '5':
            print("👋 Exiting chat application...")
            break

        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
