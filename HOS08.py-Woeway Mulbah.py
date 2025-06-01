class LibraryCatalop:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append (book)

    def display_all_books (self):
        for book in self.books:
            book.display_info()
            print()

# reverse the display_info function
    def display_info(self):
        info = f"Title: {self.title}\n" \
               f"Author: {self.author}\n"\
               f"ISBN: {self.isbn}\n"\
               f"Status: {'Checked out' if self.is_checked_out else 'Available'}"
        print(info)

# Revise the Ebook and add downloaddetails 
class Ebook(book): 
    def _int_(self, title, author, isbn, download_link, file_size):
        super()._init_(title, author, isbn)
        self.download_details = DownloadDetails(download_link, file_size)   # type: ignore


    def display_info(self):
        super().display_info()
        self.download_details.display_download_info()


class DownloadDetails:
    def __init__(self, link, size):
        self.link = link
        self.size = size


    def display_download_info(self):
        print(f"Download Link: {self.link}")
        print(f"File Size: {self.size}MB")


# Revise the bottom test cases to incorporate all the new classes
physical_book = book ("The Great Gatsby", "F. Scott Fitzgerald", "1234567890") # type: ignore
ebook = Ebook( "1984", "George Orwell", "0987654321", "http://ebooks.example.com/1984", 2)

my_library = LibraryCatalop()
my_library.add_book(physical_book)
my_library.add_book(ebook)

print("Library Catalog:")
print("Displaying info for the books in the library:")
my_library.display_all_books()

            
                

# Create Book Class
class book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False


    def check_in_or_out(self):
        self.is_checked_out = not self.is_checked_out
        status = "checked out" if self.is_checked_out else"checked in"
        print(f"The book {self.title}, by {self.author} is now {status}.")


    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {'Checked out' if self.is_checked_out else 'Available'}")       


# Create EBook 
class EBook(book) :
    def __init__(self, title, author, isbn, downlaod_link, files_size):
        super().__init__(title, author, isbn)
        self.download_link = downlaod_link
        self.file_size = files_size

    def display_info(self):
        super(). display_info()
        print(f"Download Link: {self.download_link}")
        print(f"File Size: {self.file_size} MB")

# Create two objects to test
physical_book =book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
EBook =EBook("1984", "George Orwell", "0987654321", "http://ebooks.example.com/1984", 2)


physical_book.display_info()
physical_book.check_in_or_out()
physical_book.check_in_or_out()

print()

EBook.display_info()

# The expected output:
