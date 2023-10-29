from db import addUser , addComment , addThread , removeThread , removeComment , getUser
class User:
    def __init__(self, username, password,email):
        """
        Initialize a User object.

        :param username: The username of the user.
        :param email: The email of the user.
        """
        self.username = username
        self.email = email
        self.threads = []
        self.__userId = addUser(username, password, email)
        modreator = False
        
    def getUserId(self):
        return self.__userId
    def setId(self, id):
        self.__userId = id
    def login(username, password):
        """
        Login as a user.

        :param username: The username of the user.
        :param password: The password of the user.
        :return: The User object if login was successful, None otherwise.
        """
        # Get the user from the database
        user = getUser(username, password)
        if user:
            return user
        else:
            return None
    def remove_thread(self, thread, user_id=0):
        if user_id != 0 and not self.moderator:
            raise Exception("You are not a moderator and cannot remove threads")

        if self.moderator or user_id == thread.author.user_id:
            if thread in self.threads:
                self.threads.remove(thread)
                removeThread(thread.thread_id)
            else:
                raise Exception("Thread not found in the user's list of threads")
        else:
            raise Exception("You do not have permission to remove this thread")

            

    def create_thread(self, title, content):
        """
        Create a new thread associated with this user.

        :param title: The title of the thread.
        :param content: The content of the thread.
        :return: The created Thread object.
        """
        thread = Thread(title, content, self)
        self.threads.append(thread.ThreadId)
        return thread

class Thread:
    def __init__(self, title, content, author):
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
        self.ThreadId=addThread(title,content,author)


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
        
