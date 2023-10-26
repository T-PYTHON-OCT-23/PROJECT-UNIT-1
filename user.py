class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.threads = []

    def create_thread(self, title, content):
        thread = thread(title, content, self)
        self.threads.append(thread)
        return thread

class thread:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.comments = []

    def add_comment(self, content, author):
        comment = Comment(content, author)
        self.comments.append(comment)
        return comment

class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author


