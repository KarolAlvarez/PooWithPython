from ClassUser import User

userDictyonary ={}# {1:[10,'aleja',25]}
postDictyonary = {}#1:{'idUser':[1,'title','descri']}}
commentDictyonary = {}#{'id':{'idPost':[1,'comment']}}
mainDictyonary = {'Users':userDictyonary, 'Posts':postDictyonary, 'Comments':commentDictyonary}

def menu():
    print ("""
    ..............Menu Options................
    .                                        .
    . [1] User register                      .
    . [2] Show Users                         .
    . [3] Create post                        .
    . [4] Create comment                     .
    . [5] List post by user                  .
    . [6] Show the comments of post          .
    . [7] Exit                               .
    ..........................................
    """)
    optionSelected = int(input("Select an option: "))
    return optionSelected


user = User()

optionSelected = menu()


while optionSelected > 0 and optionSelected <= 7:

    if optionSelected == 1:
        userDictyonary = user.createUser(userDictyonary)
    elif optionSelected == 2:
        user.showAllUsers(userDictyonary)

    elif optionSelected == 3:
        postDictyonary = user.createPost(postDictyonary,userDictyonary)

    elif optionSelected == 4:
        commentDictyonary = user.createComment(commentDictyonary,postDictyonary)

    elif optionSelected == 5:
        user.showPostByUser(postDictyonary, userDictyonary)

    elif optionSelected == 6:
        user.showCommentsByPost(commentDictyonary, postDictyonary)

    elif optionSelected == 7:
        exit()

    optionSelected = menu()


print("Error this option does not exist")
for n in range(0,3,1):
    print( "Bye...")
print(' _____________ ')