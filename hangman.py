"""
Hangman by Prithwish Mukherjee 
Google Dev Account: https://developers.google.com/profile/u/pmdev
Replit Account: https://replit.com/@PrithwishMukher
Devto: https://dev.to/dashboard
"""
import random
from turtle import color
from termcolor import colored,cprint
from pyfiglet import Figlet
wordlist_1 = ["Hi","Hello","Bye"]
wordlist_2 = ["mrbeast","technogamerz","liveinsaan"]
wordlist_3 = ["ifweklfjewf","fjmfef","fhokevfgefhr"]
#base vars for font
f = Figlet(font='banner3-D')
print(colored(f.renderText("Welcome to PyHangman"),'green'))
def get_random_word(difficulty_level):
    if difficulty_level == "1":
        word = random.choices(wordlist_1)
        word_letters = set(word) 
    elif difficulty_level == "2":
        word = random.choice(wordlist_2) 
        word_letters = set(word) 
    elif difficulty_level == "3":
        word = random.choice(wordlist_3)
        word_letters = set(word) 
    return word_letters, word

def hangman_basics(word):    
    for i in range(0,len(word)):
        print(" - ",end="")
    return word

def hangman_main_play(word,word_letters):
    used_letters = set() 

    #lives
    lives = 0
    for i in range(0,len(word)):
        lives +=1

    while lives > 0 and len(word) > 0:
        userguess = input("Enter your guess ").lower().strip()



def welcome():
    cprint("              Welcome to Hangman Youtuber Edition  ", 'red')
    cprint('        You will have to guess the name of the youtuber , For each correct','yellow')
    cprint('        you will get another extra life and wrong name guess will lead to ','green')
    cprint('        1 life loss, You will also be given hints,As we all know you are a noob','blue')
    cprint('PS: DO NOT ENTER SPACES FOR EXAMPLE IF YOUT GUESS IS TECHNO GAMERZ ENTER TECHNOGAMERZ','magenta')

user_inp_difficulty = "2"

welcome()
hangman_main_play(hangman_basics(get_random_word(user_inp_difficulty)))    



