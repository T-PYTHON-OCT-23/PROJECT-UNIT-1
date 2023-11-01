from db import addThread  , addThreadCategory , addCategory , get_all_categories
from mongo import removeThread , addToMongo , CreateCategories , getAllCategories , addToCommentsMongo , removeCommentMongo
class Thread:
    def __init__(self, title, content,category, author):
        """
        Initialize a Thread object.

        :param title: The title of the thread.
        :param content: The content of the thread.
        :param author: The user who created the thread.
        """
        self.title = title
        self.content = content
        self.author = author
        self.comments = []
        self.category = category
        self.ThreadId=addThread(title,category,author)
        addThreadCategory(category, self.ThreadId)
        category = catgory(category)
        category.add_thread(self)
        addToMongo(self.ThreadId, title, content,category, author)


    def add_comment(self,ThreadId,Category, content, author):
        """
        Add a new comment to the thread.

        :param content: The content of the comment.
        :param author: The user who created the comment.
        :return: The created Comment object.
        """
        comment = Comment(ThreadId,Category,content, author)
        self.comments.append(comment)
        addToCommentsMongo(ThreadId,content,Category,author)
        return comment
    
    def remove_comment(self, ThreadId,content,Category,author,comment, user_id=0):
        if user_id != 0 and not self.moderator:
            raise Exception("You are not a moderator and cannot remove comments")

        if self.moderator or user_id == comment.author.user_id:
            if comment in self.comments:
                self.comments.remove(comment)
                removeCommentMongo(ThreadId,content,Category,author)  # You should implement this function to remove the comment from the database
            else:
                raise Exception("Comment not found in the user's list of comments")
        else:
            raise Exception("You do not have permission to remove this comment")


class Comment:
    def __init__(self, ThreadId , Category ,  content, author):
        """
        Initialize a Comment object.

        :param content: The content of the comment.
        :param author: The user who created the comment.
        """
        self.content = content
        self.author = author
        self.ThreadId=ThreadId
        self.Category=Category
        

class catgory: 
    def __init__(self, name):
        self.name = name
        self.threads = []
        self.__categoryId = addCategory(name)

    def add_thread(self, thread):
        self.threads.append(thread)
        
    def remove_thread(self, thread):
        self.threads.remove(thread)
        removeThread(thread.thread_id)
        
    def get_category_id(self):
         return self.__categoryId
    def get_threads(self):
        return self.threads
    def get_name(self):
        return self.name
def Initialize():
    list_of_categories = ["Stack Overflow", "GitHub Community", "Reddit Tech Subreddits", "TechCrunch Community"] # List of categories
    allMongos=getAllCategories()  
    try:
        for i in list_of_categories:
            if i not in get_all_categories():
                catgory(i)
            if i not in allMongos:
                CreateCategories(i)
    except:
        for i in list_of_categories:
            catgory(i)    

    
Initialize()