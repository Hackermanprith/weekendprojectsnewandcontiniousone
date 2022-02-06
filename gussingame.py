import random
number = random.randint(0 , 10000)
print (number)
def users():
    user = int(input("Enter your guess ediot"))
    if user > number:
        print("Too high guess")
    elif user < number:
        print("Too low guess")
    elif user == number:
        print("Correct guess")
        

while True:
    users()