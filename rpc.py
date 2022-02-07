"""
Hangman by Prithwish Mukherjee 
Google Dev Account: https://developers.google.com/profile/u/pmdev
Replit Account: https://replit.com/@PrithwishMukher
Devto: https://dev.to/dashboard
"""
import random

comp_wins = 0
player_wins = 0

bestofwhatyouwannaplay = int(input("No of times you wanna play").strip())

#def play(comp_wins,player_wins):
#    user_choice = input("Enter 'R' for rock 'P' for paper and 'S' for scissor\n").lower().strip()
#    comp_choice = random.choice(['r', 'p', 's'])
#  if user_choice == "r":
#        if comp_choice == "p":
 #           print(f"Comp wins a point as it chose {comp_choice} and you chose {user_choice}")
  #          comp_wins +=1
   #         print(f"Comp points"+ str(comp_wins))
    #   if comp_choice == "r":
     ##      print(f"Comp points"+str(comp_wins))
    #     print(f"Player points"+str(player_wins))
     #   if comp_choice == "s":
      #      print(f"User wins a point as it chose {user_choice} and computer chose {comp_choice}")
       ##    print(f"Comp points"+str(comp_wins))
         #   print(f"Player points"+str(player_wins))
        
for i in range(0, bestofwhatyouwannaplay):
    user_choice = input("Enter 'R' for rock 'P' for paper and 'S' for scissor\n").lower().strip()
    comp_choice = random.choice(['r', 'p', 's'])
    if user_choice == "r":
        if comp_choice == "p":
            print(f"No one won a point as you both choose {user_choice}")
            print(f"Comp points"+ str(comp_wins))
            print(f"Player points"+str(player_wins))
        if comp_choice == "r":
            print(f"No one won point as it chose {comp_choice} and you chose {user_choice}")
            print(f"Comp points"+str(comp_wins))
            print(f"Player points"+str(player_wins))
        if comp_choice == "s":
            print(f"User wins a point as it chose {user_choice} and computer chose {comp_choice}")
            player_wins += 1
            print(f"Comp points"+str(comp_wins))
            print(f"Player points"+str(player_wins))   
    elif user_choice == "p":
        if comp_choice == "p":
            print(f"No one won point as it choose {comp_choice} and you choose {user_choice}")
            print(f"Comp points"+ str(comp_wins))
            print(f"Player points"+str(player_wins))
        if comp_choice == "r":
            print(f"User wins a point as it chose {user_choice} and computer chose {comp_choice}")
            player_wins += 1
            print(f"Comp points"+str(comp_wins))
            print(f"Player points"+str(player_wins))
        if comp_choice == "s":
            print(f"Computer wins a point as it choose {comp_choice} and user choose {user_choice}")
            comp_wins += 1
            print(f"Comp points"+str(comp_wins))
            print(f"Player points"+str(player_wins))
    elif user_choice == "s":
        if comp_choice == "s":
            print(f"No one won point as it choose {comp_choice} and you choose {user_choice}")
            print(f"Comp points"+ str(comp_wins))
            print(f"Player points"+str(player_wins))
        if comp_choice == "p":
            print(f"User wins a point as it chose {user_choice} and computer chose {comp_choice}")
            player_wins += 1
            print(f"Comp points"+str(comp_wins))
            print(f"Player points"+str(player_wins))
        if comp_choice == "r":
            print(f"Computer wins a point as it choose {comp_choice} and user choose {user_choice}")
            comp_wins += 1
            print(f"Comp points"+str(comp_wins))
            print(f"Player points"+str(player_wins))
        else:
            print("Invalid input")
    if player_wins > comp_wins:
        print("You are winning")
    elif comp_wins < player_wins:
        print("Computer is winning")
    else:
        print("Its a draw")