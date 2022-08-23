# Library manager
# code by prashant kumar bhaskar
def getdate():
    import datetime
    return datetime.datetime.now()
class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} AVAILABLE BOOKS ARE: ")
        for book in self.books:
            print(" ♦-- " + book)
        print("\n")
    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(
                f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED.\n")
        else:
            track.append({name: bookname})
            self.books.remove(bookname)
            with open("booklogs.txt", "a") as b:
                b.write(str([str(getdate())]) + "-" + bookname + "," + "borrowed by-" + name + "\n")
                print("Thank you")
            print("BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN ON TIME.\n")
            with open('books.txt','r') as file:
                filedata=file.read()
                filedata=filedata.replace(bookname,"")
                with open('books.txt','w') as file:
                    file.write(filedata)
    def returnBook(self, bookname):
        print("BOOK RETURNED : THANK YOU! \n")
        self.books.append(bookname)
        with open("book.txt", "a") as bk:
            bk.write(bookname+"\n")

    def donateBook(self, bookname):
        print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
        self.books.append(bookname)
        with open("bookdonationlogs.txt", "a") as d:
            print("please enter your name")
            v=input()
            d.write(str([str(getdate())]) + "-" + bookname +","+ "donated by-"+v+"\n")
            print("Thank you for donating")
        with open("book.txt", "a") as bk:
            bk.write(bookname+"\n")

class Student():
    def requestBook(self):
        self.book = input("Enter name of the book you want to borrow: ")
        return self.book


    def returnBook(self):
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        if {name: self.book} in track:
            track.remove({name: self.book})
        with open("booklogs.txt", "a") as b:
            b.write(str([str(getdate())]) + "-" + self.book +","+ "returned by-"+name+"\n")
            print("Thank you")
        return self.book


    def donateBook(self):
        self.book = input("Enter name of the book you want to donate: ")
        return self.book


if __name__ == "__main__":

    Mylibrary = Library(
        ["Constitution of india", "invention of bulb","wings of fire", "rich dad & poor dad", "indian polity", "macroeconomics", "microeconomics"])
    student = Student()
    track = []

    print("\t\t\t\t\t\t\t♦♦♦♦♦♦♦ WELCOME TO THE MY LIBRARY ♦♦♦♦♦♦♦\n")
    while (True):
        # print(track)
        print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. exit the library\n""")

        try:
            usr_response = int(input("Enter your choice: "))

            if usr_response == 1:  # listing
                Mylibrary.displayAvailableBooks()
            elif usr_response == 2:  # borrow
                Mylibrary.borrowBook(
                    input("Enter your name: "), student.requestBook())
            elif usr_response == 3:  # return
                Mylibrary.returnBook(student.returnBook())
            elif usr_response == 4:  # donate
                Mylibrary.donateBook(student.donateBook())
            elif usr_response == 5:  # track
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")

            elif usr_response == 6:  # exit
                print("THANK YOU ! \n")
                exit()
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:  # catch errors
            print(f"{e}---> INVALID INPUT! \n")
