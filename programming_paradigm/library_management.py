
class Book:
    def __init__(self, title = None, is_checked_out = None):
        if title == None and is_checked_out == None:
            self.title = "Book"
            self.__is_checked_out = False
        else:
            self.title = title
            self.__is_checked_out = is_checked_out


class Library:
    __books = []
    def add_book(self,book):
        self.__books.append(book)