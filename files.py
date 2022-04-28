import pickle
import os

from youtube_dl import list_extractors

class Reader:
    """A reader has a name, an age and a list of books readed."""
    def __init__(self, name, age):
        # Los atributos son públicos para poder convertir el objeto en diccionario facilmente
        self.__name = name            
        self.__age = age
        self.__books = []

    def get_dict(self):
        return {
            "name": self.__name,
            "age": self.__age,
            "books": self.__books
        }
        
    def put_dict(self, dic):
        self.__name = dic["name"]
        self.__age = dic["age"]
        self.__books = dic["books"]
        
    def add_book(self, book):
        self.__books.append(book)
        
    def get_name(self):
        return self.__name
        
    def __str__(self) -> str:
        result = f"{self.__name} {self.__age}\n"
        for book in self.__books:
            result += f"*{book}\n"
        return result
        
class Library:
    """A library has a name and a list of readers. The list of readers is stored in a file."""
    
    filename = "readers.dat"
    
    def __init__(self, name):
        self.__name = name
        self.__readers = []
        self.__clear_file()
        self.__sync_readers()

    def add_reader(self, reader):
        """Adds a reader to the library and stores it in the file"""
        self.__readers.append(reader)
        list_readers = []
        list_readers = self.__load_readers()

        list_readers.append(reader.get_dict())
        print(list_readers)
        self.__store_readers(list_readers)
        
    def del_reader(self, reader_name):
        """Delete a reader from the library and the file"""
        for reader in self.__readers:
            # Buscamos el lector por su nombre
            if reader.get_name() == reader_name:
                # Lo eliminamos de la lista de lectores
                self.__readers.remove(reader)
                
                # Eliminamos el libro del fichero
                list_readers = []
                list_readers = self.__load_readers()                
                for reader_dict in list_readers:
                    if reader_dict["name"] == reader_name:
                        list_readers.remove(reader_dict)
                        break
                # Actualizamos el fichero
                self.__store_readers(list_readers)
                break
        
    def show_readers(self):
        """Show all readers in the library"""
        for reader in self.__readers:
            print(reader)
    
    def __readers_as_objects(self, list_readers):
        """Returns a list of Reader objects from a list of readers dictionaries"""
        result = []

        for reader_dict in list_readers:
            reader = Reader()
            reader.put_dict(reader_dict) 
            result.append(reader)
        return result    
    
    def __load_readers(self):
        """Return a list of dict readers from the file"""
        list_readers = []
        if os.path.getsize(self.filename) > 0:
            with open(self.filename, "rb") as file:
                    list_readers = pickle.load(file)

        return list_readers
    

        
        
    def __store_readers(self, list_readers):
        if not list_readers:
            self.__clear_file()
        else:
            with open(self.filename, "wb") as file:
                pickle.dump(list_readers, file)

    def __sync_readers(self):
        list_readers = self.__load_readers()
        if list_readers:
            self.__readers = self.__readers_as_objects(list_readers)
    
    def __clear_file(self):
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
l.del_reader("Pedro")
l.show_readers()
