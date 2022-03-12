from datetime import *
import json
from tkinter import Menu
from termcolor import colored,cprint
class library:
    def __init__(self):
        self.books = {}
        self.currentborrowers = {}
        
    def add(self):
        bookname = input("Enter the book name: ")
        bookauthor = input("Enter the book author: ")
        agerecomendation = int(input("Enter the age recomendation: "))
        shelfno = int(input("Enter the shelf no: " ))
        jounre = input("Enter the jounre: ")
        self.books[bookname] = [bookname, bookauthor, agerecomendation,shelfno,jounre,True]
        
    def borrow(self):
        borrowersname = input("Enter the borrowers name: ")
        bookname = input("Enter the book name: ")
        borrowersphone = input("Enter Borrowers phone number: ")
        returndate = int(input("Enter the no of days to be returned in: "))
        Date_ret = date.today() + timedelta(days=returndate)
        date_iss = date.today()
        library.currentborrowers[bookname] = [borrowersname,borrowersphone, bookname,date_iss,Date_ret]
        self.books[bookname][5] = False
        print(self.books)
        print(self.currentborrowers)
        
    def returnbook(self):
        borrowersname = input("Enter the borrowers name: ")
        bookname = input("Enter the book name: ")
        self.books[bookname][5] = True
        self.currentborrowers.pop(bookname)
        print(self.books)
        print(self.currentborrowers)
    
    def recontinueabook(self):
        bookname = input("Enter the bookname name: ")
        newreturndate = int(input("Enter the number of days you wanna extend the book: "))
        self.currentborrowers[bookname][4] = date.today() + timedelta(days=newreturndate) 
        
    def findbook(self):
        bookname = input("Enter the book name: ")
        if bookname in self.books.keys():
            if self.books[bookname][5] == True:
                print(f"Book is available it is in shelf no {self.books[bookname][3]} and jounre is {self.books[bookname][4]}")
            elif  self.books[bookname][5] == False:
                print(f"Book is not available it is borrowed by {self.currentborrowers[bookname][0]} and it will be returned on {self.currentborrowers[bookname][4]}")
        else:
            print("Book is not in library")
    
    #add jounre , author
    def filterbooks(self):
        print("1. Filter by author")
        print("2. Filter by age recomendation")
        print("3. Filter by jounre")
        option = int(input("Enter your option: "))
        if option == 1:
            age = int(input("Enter the age"))
            for book in self.books.keys():
                if self.books[book][2] >= age:
                    if self.books[book][5] == True:
                        print(f"{book} is available it is in shelf no {self.books[book][3]} and jounre is {self.books[book][4]}")
                    elif self.books[book][5] == False:
                        print(f"{book} is in library but it is borrowed by {self.currentborrowers[book][0]} and it will be returned on {self.currentborrowers[book][4]}")
                else:
                    print("Sorry but no book for this age is available")
        elif option == 2:
            authour = input("Enter the author name: ")
            for book in self.books.keys():
                if self.books[book][1] == authour:
                    if self.books[book][5] == True:
                        print(f"{book} is available and can be borrrowed now")
                    elif self.books[book][5] == False:
                        print(f"{book} is available but is borrowed by {self.currentborrowers[book][0]} and will be returned on {self.currentborrowers[book][4]}")
                else:
                    print("Sorry but no book for this author is available") 
        elif option == 3:
            jounre = input("Enter the jounre name: ")
            for book in self.books.keys():
                if self.books[book][4] == jounre:
                    if self.books[book][5] == True:
                        print(f"{book} is available and can be borrrowed now")
                    elif self.books[book][5] == False:
                        print(f"{book} is available but is borrowed by {self.currentborrowers[book][0]} and will be returned on {self.currentborrowers[book][4]}")
                else:
                    print("Sorry but no book for this jounre is available")
        else:
            library.filterbooks()
        
    def booksborrowedby(self):
        borrowersname = input("Enter the borrowers name: ")
        for book in self.currentborrowers.keys():
            if self.currentborrowers[book][0] == borrowersname:
                print(f"{book} is borrowed by {borrowersname} and it will be returned on {self.currentborrowers[book][4]}")
                
    def finalbeforeexitprep(self):
        json.dump(self.books,open("books.json","w"))
        json.dump(self.currentborrowers,open("currentborrowers.json","w"))
        
    def startprep(self):
        B = open('books.json')
        borrowers = open('currentborrowers.json')
        self.books = json.load(B)
        self.currentborrowers = json.load(borrowers)
    def showallbooks(self):
        for book in self.books.keys():
            print(f"{book} is available and can be borrrowed now")
    def menu():
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Find a book")
        print("5. Filter books")
        print("6. Books borrowed by a user")
        print("7. Recontinue a book")
        print("8. Show all books")
        print("9. Exit")
if __name__ == "__main__":
    l = library()
    l.startprep()
    while(True):
        library.menu()
        inputb = int(input("Enter your option: "))
        if inputb == 1:
            l.add()
        if inputb == 2:
            l.borrow()
        if inputb == 3:
            l.returnbook()
        if inputb == 4:
            l.findbook()
        if inputb == 5:
            l.filterbooks()
        if inputb == 6:
            l.booksborrowedby()
        if inputb == 7:
            l.recontinueabook()
        if inputb == 8:
            l.showallbooks()
        if inputb == 9:
            l.finalbeforeexitprep()
            exit()
            