from db import addUser , removeThread , getUser , getPrevelage
from post import Thread

class User:
    def __init__(self, username, password, email):
        """
        Initialize a User object.

        :param username: The username of the user.
        :param email: The email of the user.
        """
        self.username = username
        self.email = email
        self.threads = []
        self.__userId = addUser(username, password, email)
        modreator = getPrevelage(self.__userId)
        
        
        
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
