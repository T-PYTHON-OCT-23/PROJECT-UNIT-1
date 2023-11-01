from open_ai import OpenAi
from files_operations import FilesOperations,Favorites


user_choice='''
Click the number of service:
1- to create file containing the ChatGPT output.
2- to add the containing to favorites.
3- to continue to ask ChatGPT.
4- to display files added.
5- to remove file
6- to display files added to favorites.
7- to retrieve file from favorite.
8- to delete file from favorite. 
9- to exit.
 
'''

print('''
welcome to Our ChatGPT program...
we provaide you this services using ChatGPT:''')

chat=[]


while True:
        ask=input("ask ChatGPT any thing you want or type exit to exit: ") 
        if ask == 'exit':
            break
        try:
            print(ask+"?") 
            chat_gpt=OpenAi(ask)
            chat_output=chat_gpt.ai_output()
            chat.append(chat_output)
            print(chat_output)
        except Exception:
               print("Check the internet connection status!!!")
    
show_favorites=Favorites()
while True:

        print(user_choice)
        service_number=input("Click number of service: ")

        if service_number == '9':
                break
        elif service_number == '1':
            user_entry=input("Enter file name with its extension to cancel inter no:")

            if user_entry=="no":
                        
                continue
            file_name=FilesOperations(user_entry)
            file_name.new_file(chat)
            print(f"{len(chat)} chating added")
            input("enter any key to continue")
                        
        elif service_number == '2':
                user_entry=input("Enter file name with its extension to cancel inter no:")
                if user_entry.lower()=='no':
                      continue
                favorites=Favorites(user_entry,chat)
                favorites.add_to_favorites()
                print(f"{len(chat)} chating added")
                input("enter any key to continue")
                
        elif service_number == '3':
                chat.clear()
                while True:
                    ask=input("ask ChatGPT any thing you want or type exit to exit: ") 
                    if ask == 'exit':
                        break
                    try:
                        print(ask+"?") 
                        chat_gpt=OpenAi(ask)
                        chat_output=chat_gpt.ai_output()
                        chat.append(chat_output)
                        print(chat_output)
                    except Exception:
                        print("Check the internet connection status!!!")
        elif service_number =='4':
                list_files=FilesOperations()
                print(list_files.show_file())
                input("enter any key to continue")

                
        elif service_number == '5':
                user_entry=input("Enter the correct file name with its extension,to cancel enter no:")
                if user_entry == "no":
                      continue
                try:
                    rm_file=FilesOperations()
                    rm_file.remove_file(user_entry)
                    print("Removal succeeded!!")
                    input("enter any key to continue")
                except FileNotFoundError:
                        print("Sory File Not Found!!!")
                        input("enter any key to continue")
                except PermissionError:
                      print("enter only file name or no to exit")
                      input("enter any key to continue")
        elif service_number =='6':
                   
            count=1
            for f_name in map(lambda file:file,show_favorites.take_favorites()):
                print(f"{count}-{f_name['file name']}")
                count+=1
            input("enter any key to continue")
        elif service_number =="7":
            file=input("Enter the correct file name with its extension: ")
            get_favorites=FilesOperations(file)

            for f_name in  map(lambda file:file,show_favorites.take_favorites()):
                if f_name['file name'] == file:
                                 
                    get_favorites.new_file(f_name['content'])           
                    input("done Enter any key")
                    break
            else:
                print("Sory File Not Found!!!")
                input("enter any key to continue")
        elif service_number =='8':
              
            delete_file = Favorites()
            delete_file.delete_favorite(input("Enter the correct file name with its extension:"))
            


                 

            


    

