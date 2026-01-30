print("welcome to your daily habit tracker")
name = input("what is your name")
print("hi", name + "lets check off your habits")

habits = ["exersize","read for 15 minutes","drink water","practice coding"]


for habit in habits:
    response = input("did you" + habits + "today?(yes/no):")
    if response.lower() == "yes":
        print("👍 nice job", habit + "!")
    else:
        print("❌ try again tomarow")
        
while True:
    print("\n---daily habit check---")
    for habit in habits:print("")
    response = input("did you" + habits + "today?(yes/no):")
    if response.lower() == "yes":
        print("👍 great work on", habit + "!")
    else:
        print("❌ no worries try again tomarow")
        again = input("\nType 'done' to exit or press enter to track again tomarow:")
        if again.lower() == "done":
            print("see you tomorrow," +name+ "!")

        