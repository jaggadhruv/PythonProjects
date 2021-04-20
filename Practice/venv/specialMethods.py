print("This script is Special Methods Script")


class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages


    # string representation - special method for string
    def __str__(self):
        return f"{self.title} by {self.author} with {self.pages} pages"



# --------------------------------------------------------

my_book = Book(title="Damru ki Kahanian",author="Prupaliti",pages=458)

print(my_book)