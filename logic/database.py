import sqlite3

class Database:
    def __init__(self, db_name='handler/database.db'):
        self.db_name = db_name
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT UNIQUE,
                            password TEXT,
                            name TEXT)''')  
        self.conn.commit()

    def register_user(self, username, password, name=None):
        try:
            self.connect()
            self.cur.execute("INSERT INTO users (username, password, name) VALUES (?, ?, ?)", (username, password, name))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            self.close()

    def authenticate_user(self, username, password):
        try:
            self.connect()
            self.cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = self.cur.fetchone()
            return user is not None
        finally:
            self.close()

    def login_user(self, username, password):
        try:
            self.connect()
            self.cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = self.cur.fetchone()
            if user:
                return user
            else:
                return None
        finally:
            self.close()

    def get_users(self):
        try:
            self.connect()
            self.cur.execute("SELECT * FROM users")
            return self.cur.fetchall()
        finally:
            self.close()

    def close(self):
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    db = Database()
