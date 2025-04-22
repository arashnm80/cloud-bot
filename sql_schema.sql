CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS messages (
    user_id INTEGER,
    message_id INTEGER,
    text TEXT,
    PRIMARY KEY (user_id, message_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
