import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password"
)

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create the database (if it doesn't exist)
cur.execute("CREATE DATABASE IF NOT EXISTS forum_db")

# Use the forum_db database
cur.execute("USE forum_db")

# Create the users table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL
    );
""")

# Create the threads table
cur.execute("""
    CREATE TABLE IF NOT EXISTS threads (
        thread_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        content TEXT NOT NULL,
        user_id INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    );
""")

# Create the comments table
cur.execute("""
    CREATE TABLE IF NOT EXISTS comments (
        comment_id INT AUTO_INCREMENT PRIMARY KEY,
        content TEXT NOT NULL,
        user_id INT,
        thread_id INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (thread_id) REFERENCES threads(thread_id)
    );
""")

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
