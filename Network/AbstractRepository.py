
from database import Connection

class AbstractRepository:
    def __init__(self, reset):
        self.cursor = Connection().getInstance()
        if reset:
            try:
                self.cursor.execute(self.delete_querry)
            except Exception as e:
                print(self.delete_querry)
                print("Drop failed.")
                print(e)
                raise e

            try:
                self.cursor.execute(self.create_querry)
            except Exception as e:
                print(self.create_querry)
                print("Create failed.")
                print(e)
                raise e

    def _findAll(self):
        
        self.get_all_querry = """
            SELECT * FROM {};
        """.format(self.name)


        try:
            self.cursor.execute(self.get_all_querry)
        except Exception as e:
            print(self.get_all_querry)
            print ("failed.")
            print(e)
            return None
        
        result = self.cursor.fetchall()
        return result

    def _findBy(self, arr):
        if arr == {}:
            return self.getAll()

        keys = list(arr.keys())

        self.querry = """
            SELECT * FROM {}
            WHERE `{}` = "{}"
        """.format(self.name, keys[0], arr[keys[0]])

        for i in range(1, len(arr) ):
            self.querry = (self.querry  + " AND {} = {}" ).format(keys[i], arr[keys[i]])
        
        try:
            self.cursor.execute(self.querry)
        except Exception as e:
            print(self.querry)
            print ("failed.")
            print(e)
            return None
        
        result = self.cursor.fetchall()
        return result

    def _add(self, object):
        arr = object.__dict__
        keys = list(arr.keys())
        values = list(arr.values())

        new_keys = []
        new_values = []

        for i in range(len(arr)):
            if arr[keys[i]] not in ['', None]:
                new_keys.append(keys[i])
                new_values.append(arr[keys[i]])

        if arr['id'] == None:
            self.querry = "INSERT INTO `{}` (`{}`" + ((", `{}`")*(len(new_keys)-1)) + ")"
            self.querry = self.querry.format(self.name, *new_keys)

            self.querry = self.querry + " VALUES (\"{}\"" + ((", \"{}\"")*(len(new_keys)-1)) + ")"
            self.querry = self.querry.format(*new_values)
        else:
            values = []
            for k, v in arr.items():
                values.append(k)
                values.append(v)

            self.querry = "UPDATE {} SET ".format(self.name)
            self.querry = self.querry + ("`{}`={}" + ", `{}`={}"* (len(arr)-1)).format(*values)

            self.querry = self.querry + " WHERE id={}".format(arr['id'])

        try:
            print (self.querry)
            self.cursor.execute(self.querry)
        except Exception as e:
            print(self.querry)
            print ("failed.")
            print(e)
            return False

        query = "SELECT last_insert_rowid()"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        return result[0][0]

if __name__ == "__main__":
    ar = AbstractRepository()
    ar.name = "users"
    print ( ar.findBy( {"users_id" : "1"} ) )