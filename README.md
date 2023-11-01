# PROJECT-UNIT-1


### Padel court evaluation

The program focuses on providing a user to finding and rating padel courts in different cities. I have designed a program that allows users to explore padel courts, leave ratings, and comments

I use tow classes 
 1- Padel_Court class that contain the attribute of padels and mithods
    - firs method :court_info (information about a Padel court)
        This function prints details about a Padel court, including its city, name, the number of courts available,
        whether it offers facilities for women, and its rating.
    - scand method : search (Search for Padel courts in a specific city)
            This function searches for Padel courts in the given city within the provided court data.
            It returns a list of matching courts.
            If no matching courts are found, it raises an Exception.

2- Court_Rating class that contain the attribute of (raring , new rating and comment)  and mithods
    - firs method : add_rating
       This method allows you to add a new rating to the Court_Rating object
    - scand method : add_comment 
       This method allows you to add a comment to the Court_Rating object.

I use colorama and art modules to desgin ghe output

