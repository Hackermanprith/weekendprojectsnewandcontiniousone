from datetime import *
        
class library:
    def __init__(self):
        self.books = {}
        self.currentborrowers = {}
        
    def add(self):
        bookname = input("Enter the book name")
        bookauthor = input("Enter the book author")
        agerecomendation = int(input("Enter the age recomendation"))
        shelfno = int(input("Enter the shelf no"))
        jounre = input("Enter the jounre")
        self.books[bookname] = [bookname, bookauthor, agerecomendation,shelfno,jounre,True,]
        print(self.books)
        
    def borrow(self):
        borrowersname = input("Enter the borrowers name")
        bookname = input("Enter the book name")
        borrowersphone = input("Enter Borrowers phone number")
        returndate = int(input("Enter the no of days to be returned in"))
        Date_ret = date.today() + timedelta(days=returndate)
        date_iss = date.today
        library.currentborrowers[bookname] = [borrowersname,borrowersphone, bookname,date_iss,Date_ret]
        self.books[bookname][5] = False
        print(self.books)
        print(self.currentborrowers)
        
    def returnbook(self):
        borrowersname = input("Enter the borrowers name")
        bookname = input("Enter the book name")
        self.books[bookname][5] = True
        self.currentborrowers.pop(borrowersname)
        print(self.books)
        print(self.currentborrowers)
        
    def checkifistrue(self,bookname):
        if self.books[bookname][5] == True:
            print("Book is available")
        elif  self.books[bookname][5] == True:
            print("Book is not available")
        else:
            print("Book is not in library")
    
    def recontinueabook(self):
        bookname = input("Enter the bookname name")
        newreturndate = input("Enter the number of days you wanna extend the book")
        self.currentborrowers[bookname][4] = date.today() + timedelta(days=newreturndate) 
        
    
print(library.books)

