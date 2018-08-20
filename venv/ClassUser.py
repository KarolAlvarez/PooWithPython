from  ClassPost import Post
class User(Post):

    __id = 0
    __name = ''
    __lastName = ''
    __phone = ''
    __email = ''
    __age = 0


    def createUser(self, userDictyonary):
        idIsNumber = False
        ageIsNumber = False
        if not userDictyonary:
            while not idIsNumber:
                try:
                    self.__id = int(input('Write the id of the user'))
                    idIsNumber = True
                except ValueError:
                    print('Please enter a numeric value')
            self.__name = input('Write your name')
            self.__lastName = input('Write your last names')
            self.__phone = input('Write your phone')
            self.__email = input('Write your email')
            while not ageIsNumber:
                try:
                    self.__age = int(input('Write your age'))
                    ageIsNumber = True
                except ValueError:
                    print('Please enter a numeric value')
        else:
            while not idIsNumber:
                try:
                    self.__id = int(input('Write the id of the user'))
                    idIsNumber = True
                except ValueError:
                    print('Please enter a numeric value')
            for user in userDictyonary:
                while user == self.__id:
                    idIsNumber = False
                    print('The user already exist')
                    while not idIsNumber:
                        try:
                            self.__id = int(input('Write the id of the user'))
                            idIsNumber = True
                        except ValueError:
                            print('Please enter a numeric value')

            self.__name = input('Write your name')
            self.__lastName = input('Write your last names')
            self.__phone = input('Write your phone')
            self.__email = input('Write your email')
            ageIsNumber = False
            while not ageIsNumber:
                try:
                    self.__age = int(input('Write your age'))
                    ageIsNumber = True
                except ValueError:
                    print('Please enter a numeric value')       
        
        userDictyonary[self.__id] = [self.__name, self.__lastName, self.__phone, self.__email, self.__age] 
        return userDictyonary               


    def showAllUsers(self,userDictyonary):
        if not userDictyonary:
            print('there are no users to show')
        else:
            for user in userDictyonary:
                print("""
                Name: {}.
                Last names: {}.
                Age: {}.
                Email: {}.
                Phone: {}.""".format(userDictyonary[user][0],userDictyonary[user][1],
                           userDictyonary[user][4],userDictyonary[user][3],
                           userDictyonary[user][2]))