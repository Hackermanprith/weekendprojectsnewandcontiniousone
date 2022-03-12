class Book:
    def __init__(self,title,quantity,author,price,genre):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = 0
        self.genre = genre
    
    def set_discount(self,discount):
        self.__discount = discount
    
    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price
    
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()},Genre: {self.genre}"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages,genre):
        super().__init__(title, quantity, author, price, genre)
        self.pages = pages


book = Book("Python",10,"John",100,"Programming")
book.set_discount(0.25)

novel1 = Novel('Malgudi Days', 20, 'Ruskin Bond', 200, 187,"Fantasy")
novel1.set_discount(0.20)
print(book, novel1)
