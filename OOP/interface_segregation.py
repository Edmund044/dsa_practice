from abc import ABC,abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self):
        pass

class PhotoCopier(ABC):
    @abstractmethod
    def photo_copy(self):
        pass

class OldPrinter(Printer):
    def print(self):
        print("Old printer printing")

class NewPrinter(Printer,Fax,PhotoCopier):
    def print(self):
        print("New printer printing")      
    def fax(self):
        print("New printer faxing")
    def photo_copy(self):
        print("New printer photocopying")    



new_printer = NewPrinter()
new_printer.print()
new_printer.fax()
new_printer.photo_copy()



              









# from abc import ABC, abstractmethod

# class Printer(ABC):
#     @abstractmethod
#     def print(self):
#         pass

# class Faxer(ABC):
#     @abstractmethod
#     def fax(self):
#         pass    
# class Photocopy(ABC):
#     @abstractmethod
#     def photocopy(self):
#         pass

# class OldPrinter(Printer):
#     def print(self):
#         print("Old printer printing")

# class NewPrinter():
#     def print(self):
#         print("New Printer printing")

#     def fax(self):
#         print("New printer faxing")

#     def photocopy(self):
#         print("New printer photocopying")


# new_printer = NewPrinter()
# old_printer = OldPrinter()
# new_printer.print()
# new_printer.fax()
# new_printer.photocopy()
# old_printer.print()











# class Printer(ABC):
#     @abstractmethod
#     def print(self):
#      pass
# class Faxer(ABC):
#    @abstractmethod
#    def fax(self):
#       pass
   
# class Scanner(ABC):
#    @abstractmethod
#    def scan(self):
#       pass
   

# class OldPrinter(Printer):
#    def print(self):
#       return "Old Printer Priting"

# class NewPrinter(Printer,Faxer,Scanner):
#    def print(self):
#       return "New printer printing"     
#    def fax(self):
#       return "New printer faxing"
#    def scan(self):
#       return "New printer scanning"
   

# old_printer = OldPrinter()
# print(old_printer.print())
# new_printer = NewPrinter()   
# print(new_printer.print())
# print(new_printer.fax())
# print(new_printer.scan())
         