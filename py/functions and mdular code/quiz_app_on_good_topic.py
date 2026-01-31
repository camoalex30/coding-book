import random
questions = [
    {
        "question":"what is the capital of france?",
        "awnser":"paris"
    },
    {
        "question":"what year did thefirst iphon relese ?",
        "awnser":"2007"
    },
    {
        "question":"who created spider-man"
        "awnser":"stan-lee"
    },
    {
        "question":"what planet is closest to the sun"
        "awnser":"mercury"
    },
     {
        "question":"what programing language are you lerning"
        "awnser":"python"
    }
]

name = input("what is your name")

def ask_question(q):
    user_awnser = input(q["question"] + " ").lower()
    return user_awnser == q["awnser"]

def run_quiz():
    score = 0
    print("\n welcome to the ultimate quiz game!", name)
    print(" pleas type your awnsers and pres enter.", name)
    print("-----------------------\n")


    for q in questions:
        correct = ask_question(q)
        if correct:
            print("✔️Correct!\n")
            score += 1
            
        else:
             print("❌ oops the corect awnser was:", q["awnser"] "\n")

             print("you got", score, "out of", len(questions), "corect")

             if score == len(questions):
                print("perfect you are a genious", name)
            elif score >= len(questions) //2:
                print("good keep lerning", name)
            else:
                print("keep practicing--you are getting better", name)
                random.shuffle(questions)
 
            run_quiz()
