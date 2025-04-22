import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('cloud.db')
cursor = conn.cursor()

# Create the 'users' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY
)
''')

# Create the 'messages' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    user_id INTEGER,
    message_id INTEGER,
    text TEXT,
    PRIMARY KEY (user_id, message_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
)
''')

conn.commit()

import sqlite3

def add_user(user_id):
    with sqlite3.connect('cloud.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (id) VALUES (?)', (user_id,))
        conn.commit()

def add_message(user_id, message_id, text):
    with sqlite3.connect('cloud.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO messages (user_id, message_id, text) VALUES (?, ?, ?)', 
                       (user_id, message_id, text))
        conn.commit()

def get_user_messages(user_id):
    with sqlite3.connect('cloud.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT message_id, text FROM messages WHERE user_id = ?', (user_id,))
        return cursor.fetchall()



# Example input: Add users and messages
user_id_1 = 1001  # This could be input from the user
user_id_2 = 1002

# Add users
add_user(user_id_1)
add_user(user_id_2)

# Add messages for these users
add_message(user_id_1, 10, 'Message for User 1001')
add_message(user_id_1, 11, 'Another message for User 1001')
add_message(user_id_2, 10, 'Message for User 1002')

# Retrieve and print messages for each user
messages = get_user_messages(user_id_1)
print(f"Messages for User {user_id_1}:")
for msg in messages:
    print(f"Message ID: {msg[0]}, Text: {msg[1]}")

messages = get_user_messages(user_id_2)
print(f"Messages for User {user_id_2}:")
for msg in messages:
    print(f"Message ID: {msg[0]}, Text: {msg[1]}")

# Close the connection
conn.close()
