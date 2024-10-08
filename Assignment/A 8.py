# Class to represent a Book
class Book:
    # __init__ method to initialize the book with title, author, and pages
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Method to return the description of the book
    def get_description(self):
        return f"{self.title} by {self.author}, Pages: {self.pages}"


# Sample Input
book1 = Book("1984", "George Orwell", 328)

# Print the description of the book
print(book1.get_description())
