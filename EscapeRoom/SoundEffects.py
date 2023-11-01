from playsound import playsound

#Play the sound when you solve all the clues
def play_yay_sound():
    try:
        file = "Sounds/yay_sound.mp3"
        return playsound(file)
    except Exception as e:
        print(e)
    

#Play the sound when user answer correct 
def play_correct_answer_sound():

    try:
        file = "Sounds/correct_answer.wav"
        return playsound(file)
    except Exception as e:
        print(e)
    
#Play the sound when user answer incorrect 
def play_incorrect_answer_sound():
    try:
        file = "Sounds/incorrect_answer.wav"
        return playsound(file)
    except Exception as e:
        print(e)
    
