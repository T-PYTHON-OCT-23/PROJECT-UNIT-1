from db import addUser , addComment , addThread
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
        self.userId = addUser(username, password, email)
        

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

class Comment:
    def __init__(self, content, author):
        """
        Initialize a Comment object.

        :param content: The content of the comment.
        :param author: The user who created the comment.
        """
        self.content = content
        self.author = author
        
