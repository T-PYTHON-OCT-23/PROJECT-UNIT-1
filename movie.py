class Movie:
    def __init__(self,name_movie,price,hall,type,time,story):
        self.name_movie=name_movie
        self.price=price
        self.hall=hall
        self.type=type
        self.time=time
        self.story=story

    #def Adults(self):
        #return("Adult movies:")
    
   # def kids(self):
        #return("kids movies:")

movies=[ Movie("Bouchers Crossing",60,1,"adventure" ,"8:30 PM","A university explorer joins a team of hunters on a journey that puts his life and mind in danger."),
        Movie("killers of the flower moon",60,3,"drama crime" ,"12:45 AM","Set in the 1920s, the film depicts the serial killings of members of the Osage nation, a series of brutal crimes."),
        Movie("headspace",40, 4, "Action","1:30 AM","After chasing the evil Zolhardt through a wormhole, three aliens find themselves trapped in 16-year-old Norman's brain."),
        Movie("The inspripples",40, 2, "Animation" ,"10:20 PM","The adventures of two unlikely friends, an abandoned stuffed animal and a toy animal, as they meet to begin an exciting adventure."),
        Movie("deep fair",60,4,"horror suspense","2:00 AM ","Nomi met his fiancée on the Caribbean islands to help a sinking ship. Events take a sinister turn when the survivors turn out to be drug dealers."),
        Movie("corner office",60,5,"comedy","11:00 PM","Orson finds himself trapped in the company and has difficulty communicating with his mysterious colleague and his colleagues."),
]

def display_movies():
    for i, movie in enumerate(movies):
        print(f"{i + 1}. {movie.name_movie} - Movie price: {movie.price}$ - {movie.time} - Hall: {movie.hall} - {movie.type}  ")

def display_story_movie():
    pass