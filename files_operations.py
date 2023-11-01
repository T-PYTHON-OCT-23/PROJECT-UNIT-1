import os
import json
from datetime import datetime
class FilesOperations:
    def __init__(self,file_name:str="empty_file.txt"):
        self.file_name = file_name
        

    def new_file(self,content : list):
        with open(f"added_files/{self.file_name}","a", encoding="utf-8") as file:
            for text in content:
                file.write(text)

    def show_file(self):
        list_file=os.listdir('added_files/')
        files="Your added files:\n"
        num =1
        for file in list_file:
            
            files+=f"{num}- {file}\n"
            num+=1
         
        return files
    
    def remove_file(self,file_name):
        os.remove('added_files/'+file_name)



class Favorites:
    
    def __init__(self,file_name : str="empty",content : str="empty"):

        self.content = content
        self.file_name = file_name
    
    def add_to_favorites(self):
           
       favorites =[]

       with open(f"added_files/favorites.json","r",encoding="utf-8") as file:
   
           content = file.read()
           favorites=json.loads(content) if  len(content) > 5 else []

       favorites.append({"file name":self.file_name,"content":self.content,"date":f"{str(datetime.now())}"})
       with open(f"added_files/favorites.json","w",encoding="utf-8") as file:
   
           data=json.dumps(favorites,indent=2)
           file.write(data)
    
    def take_favorites(self):
        
        with open("added_files/favorites.json") as file:
           content = file.read()
           favorites=json.loads(content) if  len(content) > 5 else []
        
        return favorites
    
    def delete_favorite(self,file_name):
        favorite_update=[]

        favorite=Favorites.take_favorites(self)
        is_found = False
        for file in favorite:
            if file["file name"] == file_name:
                is_found = True
            else :
                favorite_update.append(file)
                

        if not is_found: 
            print("file not found")
            input("Enter any key")
        
        if is_found:
            input("done Enter any key")
        

        with open(f"added_files/favorites.json","w",encoding="utf-8") as file:
   
           data=json.dumps(favorite_update,indent=2)
           file.write(data)
        
        







        
        



    
    

        


    
    
    
    


    




