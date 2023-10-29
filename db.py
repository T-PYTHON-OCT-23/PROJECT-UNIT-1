import mysql.connector
# Connect to the MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="bader",
            password="root12345",
            database="forum_db"  # Assuming your database is already created
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def close_connection(conn):
    conn.close()

def create_tables(conn):
    try:
        cursor = conn.cursor()
        
        # Create the users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL,
                email VARCHAR(50) UNIQUE NOT NULL
            );
        """)

        # Create the threads table
        cursor.execute("""
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
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comments (
                comment_id INT AUTO_INCREMENT PRIMARY KEY,
                content TEXT NOT NULL,
                user_id INT,
                thread_id INT,
                category_id INT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (thread_id) REFERENCES threads(thread_id)
            );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
        category_id INT AUTO_INCREMENT PRIMARY KEY,
        category_name VARCHAR(50) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    CREATE TABLE IF NOT EXISTS thread_categories (
        thread_category_id INT AUTO_INCREMENT PRIMARY KEY,
        thread_id INT,
        category_id INT,
        FOREIGN KEY (thread_id) REFERENCES threads(thread_id),
        FOREIGN KEY (category_id) REFERENCES categories(category_id)
    );
        """)

        conn.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def addUser(username, password, email):
    conn=connect_to_database()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        values = (username, password, email)
        cursor.execute(query, values)
        conn.commit()
        # Get the user_id of the newly added user
        user_id = cursor.lastrowid
        cursor.close()
        return user_id 
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except:
        print("Sorry we can not register you now try again later")

# Similar functions for addThread, addComment, getUser, getThread, getComment, getThreads, getComments

def addThread(title, content,category, user_id):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO threads (title, content, user_id) VALUES (%s, %s, %s)"
        values = (title, content, user_id)
        cursor.execute(query, values)
        conn.commit()
        thread_id = cursor.lastrowid
        cursor.close()
        return thread_id
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

def addThreadCategory(thread_id, category_id):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO thread_categories (thread_id, category_id) VALUES (%s, %s)"
        values = (thread_id, category_id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")        
      
        
def removeThread(thread_id):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = "DELETE FROM threads WHERE thread_id = %s"
        cursor.execute(query, (thread_id,))
        conn.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

def removeComment(comment_id):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = "DELETE FROM comments WHERE comment_id = %s"
        cursor.execute(query, (comment_id,))
        conn.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def addComment(theard_id, content, user_id):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO comments (theard_id, content, user_id) VALUES (%s, %s, %s)"
        values = (theard_id, content, user_id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

def getThreadsInCategory(category_name):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = """
            SELECT t.thread_id, t.title, t.content, t.created_at, u.username
            FROM threads t
            JOIN users u ON t.user_id = u.user_id
            JOIN categories c ON t.category_id = c.category_id
            WHERE c.category_name = %s
        """
        cursor.execute(query, (category_name,))
        
        threads = cursor.fetchall()
        cursor.close()
        
        return threads
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None  # Return None to indicate an error

def get_all_categories():
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT category_name FROM categories")
        categories = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return categories
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    

def getUser(username, password):
    conn = connect_to_database()
    print(username, password)
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        cursor.close()
        return user
    except mysql.connector.Error as err:
        print(f"Error in getUser: {err}")
        return None

    
if __name__ == "__main__":
    conn = connect_to_database()
    if conn:
        create_tables(conn)
        # You can call your database functions here
        close_connection(conn)
