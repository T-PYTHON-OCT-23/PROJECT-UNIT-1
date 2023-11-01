from playsound import playsound


def play_yay_sound():
    try:
        file = "Sounds/yay_sound.mp3"
        return playsound(file)
    except Exception as e:
        print(e)



play_yay_sound()