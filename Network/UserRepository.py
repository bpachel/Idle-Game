from AbstractRepository import AbstractRepository

class User:
    def __init__(self):
        self.id = ""
        self.username = ""
        self.password = ""
        self.email = ""

class UserRepository(AbstractRepository):

    def __create_array_from_result(self, results):
        users = []

        for result in results:
            user = User()
            user.id         = result[0]
            user.username   = result[1]
            user.password   = result[2]
            user.email      = result[3]

            users.append(user)

        return users
        
    def __init__(self, reset=False):
        self.name = "user"
        self.delete_querry = """DROP TABLE IF EXISTS `user`;"""
        self.create_querry = """
        CREATE TABLE `user` (
            `id`                INTEGER PRIMARY KEY AUTOINCREMENT,
            `username`          VARCHAR(32) NOT NULL UNIQUE,
            `password`          VARCHAR(60) NOT NULL,
            `email`             VARCHAR(255) NOT NULL UNIQUE
        );
        """
        super().__init__(reset)

    def findAll(self):
        results = self._findAll()
        return self.__create_array_from_result(results)

    def findBy(self, arr):
        results = self._findBy(arr)
        return self.__create_array_from_result(results)

    def findOneBy(self, arr):
        result = self.findBy(arr)
        if len(result) > 0:
            return result[0]
        return None

    def add(self, object):
        if object.__class__.__name__ == "User":
            self._add(object)
        else:
            raise TypeError

if __name__ == "__main__":
    
    userRepository = UserRepository()

    user = User()
    user.username = "abcdef"
    user.password = "gggggg"
    user.email = "gggggg"

    userRepository.add(user)
    
    for user in userRepository.findAll():
        print (user.id, user.username, user.password, user.email)

    user = userRepository.findOneBy({"id" : 4})
    print (user.id, user.username, user.password, user.email)
    #print ( list(user.__dict__.keys() ))