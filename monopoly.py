from pyfiglet import Figlet
from termcolor import colored,cprint
all_users = []
money = []
loan_taken = {}
class Starting_money:
    def add_user(noofpeopleingame):
        for i in range(noofpeopleingame):
            name = input("Enter the name of the player: ").lower() # .lower() is used to make the name of the user in lower case
            all_users.append(name) # appending the name of the user to the list   
    def add_money(noofpeopleingame):
        for i in range(noofpeopleingame):  # noofpeopleingame is the number of players in the game
            money.append(1500)         # adding money to the index of players in another array 
    def generate_loan_dict():
        for i in range(len(all_users)): # len(all_users) is the number of players in the game
            loan_taken[all_users[i]] = 0 # adding the loan taken to the dictionary

class main_bank:
    def transfer_money():
        user_to_deduct_from = input("Enter the name of the user to deduct from: ").lower() #user to deduct from
        user_to_add_from = input("Enter the name of the user to add to: ").lower() #user to add to
        amount = int(input("Enter the amount to transfer: ")) #amount to transfer
        to_user_name_index = all_users.index(user_to_add_from)  #index of the user to add to
        from_user_name_index = all_users.index(user_to_deduct_from)   #index of the user to deduct from
        money[to_user_name_index] += amount #adding the amount to the user to add to
        money[from_user_name_index] -= amount #deducting the amount from the user to deduct from
        cprint(f"Successfully transferred ${amount}",'green') #printing the amount transferred
        cprint(f"{user_to_add_from} has ${money[to_user_name_index]} after the transaction",'red') #printing the balance of the user to add to
        print(f"{user_to_deduct_from} has ${money[from_user_name_index]} after the transaction",'green') #printing the balance of the user to deduct from
        
    def remove_money():
        user = input("Enter the name of the user to deduct from: ").lower() #user to deduct from
        ammount_to_remove_from_user = int(input("Enter the amount to remove from the user: ")) #amount to remove from the user
        user_name_index = all_users.index(user) #index of the user to deduct from
        money[user_name_index] -= ammount_to_remove_from_user #deducting the amount from the user to deduct from
        print("Money removed successfully") #printing the amount removed
        print(f"{user} has ${money[user_name_index]} left") #printing the balance of the user to deduct from
        
    def take_loan():  
        user = input("Enter the name of the user who will take the loan : ").lower()  #user to take loan from
        ammount_to_take_loan = int(input("Enter the amount to take loan: "))  #amount to take loan
        no_of_rounds = int(input("Enter the number of rounds in which you will repay loan: ")) #number of rounds in which you will repay loan
        user_name_index = all_users.index(user) #index of the user to take loan from
        money[user_name_index] += ammount_to_take_loan #adding the amount to the user to take loan from 
        loan_taken[user] = ammount_to_take_loan  + no_of_rounds * 100 #adding the loan taken to the dictionary
        print("Money added successfully") #printing the amount added
        print(f"Current balance of {user}: ", money[user_name_index]) #printing the balance of the user to take loan from
        print(f"{user} will have to pay ${loan_taken[user]} to end the loan") #printing the loan taken from the dictionary
        
    def add_money():
        user = input("Enter the name of the user who will add money: ").lower() #user to add money to
        ammount_to_add = int(input("Enter the amount to be add: ")) #amount to add
        user_name_index = all_users.index(user) #index of the user to add money to
        money[user_name_index] += ammount_to_add #adding the amount to the user to add money to
        print("Money added successfully") #printing the amount added
        print(f"Current balance of {user} is ", money[user_name_index]) #printing the balance of the user to add money to
    
    def pay_loan():
        user = input("Enter the name of the user who will pay the loan : ").lower() 
        ammount_to_pay_loan = int(input("Enter the amount of the loan you wanna pay: "))
        user_name_index = all_users.index(user)#amount to pay loan
        loan_taken[user] = loan_taken.get(user) - ammount_to_pay_loan
        money[user_name_index] -= ammount_to_pay_loan #deducting the loan taken from the dictionary
        print(f"{user} will have to pay ${loan_taken[user]}") #printing the loan taken from the dictionary
        print(f"Current balance of {user}: ", money[user_name_index]) 
        
    def show_money():
        for i in range(len(all_users)):
            print(f"{all_users[i]} has ${money[i]}")
                                                
    def show_all_loans():
        print("The following users has these loans: ")
        for i in range(len(all_users)):
            if all_users[i] in loan_taken.keys():
                print(f"{all_users[i]} has taken a loan of ${loan_taken[all_users[i]]}")   

if __name__ == "__main__":
    f = Figlet(font='standard')
    print(colored(f.renderText('WELCOME TO MONOPOLY BANK MANAGER'), 'green'))
    cprint("Docs For the Bank Manager is at http://pmdev.in/docs/bank_manager.html",'red')
    noofpeoplewhowillplaythegame = int(input("Enter the number of people who will play the game: "))
    Starting_money.add_user(noofpeoplewhowillplaythegame)
    Starting_money.add_money(noofpeoplewhowillplaythegame)
    Starting_money.generate_loan_dict()
    while True:
        print("Check balance: 1")
        print("Do other stuff: 2")  
        print("Show all loans: 3")
        print("Exit: 4")
        dooption = int(input("Enter the option you want to do: ")  )     
        if dooption == 1:
            main_bank.show_money()
        elif dooption == 2:
            cprint("1. Transfer money",'green')
            print("2. Buy property money (subtract it)")
            print("3. Add money(rent)")
            print("4. Pay loan")
            print("5. Take loan")
            print("6. Show all loans")
            print("7. Exit")
            option = input("Enter the option you want to do: ")
            if option == "1":
                main_bank.transfer_money()
            elif option == "2":
                main_bank.remove_money()
            elif option == "3":
                main_bank.add_money()
            elif option == "4":
                main_bank.pay_loan() 
            elif option == "5":
                main_bank.take_loan()
            elif option == "6":
                main_bank.show_all_loans()
            elif option == "7":
                break
        elif dooption == 3:
            main_bank.show_all_loans()
        elif dooption == 4:
            break