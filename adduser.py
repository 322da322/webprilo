import sqlite3

class DB():
    def __init__(self):
        pass

        

    
    def add_user(self, id: int, username: str, password: str):
        self.id = id
        self.username = username
        self.password = password
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        cursor.execute(f"""INSERT INTO User (id, username, password) VALUES (?, ?, ?)""", (self.id, self.username, self.password)
        )
        connection.commit()
        connection.close()

#db = DB(id= 1, username= "qwe", password= "123")

#db.add_user()