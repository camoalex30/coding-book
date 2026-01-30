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

def ask_question(q):
    user_awnser = input(q["question"] + " ").lower()
    return user_awnser == q["awnser"]
