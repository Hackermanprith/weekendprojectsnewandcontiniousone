"""
Hangman by Prithwish Mukherjee 
Google Dev Account: https://developers.google.com/profile/u/pmdev
Replit Account: https://replit.com/@PrithwishMukher
Devto: https://dev.to/dashboard
"""

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
