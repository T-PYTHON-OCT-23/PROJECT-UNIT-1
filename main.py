from stringcolor import * 
import config as cf
import sys
import manage_user as mu
import manage_book as mb
import manage_account as ma
import library
from stringcolor import * 

lub=library.Library_Management_System.Book()
cf.makedir()
def onStart():
    '''
    str1 = 'Library Management System'
    upper = lambda string: string.upper()
    print(upper(str1))'''

    print(bold('   Library Management System   ').underline().cs("Aqua","Chartreuse"))
    print('-------------------------------')
    print(cs('[ 1 ]  Login\n[ 2 ]  Register\n[ 0 ]  Exit', "Aqua").bold())  
    choice=input('_______________________________\nEnter a choice : ')
    if choice=='0':
        cf.cls()
        sys.exit(print(cs('--Program terminated Successfully--', "Teal")))
    elif choice=='1':
        login()                         
    elif choice=='2':
        cf.cls()
        mu.register_lib()
    else:
        onStart()
    onStart()

def login():
    cf.cls()
    print('============ Login ============')
    username = input('Username : ')
    password = input('Password : ')
    if library.Library_Management_System().Login(username,password):
        cf.cls()
        print('----------------------------------')
        print(cs('   Login successful  ', "DeepPink6"))
        print('-----------------------------------')
        onCreate()
    else:
        cf.cls()
        print(cs('Incorrect username or password.\nWould you like to register ? [Y/N]\n', "Wheat"))
        ans = input('[Y/N]')
        if ans=='Y' or ans=='y':
            cf.cls()
            mu.register_lib()
        elif ans=='N' or ans=='n':
            cf.cls()
            login()
        else:
            print(cs('Incorrect Option Selected', "Khaki"))
            onStart()

def onCreate(): 
    print('==================================')
    print(bold('   Library Management System   ').underline().cs("Wheat","DeepPink4"))
    print('----------------------------------')
    print(cs('[ 1 ] >> Book Request\n[ 2 ] >> Return Book\n[ 3 ] >> Book Accounts\n[ 4 ] >> User (Add/Edit)\n[ 5 ] >> Book (Add/Edit)\n[ L ] >> Logout\n[ 0 ] >> Exit',"Wheat").bold())
    choice=input('_______________________________\nEnter a choice : ')
    cf.cls()
    if choice=='0':
       sys.exit(print(cs('--Program terminated Successfully--', "Teal")))
    elif choice=='1':
        cf.cls()
        mb.issue()
    elif choice=='2':
        con=mu.getcontact()
        cf.cls()
        lub.Return_book(con)
    elif choice=='3':
        bookaccount()
    elif choice=='4':
        cf.cls()
        manage_user()
    elif choice=='5':
        manage_book()
    elif choice=='L' or choice=='l':
        onStart()
    else:
        cf.cls()
    onCreate()

def manage_user():
    print(bold('    ** MANAGE USERS **    ').underline().cs("White","LightPink"))
    print('==================================')
    print(cs('[ 1 ] >> Add\n[ 2 ] >> Update\n[ 3 ] >> Search\n[ 4 ] >> Display\n[ 5 ] >> Delete\n[ b ] >> Back',"Thistle").bold())
    choice=input('_______________________________\nEnter a choice : ')
    if choice=='0':
       sys.exit(print(cs('--Program terminated Successfully--', "Teal")))
    elif choice=='1':
        if mu.add():
            cf.cls()
            print(cs(' * User added successfully *  ', "Grey7"))
            print('-------------------------------')
        else:
            cf.cls()
            print(cs(' * User added successfully *  ', "White"))
            print('-------------------------------')
    elif choice=='2':
        cf.cls()
        mu.update()
    elif choice=='3':
        cf.cls()
        mu.search()
    elif choice=='4':
        cf.cls()
        mu.display()
    elif choice=='5':
        cf.cls()
        mu.delete()
    elif choice=='b' or choice=='B':
        cf.cls()
        return 0
    else:
        cf.cls()
    manage_user()

def manage_book():
    print(bold('    ** MANAGE BOOKS **      ').underline().cs("Black","LightSkyBlue"))
    print('===============================')
    print(cs('[ 1 ] >> Add\n[ 2 ] >> Update\n[ 3 ] >> Search\n[ 4 ] >> Display\n[ 5 ] >> Delete\n[ b ] >> Back',"Aqua").bold())
    choice=input('_______________________________\nEnter a choice : ')
    if choice=='0':
        sys.exit(print(cs('--Program terminated Successfully--', "Teal")))
    elif choice=='1':
        if mb.add():
            cf.cls()
            print(cs(' * Book added successfully *  ', "Grey7"))
            print('-------------------------------')
        else:
            cf.cls()
            print(cs(' * Book already exists *   ', "White"))
            print('-------------------------------')
    elif choice=='2':
        cf.cls()
        mb.update()
    elif choice=='3':
        cf.cls()
        mb.search()
    elif choice=='4':
        cf.cls()
        mb.display()
    elif choice=='5':
        cf.cls()
        mb.delete()
    elif choice=='b' or choice=='B':
        cf.cls()
        return 0
    else:
        cf.cls()
    manage_book()

def bookaccount():
    print('\n===============================')
    print(bold('    ** BOOK ACCOUNTS **      ').underline().cs("White","Orange"))
    print('-------------------------------')
    print(cs('[ 1 ] >> Reserved Book\n[ 2 ] >> Borrow List\n[ 3 ] >> Returned List\n[ b ] >> Back\n[ 0 ] >> Exit',"LightGoldenrod2").bold())
    choice=input('_______________________________\nEnter a choice : ')
    if choice=='0':
        sys.exit(print(cs('--Program terminated Successfully--', "Teal")))
    elif choice=='1':
        ma.display_res()
    elif choice=='2':
        ma.display_bor()
    elif choice=='3':
       ma.display_ret() 
    elif choice=='b' or choice=='B':
        cf.cls()
        return 0
    else:
        bookaccount()
    

onStart()