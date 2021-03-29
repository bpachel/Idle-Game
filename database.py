# pip install mysql-connector-python
import mysql.connector

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
        self.cnx = mysql.connector.connect(
            user='sql11402333',
            password='REAQNqhjEa',
            host='sql11.freemysqlhosting.net',
            database='sql11402333',
            port=3306,
            autocommit=True
        )
    
    def getInstance(self):
        return self.cnx.cursor()
        
    def __del__(self):
        self.cnx.close()
        
# Example
if __name__ == "__main__":
    # The client code.

    cursor = Connection().getInstance()
    
    querry = "INSERT INTO `users` (`username`, `password`, `email`) VALUES (%s, %s, %s)";
    values = ("User_123", "Password_123", "Email_123")
    cursor.execute(querry, values);
    
    querry = "SELECT * FROM `users`";
    cursor.execute(querry);
    
    for row in cursor:
        print (row)
    












