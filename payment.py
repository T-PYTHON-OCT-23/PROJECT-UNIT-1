class Payment:
    def __init__(self,email:str,is_payed:int) -> None:
        self.is_paid = is_payed
        self.email = email
    
    def is_it_payed(self,cost):
        self.is_paid -= cost
        print(self.is_paid)
        return True
