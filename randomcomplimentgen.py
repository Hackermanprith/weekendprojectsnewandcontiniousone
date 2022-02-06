#imports
import random
#intial variables
#Just cheking for grammer and also intial inouts
name = input("What is your name:")
gender = input("what is your gender as F or f as female and M or m as Male").strip().lower()
#heshe and things:

while True:
    if gender == "m" :
        heshe = "he"; hisher = "his"; guygirl = "guy"; himher = "him"; 
        break
    elif gender == "f":
        heshe = "She"; hisher = "Her"; guygirl = "girl"; himher = "her"; 
    else:
        print("Not valid input")
        break
complements = [name + " is a very great " + guygirl,
               name +  " is very talented " + guygirl + " he is always ready to help",
               name + " is very hard working " + guygirl +" like " + hisher + " parents ",
               name + " is the best ",
               name + " has big dreams and " + heshe + " can make them true ",
               name + " is very generous " + heshe + " dornates to charity and dosen't care about " + himher + "self "+ heshe + "is always thinking about others good."
               ]

history = []
#some stupid loops boi
for i in range(6):
    text = random.choice(complements)
    print(text)
    try:
        history.index(text)
        continue
    except:
        history.append(text)
