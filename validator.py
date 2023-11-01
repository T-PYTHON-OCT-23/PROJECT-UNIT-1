def checkstring(value):  # يتحقق من الاسم
    
    restrict='1234567890!@#$%^&*()-_+=} {:][|\"\'\\|/?.><,'
    for i in value:
        flag=True
        if i in restrict:
            print('Invalid character used in name.')  #حرف غير صالح مستخدم في الاسم
            flag=False
            break
    return flag
        
def checkpass(value): # يتحقق من الباسورد
    restrict='-][,\)('
    for i in value:
        flag=True
        if i in restrict:
            print('Invalid character used in name.')
            flag=False
            break
    return flag

def entry(title,Valuetype,ttype,size):
    if Valuetype=='char':
        value=input(title+' : ').strip()
        if len(value)<3 or len(value)>size:
            print('Invalid size, '+title+' must be 3 to '+str(size))
            return None
        elif checkstring(value):
            return value.capitalize()
        else:
            return None
    elif Valuetype=='string':
        value=input(title+' : ').strip()
        if len(value)<4 or len(value)>size:
            print('Invalid size, '+title+' must be 4 to '+str(size))
            return None
        else:
            return value.title().replace(' ','_')
    elif Valuetype=='email':
        value=input(title+' : ').strip()
        if len(value)<10 or len(value)>size:
            print('Invalid size, '+title+' must be 10 to '+str(size))
            return None
        elif '@' not in value:
            print('Invalid '+title+' \'@\' missing.')
            return None
        else:
            if value[value.find('@'):].count('.')==1:
                if len(value[value.find('@'):][value[value.find('@'):].find('.'):]) >=3:
                    return value.lower()
            else:
                print('Invalid Domain.')
                return None
    elif Valuetype=='int' and ttype=='user':
        value=int(input(title+' : '))
        if len(str(value))==10:
            return value
            del title,vtype,ttype,size
        else:
            print('Invalid contact no.')
            return None
    elif Valuetype=='int' and ttype=='book':
        if size==2:
            value=int(input(title+' : '))
            if value>0 and value<100:
                return value
            else:
                print('Book limit exceed.')
                return None
        else:
            value=int(input(title+' : '))
            if len(str(value))>=9 and len(str(value))<=size:
                return value
            else:
                print('ISBN error.')
                return None
    elif Valuetype=='select' and ttype=='user':
        print('1 Student\n2 Staff')
        choice=input('Enter a choice : ')
        if choice=='1':
            return 'Student'
        elif choice=='2':
            return 'Staff'
        else:
            return None
    elif Valuetype=='select' and ttype=='book':
        print('1 Reserved\n2 Non Reserved')
        choice=input('Enter a choice : ')
        if choice=='1':
            return 'rserv'
        elif choice=='2':
            return 'nores'
        else:
            return None
    else:
        #عملية غير صالحة. يرجى إعادة التشغيل
        print('Invalid operation. Please restart ')