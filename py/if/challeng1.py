print("welcome to the mood-based playlist generator")
print("how are you feeling today")
print("choose from happy, sad, angry, tired or excited")

mood = input("enter your mood")

#if else logic

mood = mood.lower()


#conditions

if mood == "happy":
    print("heres your happy playlist")
elif mood == "sad":
    print("here is your sad playlist")
elif mood == "angry":
    print("here is your sad playlist")
elif mood == "tired":
    print("here is your tired playlist")
elif mood == "excited":
    print("here is your excited playlist")
else:
    print("sorry i didn't get that try again with a listed one")
    
    
name = input("what is your name")
print("hi", name + "!", "lets find a playlist for your mood")


if mood == "happy":
    print("happy vibes only here is your playlist")
    
mood = input("how are you feeling today(you can list more than 1)").lower()

if "happy" in mood:
    print("uplifting tunes coming your way")
if "sad" in mood:
    print("here are some tunes to help u though it")
if "angry" in mood:
    print("turn up the volume and let it out")
if "tired" in mood:
    print("time to wind down these mellow tracks")
if "excited" in mood:
    print("pump-up the playlist ready to go")