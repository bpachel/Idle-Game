# pip install mysql-connector-python
import sqlite3

class ConnectionMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Connection(metaclass=ConnectionMeta):
    cnx = None
    def __init__(self):
        self.cnx = sqlite3.connect('database.db', isolation_level=None)
        self.cnx.cursor().execute('')
    
    def getInstance(self):
        return self.cnx.cursor()
        
    def __del__(self):
        self.cnx.close()
        
# Example

def create_db():
    cursor = Connection().getInstance()
    
    querry = "DROP TABLE IF EXISTS `users`;";
    cursor.execute(querry);
    
    querry = """
    CREATE TABLE `users` (
        `users_id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `username` varchar(32) NOT NULL UNIQUE,
        `password` varchar(60) NOT NULL,
        `email` varchar(255) NOT NULL UNIQUE
    );
    """
    cursor.execute(querry);
    
    
if __name__ == "__main__":
    
    #create_db()
    cursor = Connection().getInstance()
    
    """
    querry = "INSERT INTO `users` (`username`, `password`, `email`) VALUES (?, ?, ?)";
    values = ("User_123", "Password_123", "Email_123")
    cursor.execute(querry, values);
    """
    querry = "SELECT * FROM `users`";
    cursor.execute(querry);
    
    for row in cursor:
        print (row)












