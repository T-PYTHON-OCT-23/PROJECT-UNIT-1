import playsound
#Note: If the sound is not working for you, this module can be used
#Play the sound when user answer correct 
def play_correct_answer_sound():
    try:
        file = "correct_answer.wav"
        return playsound(file)
    except Exception as e:
        print(e)
    
#Play the sound when user answer incorrect 
def play_incorrect_answer_sound():
    try:
        file = "incorrect_answer.wav"
        return playsound(file)
    except Exception as e:
        print(e)
    
    
#Play the sound when you solve all the clues
def play_yay_sound():
    try:
        file = "yay_sound.wav"
        return playsound(file)
    except Exception as e:
        print(e)
    
    

