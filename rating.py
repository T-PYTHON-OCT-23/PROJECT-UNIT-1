class Court_Rating:
    def __init__(self, rating=0, comments=[]):
        self.rating = rating
        self.comments = comments

    def add_rating(self, new_rating):
        '''This method allows you to add a new rating to the Court_Rating object'''
        # Check if there are existing ratings
        if not hasattr(self, 'ratings'):
            self.ratings = []
        
        # Add the new rating to the list of ratings
        self.ratings.append(new_rating)

    def add_comment(self, comment):
        '''This method allows you to add a comment to the Court_Rating object'''
        self.comments.append(comment)

