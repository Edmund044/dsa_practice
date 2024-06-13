from abc import ABC, abstractmethod

class Frontend():
    def __init__(self,data_source) -> None:
        self.data_source = data_source

    def display_data(self):
        return self.data_source.get_data()
        


class DataSource:
    @abstractmethod
    def get_data(self):
        pass


class Database(DataSource):
    def get_data(self):
        print("Getting data from database")

class API(DataSource):
    def get_data(self):
        print("Getting data from API")

frontend = Frontend(API())
frontend.display_data()
frontend = Frontend(Database())
frontend.display_data()