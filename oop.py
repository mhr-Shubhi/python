class books:
    total_books=0
    
    def __init__(self,name,genre):
        self.__name= name# private by adying__
        self.__genre=genre
        books.total_books+=1

    def get_name(self):#method inside class (se end krna)
        return self.__name + "!"

    @staticmethod # decoraters # can only be used by class, not by any object
    def general_info():
        return "books are source of knowledge"

    @property
    def genre(self):
        return "sci-fi"

    def full_info(self):#method h ye bc
        return f"{self.__name} {self.__genre}"

class self_help(books):#inheritance from above
    def __init__(self, __name, __genre,length):
        super().__init__(__name, __genre)
        self.length=length

my_book=self_help("Dune","genre","800 pages")
print(my_book.get_name())


print(my_book.genre)