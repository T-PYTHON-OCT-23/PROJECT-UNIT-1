class Padel_Court:
    def __init__(self,city:str,name:str,court_number:int,women:bool,rate:float) :

        self.city = city
        self.name = name
        self.court_number = court_number
        self.women = women
        self.rate = rate
        
    
    def court_info (self):
        '''information about a Padel court,including its city, name, the number of courts available,whether it offers facilities for women, and its rating.'''

        print("City :" , self.city)
        print("Court Name :" ,self.name)
        print("Number of courts :" ,self.court_number)
        print("Court for womens :" , self.women)
        print("Court rating :" , self.rate)

    def search(court_data, city: str) -> list:
        '''Search for Padel courts in the given city within the provided court data.'''
     
        matching_court = []
        for court in court_data[city]:
            if city.lower() == court.city.lower():
                matching_court.append(court)

        if not matching_court:
            print("No matching courts found")
        
        return matching_court










      
       


