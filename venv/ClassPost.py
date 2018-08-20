from  ClassComments import Comments
class Post (Comments):

    __id = 0
    __idUser = 0
    __title = ''
    __description = ''
    
    def createPost(self, postDictyonary, userDictyonary):
        notExistUsers = False
        idUserNotNumber = False
        idPostNotNumber = False
        
        if not userDictyonary:
            print('There are no registered users')
            notExistUsers = True
        else:
            while (not idUserNotNumber):
                try:
                    self.__idUser = int(input('Write the id of the user'))
                    idUserNotNumber = True
                except ValueError:
                    print('Please enter a numeric value')

            for user in userDictyonary: 
                if user == self.__idUser:

                    while (not idPostNotNumber):
                        try:
                            self.__id = int(input('Write the id of the post'))
                            idPostNotNumber = True
                        except ValueError:
                            print('Please enter a numeric value')

                    if not postDictyonary:
                        self.__title = input('Write a title for this post')
                        self.__description = input('Write a description for this post')
                    else:
                        for post in postDictyonary:
                           while post == self.__id:
                               idPostNotNumber = False
                               while (not idPostNotNumber):
                                   try:
                                       self.__id = int(input('Write the id of the post'))
                                       idPostNotNumber = True
                                   except ValueError:
                                       print('Please enter a numeric value')

                        self.__title = input('Write a title for this post')
                        self.__description = input('Write a description for this post')

                    
        if not notExistUsers:
            postDictyonary[self.__id]= {'idUser':self.__idUser, 'title':self.__title, 'description':self.__description}
        else:
            print('Unregistred user')
            
        return  postDictyonary          


    def showPostByUser(self,postDictyonary,userDictyonary):

        notNumbrer = False

        if not postDictyonary:
            print('No posts to show')
        else:
            while not notNumbrer:
                try:
                    self.__idUser = int(input('Write the user ID: '))
                    notNumbrer = True
                except ValueError:
                    print('Please enter a numeric value')

            for post in postDictyonary:
                if self.__idUser == postDictyonary[post]['idUser']:
                    print("""
                    Name user: {}.
                    Title of the post: {}.
                    Description: {}.                    
                    """.format(userDictyonary[self.__idUser][0],postDictyonary[post]['title'],
                               postDictyonary[post]['description']))