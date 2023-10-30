# TECH FOURMS
## Tech Forums Project Readme

Welcome to the Tech Forums project! This project is designed to create an online platform where tech enthusiasts can discuss various topics related to technology, seek help, and share their knowledge. Here's an overview of the project and how to use it.

### Overview

Tech Forums is an online community for tech-savvy individuals. It allows two main types of users: regular users and moderators. Each user type has specific functionalities:

#### Regular Users
- Browse and search for tech-related topics.
- View detailed information about a topic, including the content, author, and post date.
- Create new topics to start discussions.
- Reply to existing topics with comments.
- Like and upvote topics and comments.
- Edit and delete their own topics and comments.
- Follow other users and receive notifications about their activity.
- Edit their profile information, including a profile picture and biography.

### Moderators
- All the functionalities of regular users.
- Ability to moderate content, including the ability to delete inappropriate topics and comments.
- Suspend or ban users who violate the community guidelines.
- Mark topics as "sticky" for important announcements.

### Usage

To make the most of Tech Forums, here's how to use the project:

1. **Registration and Authentication**:
   - Create a new account or log in if you already have one.
   - Verify your email address for account security.

2. **Browsing Topics**:
   - Explore the homepage to see the latest and trending topics.
   - Use the search bar to find specific topics or keywords.

3. **Viewing Topics**:
   - Click on a topic to view its details, including the content and comments.

4. **Engaging in Discussions**:
   - Reply to topics by adding your comments.
   - Like or upvote topics and comments that you find valuable.

5. **Creating New Topics**:
   - Start a new discussion by clicking the "New Topic" button.
   - Provide a title and detailed content for your topic.

6. **Managing Your Profile**:
   - Edit your profile information, including your profile picture and biography.
   - Follow other users to stay updated on their activity.

7. **Moderator Actions** (Moderators only):
   - Ensure the community guidelines are followed.
   - Delete inappropriate content.
   - Suspend or ban users who violate the guidelines.
   - Mark important announcements as "sticky."

### Support and Feedback

If you encounter any issues or have suggestions for improving Tech Forums, please reach out to our support team or use the "Feedback" section on the platform. We are continuously working to make this community a great place for tech discussions and learning.

Thank you for joining Tech Forums, and we hope you enjoy your experience in this tech-savvy community!

### About The Code 

### Function: `addThreadCategory(thread_id, category_id)`
- This function is used to add a thread to a category in a database.
- It takes two parameters: `thread_id` and `category_id`.
- It connects to the database, creates a cursor, and executes an SQL INSERT statement.
- If an error occurs, it catches the exception and prints an error message.

### Function: `removeThread(thread_id)`
- This function is used to remove a thread from the database by its `thread_id`.
- It takes one parameter: `thread_id`.
- It connects to the database, creates a cursor, and executes an SQL DELETE statement.
- If an error occurs, it catches the exception and prints an error message.

### Function: `removeComment(comment_id)`
- This function is used to remove a comment from the database by its `comment_id`.
- It takes one parameter: `comment_id`.
- It connects to the database, creates a cursor, and executes an SQL DELETE statement.
- If an error occurs, it catches the exception and prints an error message.

### Function: `addComment(thread_id, content, user_id)`
- This function is used to add a comment to a thread in the database.
- It takes three parameters: `thread_id`, `content`, and `user_id`.
- It connects to the database, creates a cursor, and executes an SQL INSERT statement.
- If an error occurs, it catches the exception and prints an error message.

## Class: `Mongo`
The `Mongo` class provides a set of methods for interacting with a MongoDB database. It is designed to handle operations related to threads and categories within the database.

### Constructor: `__init__(self, host, port, database)`
- The constructor initializes a connection to a MongoDB server and selects a specific database.
- It takes three parameters: `host`, `port`, and `database`.
- It establishes a connection to the MongoDB server using the provided host and port and selects the specified database for further operations.

### Method: `addToMongo(self, thread_id, title, content, category, author)`
- This method is used to add a thread document to a specific category within the MongoDB database.
- It takes five parameters: `thread_id`, `title`, `content`, `category`, and `author`.
- It creates a document with the provided data and inserts it into a MongoDB collection named after the specified category.

### Method: `getCategories(self, category)`
- This method creates collections within the MongoDB database based on a list of categories.
- It takes a single parameter: `category`, which is a list of category names.
- For each category in the list, a new collection is created within the database to organize threads.

### Method: `getThreads(self, category)`
- This method retrieves all threads from a specified category in the MongoDB database.
- It takes one parameter: `category`, which is the name of the category to retrieve threads from.
- It fetches all documents from the MongoDB collection associated with the specified category and returns them.

### Method: `getThreadsById(self, category, id)`
- This method retrieves a specific thread from a specified category in the MongoDB database by its `thread_id`.
- It takes two parameters: `category` and `id`.
- It searches the MongoDB collection associated with the specified category for documents with a matching `thread_id` and returns them.

### Method: `removeThread(self, category, id)`
- This method removes a specific thread from a specified category in the MongoDB database by its `thread_id`.
- It takes two parameters: `category` and `id`.
- It searches the MongoDB collection associated with the specified category for documents with a matching `thread_id` and deletes them.
