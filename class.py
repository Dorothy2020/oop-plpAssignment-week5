# Assignment1: Design your own class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.__pages = pages 
    def get_info(self):
        return f"'{self.title}' by {self.author}, {self.__pages} pages"

    def get_pages(self): 
        return self.__pages

    def set_pages(self, new_pages):
        if new_pages > 0:
            self.__pages = new_pages
        else:
            print("Page count must be positive.")


class ComicBook(Book):
    def __init__(self, title, author, pages, illustrator):
        super().__init__(title, author, pages)  # Reuse base class constructor
        self.illustrator = illustrator

    def get_info(self):
        return f"'{self.title}' by {self.author}, illustrated by {self.illustrator}"


if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 328)
    comic1 = ComicBook("Spider-Man", "Stan Lee", 50, "Steve Ditko")

    print(book1.get_info())       
    print(comic1.get_info())      
    print(book1.get_pages())      
