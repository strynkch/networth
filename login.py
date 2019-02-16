import sqlite3, time, sys
import networthORIG2

def login():
    while True:
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
        with sqlite3.connect('username2.db') as db:
            cursor = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ? AND password = ?')
        cursor.execute(find_user, [(username),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print('Welcome ' + i[2])
            return('exit')


        else:
            print('Username and Password not recognized')
            again = input('Do you want to try again?(y/n): ')
            if again.lower() == 'n':
                print('Goodbye')
                exit()
            if again.lower() == 'y':
                login()
                exit()


def newuser():
    found = 0
    while found ==0:
        username = input('Enter a username: ')
        with sqlite3.connect('username2.db') as db:
            cursor = db.cursor()
        finduser = ('SELECT * FROM user WHERE username = ?')
        cursor.execute(finduser,[(username)])

        if cursor.fetchall():
            print('Username take, Please try again.')
        else:
            found = 1

    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')
    password = input('Enter in a password: ')
    password1 = input('Re-enter your password: ')
    while password != password1:
        print('Passwords did not match, Please try again.')
        password = input('Enter in a password: ')
        password1 = input('Re-enter your password: ')
    insertdata = '''INSERT INTO user(username,firstname,lastname,password)
    VALUES(?,?,?,?)'''
    cursor.execute(insertdata,[(username),(firstname),(lastname),(password)])
    db.commit()




def menu():
    while True:
        print('Welcome.')
        menu =('''
        1 - Create New User
        2 - Login
        3 - Net Worth
        4 - Exit\n''')

        userchoice = input(menu)

        if userchoice == '1':
            newuser()
        elif userchoice == '2':
            login()
        elif userchoice == '3':
            networthORIG2.ass_lib()
        elif userchoice == '4':
            print('Goodbye!')
            sys.exit()


menu()