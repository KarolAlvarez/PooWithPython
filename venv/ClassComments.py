class Comments:

    __id = 0
    __idPost = 0
    __comment = ''

    def createComment(self, commentDictyonary, postDictyonary):
        notExistPosts = False
        idPostNotNumber = False
        idCommentNotNumber = False
        
        if not postDictyonary:
            print('There is no post to comment')
            notExistPosts = True
        else:
            while (not idPostNotNumber):
                try:
                    self.__idPost = int(input('Write the id of the post'))
                    idPostNotNumber = True
                except ValueError:
                    print('Please enter a numeric value')

            for post in postDictyonary:
                if post == self.__idPost:
                    
                    while(not idCommentNotNumber):
                        try:
                            self.__id = int(input('Write the id of the comment'))
                            idCommentNotNumber = True
                        except ValueError:
                            print('Please enter a numeric value')
                    
                    if not commentDictyonary:
                        self.__comment = input('Write a comment')
                    else:
                        for com in commentDictyonary:
                            while com == self.__id:
                                
                                idCommentNotNumber = False
                                while (not  idCommentNotNumber):
                                    try:
                                        self.__id = int(input('This comment already exists, write another ID'))
                                        idCommentNotNumber = True
                                    except ValueError:
                                        print('Please enter a numeric value')
                                
                        self.__comment = input('Write a comment')
                    
        if not notExistPosts:
            commentDictyonary[self.__id] = {'idPost':self.__idPost,'comment':self.__comment}
        else:
            print('Unregistred post')

        return commentDictyonary


    def showCommentsByPost(self,commentDictyonary, postDictyonary):
        notNumbrer = False
        if not commentDictyonary:
            print('There are no comments to show')
        else:
            while not notNumbrer:
                try:
                    self.__idPost = int(input('Write the post ID: '))
                    notNumbrer = True
                except ValueError:
                    print('Please enter a numeric value')

            for comment in commentDictyonary:

                if self.__idPost == commentDictyonary[comment]['idPost']:
                    print("""
                    Post: {}.
                    Comment: {}                    
                    """.format(postDictyonary[self.__idPost]['title'], commentDictyonary[comment]['comment']))


