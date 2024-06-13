from abc import ABC, abstractmethod

class Datasource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class API1(Datasource):
    def get_data(self):
        print("Getting data from API1")

class API2(Datasource):
    def get_data(self):
        print("Getting data from API2")


class Frontend():
    def __init__(self,data_source:Datasource) -> None:
        self.data_source = data_source
    
       
    def get_display(self):
        return self.data_source.get_data()

Frontend(API1()).get_display()
# Frontend(API1()).get_display()
# frontend = Frontend(API1())
# frontend.get_display()

        






# from abc import ABC,abstractmethod


# class Datasource(ABC):
#     @abstractmethod
#     def get_data(self):
#         pass

# class API(Datasource):
#     def get_data(self):
#         print("Getting data from AP1")

# class API2(Datasource):
#     def get_data(self):
#         print("Getting data from API2")


# class Frontend():
#     def __init__(self,datasource: Datasource) -> None:
#         self.data_source =  datasource
        

#     def display_data(self):
#         return self.data_source.get_data()

# frontend = Frontend(API())
# frontend.display_data()    

# frontend2 = Frontend(API2())
# frontend2.display_data()
        










# class DataSource(ABC):
#     @abstractmethod
#     def get_data(self):
#         pass

# class Database(DataSource):
#     def get_data(self):
#         print("Getting data from database")

# class API(DataSource):
#     def get_data(self):
#         print("Getting data from API")

# class FrontEnd():                
#     def __init__(self,data_source: DataSource):
#         self.data_source = data_source

#     def display_data(self):
#         return self.data_source.get_data()
    

# frontend = FrontEnd(API())
# frontend.display_data()    

# frontend2 = FrontEnd(Database())
# frontend2.display_data()