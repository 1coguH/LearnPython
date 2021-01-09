Answer = float (input ("How many km would you like to travel?"))

if Answer <= 3 :
    print (" You should walk to your destination")
elif Answer > 3  and Answer <= 300 :
    print ("You should drive to your destination")
else :
    if Answer > 300 :
        print ("You should fly to your destination")