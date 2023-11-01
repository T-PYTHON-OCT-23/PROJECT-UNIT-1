push:str =[" Chest press " , " Incline dumbbell press " , " Shoulder press " , "literal rises ", "Triceps extention", "Triceps pushdown "  ]

pull:str = ["Pull ups " , " Barbell row " , "Single arm row " , "Biceps curls ", "Hummer curls"  ]

lower:str =["Squat" ,"Leg press " , " Hip thrust " , " RDL " , " Leg extention" ,"Deadleft" , "calf rises" ]

abs:str = ["Plank " , " Knee crunch " , " Leg rises " , " Shoulder taps " , "Bicycle Crunch" , "Heel reach" ]


def show_workout(workout_type:str):

    if workout_type == "push".lower():
         list_workout = print (f"\nThese are the workouts for push day \n {push}  ")
         return list_workout
    
    elif workout_type == "pull".lower():
         list_workout = print (f"\nThese are the workouts for pull day \n {pull}  ")
         return list_workout
         
    elif workout_type == "lower".lower():
         list_workout = print (f"\nThese are the workouts for lower body day \n {lower }  ")
         return list_workout

          
    elif workout_type == "abs".lower():
         list_workout = print (f"\nThese are the workouts for abs day \n {abs}  ")
         return list_workout

