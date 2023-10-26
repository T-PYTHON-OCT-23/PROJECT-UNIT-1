class Error:
    def __init__(self,error:str) -> None:
        self.error = error
    
    def check_valid_number(self,error):
        if error < 0:
            print("please enter a positive number")