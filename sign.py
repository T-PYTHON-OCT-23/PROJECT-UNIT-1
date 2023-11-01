from stringcolor import * 


sign_up = {"0507100798" : "albandari" ,
           "0555555555" : "fay" } 


def check_user( phone_num , name ):

     if len(phone_num) < 10 or len(phone_num) > 10 or not phone_num.isnumeric():
          raise Exception(cs("Please provide a valid number" , "red"))
     
     sign_up.update(phone_num = name)
     return  cs(f"Operation succesfully, Welcome {name}", "green")
