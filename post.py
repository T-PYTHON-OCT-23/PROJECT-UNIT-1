from db import addComment , addThread  , removeComment , addThreadCategory , addCategory
from mongo import removeThread , addToMongo
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
        category.add_thread(self)
        addToMongo(self.ThreadId, title, content,category, author)


    def add_comment(self,ThreadID, content, author):
        """
        Add a new comment to the thread.

        :param content: The content of the comment.
        :param author: The user who created the comment.
        :return: The created Comment object.
        """
        comment = Comment(content, author)
        self.comments.append(comment)
        addComment(ThreadID,content,author)
        return comment
    
    def remove_comment(self, comment, user_id=0):
        if user_id != 0 and not self.moderator:
            raise Exception("You are not a moderator and cannot remove comments")

        if self.moderator or user_id == comment.author.user_id:
            if comment in self.comments:
                self.comments.remove(comment)
                removeComment(comment.comment_id)  # You should implement this function to remove the comment from the database
            else:
                raise Exception("Comment not found in the user's list of comments")
        else:
            raise Exception("You do not have permission to remove this comment")


class Comment:
    def __init__(self, content, author):
        """
        Initialize a Comment object.

        :param content: The content of the comment.
        :param author: The user who created the comment.
        """
        self.content = content
        self.author = author
        

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