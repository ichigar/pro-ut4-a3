import pickle
from re import L

class Reader:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__books = []

        
    def add_book(self, book):
        self.__books.append(book)
        
    def __str__(self) -> str:
        result = f"{self.__name} {self.__age}\n"
        result += f"{len(self.__books)} libros"
        return result
        
class Library:
    filename = "readers.dat"
    
    def __init__(self, name):
        self.__name = name
        self.__readers = []
        self.clear_file()
        
    def add_reader(self, reader):
        readers = self.load_readers()
        if readers:
            self.__readers = readers
        else:
            self.__readers = []
    
        self.__readers.append(reader)
        self.store_readers()
        
    def show_readers(self):
        self.load_readers()
        for reader in self.__readers:
            print(reader)
        
    def load_readers(self):
        self.__readers.clear()
        self.__readers = []
        try:
            with open(self.filename, "rb") as file:
                self.__readers.append(pickle.load(file))
                
        except FileNotFoundError:
            return False
        
    def store_readers(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.__readers, file)

    def clear_file(self):
        with open(self.filename, "wb") as file:
            file.truncate()
            
r1 = Reader("Juan", 20)
r2 = Reader("Pedro", 30)
r3 = Reader("Ana", 40)
r1.add_book("Python")
r1.add_book("Java")
r2.add_book("C++")
r2.add_book("C")
r3.add_book("JavaScript")


l = Library("Librería")
l.add_reader(r1)
l.add_reader(r2)
l.add_reader(r3)
l.show_readers()
