class Library:
    def __init__(self,Books):
        self.books=Books
    def displayBooks(self):
         for keys , values in self.books.items(): # Here self.books is dict using 
            # items we can access both key values in the dict 
            print(f"{keys} {values}")
    def borrowBook(self,bookname):
        if(self.books[bookname]>0):
            print(f"You have borrowed {bookname} this book")
            self.books[bookname]-=1
            return True
           
        else:
            print("Sorry this Book is int available")
            return False
    def returnBook(self,bookname):
        self.books[bookname]+=1
        print("Thanks for returning the book.Please Visit us Again")
class Student(Library):
    def requestBook(self):
        self.books1=input("Enter the Book u want to boorow")
        centralLib.borrowBook(self.books1)
    def returnBOOK(self):
        self.books1=input("Enter the Book u want to return")
        centralLib.returnBook(self.books1)
centralLib=Student({"Algorithms" : 3,"Theory of Computations": 3,"Data Structure":3,"Mathematics":3})
if __name__=="__main__":
    print("Hello Welcome to Central Libarary Please Choose an option below")
    print("Press 1 for displaying books available in the library ")
    print("Press 2 for Borrow books available in the library ")
    print("Press 3 for Return books available in the library ")
    print("Press 4 for Exiting from the library ")
    while(True):
        no=int(input("Enter the number "))
        if(no==1):
            centralLib.displayBooks()
        elif(no==2):
            centralLib.requestBook()
        elif(no==3):
            centralLib.returnBOOK()
        else:
            print("Thank Tou Visit Again")
            break

