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
        self.cnx = sqlite3.connect('database.db',
            isolation_level=None) # autocommit
        self.cnx.cursor().execute("PRAGMA foreign_keys = 1") # Włączenie sprawdzania kluczy obcych
        #cursor().execute('')
    
    def getInstance(self):
        return self.cnx.cursor()
        
    def __del__(self):
        self.cnx.close()
        
# Example

def create_db():
    cursor = Connection().getInstance()
        
    querries = [
        """DROP TABLE IF EXISTS `users_currency`;""",
        """DROP TABLE IF EXISTS `users_attribute`;""",
        """DROP TABLE IF EXISTS `users_items`;""",
        """DROP TABLE IF EXISTS `users`;""",
        
        """
        CREATE TABLE `users` (
            `users_id`          INTEGER PRIMARY KEY AUTOINCREMENT,
            `username`          VARCHAR(32) NOT NULL UNIQUE,
            `password`          VARCHAR(60) NOT NULL,
            `email`             VARCHAR(255) NOT NULL UNIQUE
        );
        """,
        """
        CREATE TABLE `users_currency` (
            `users_currency_id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `users_id`          INTEGER NOT NULL UNIQUE,
            `gold`              VARCHAR DEFAULT 0 NOT NULL,
            `might`             VARCHAR DEFAULT 1 NOT NULL,
            `cunning`           VARCHAR DEFAULT 1 NOT NULL,
            `psyche`            VARCHAR DEFAULT 1 NOT NULL,
            `lore`              VARCHAR DEFAULT 1 NOT NULL,
            `treasures`         VARCHAR DEFAULT 1 NOT NULL,
            `riches`            VARCHAR DEFAULT 1 NOT NULL,
            FOREIGN KEY(`users_id`) REFERENCES users(`users_id`)
        );
        """,
        """
        CREATE TABLE `users_attribute` (
            `users_attribute_id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `users_id`          INTEGER NOT NULL UNIQUE,
            `stamina`           VARCHAR DEFAULT 1 NOT NULL,
            `health`            VARCHAR DEFAULT 1 NOT NULL,
            `ploy`              VARCHAR DEFAULT 1 NOT NULL,
            `spirit`            VARCHAR DEFAULT 1 NOT NULL,
            `clarity`           VARCHAR DEFAULT 1 NOT NULL,
            FOREIGN KEY(`users_id`) REFERENCES users(`users_id`)
        );
        """,
        """
        CREATE TABLE `users_item` (
            `users_item`        INTEGER PRIMARY KEY AUTOINCREMENT,
            `users_id`          INTEGER NOT NULL UNIQUE,
            `item_id`           INTEGER NOT NULL,
            FOREIGN KEY(`users_id`) REFERENCES users(`users_id`)
        );
        """
    ]
    
    i = 0
    for querry in querries:
        try:
            cursor.execute(querry)
        except Exception as e:
            print (i, "failed.")
            print(querry)
            raise e
        
        
        print (i, "success.");
        i = i + 1
    
def insert_example_data():
    cursor = Connection().getInstance()

    querry = "INSERT INTO `users` (`username`, `password`, `email`) VALUES (?, ?, ?)";
    values = ("User_123", "Password_123", "Email_123")
    cursor.execute(querry, values);
    
    querry = "INSERT INTO `users_currency` (`users_id`) VALUES (1)";
    cursor.execute(querry);
    
    querry = "INSERT INTO `users_attribute` (`users_id`) VALUES (1)";
    cursor.execute(querry);
    

if __name__ == "__main__":
    
    create_db()
    insert_example_data()
    cursor = Connection().getInstance()
    

    querry = "SELECT * FROM `users`";
    cursor.execute(querry)
    for row in cursor:
        print (row)
        
    querry = "SELECT * FROM `users_currency`";
    cursor.execute(querry)
    for row in cursor:
        print (row)

    querry = "SELECT * FROM `users_attribute`";
    cursor.execute(querry)
    for row in cursor:
        print (row)











