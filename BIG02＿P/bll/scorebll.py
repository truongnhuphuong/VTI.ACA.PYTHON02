from pydoc import text
from dal import ScoreDAL
from dto import ScoretDto

class ScoreBLL:
    def __init__(self):
        self.__scDAL = ScoreDAL()
    def insert(self, sc: ScoretDto):
        return self.__scDAL.insert(sc)
    def update(self, sc: ScoretDto):
        return self.__scDAL.update(sc)
    def get(self):
        return self.__scDAL.get()
    def getOne(self, stcode: str, sucode:str):
        return self.__scDAL.getOne(stcode, sucode)
    def search (self, text: str):
        return self.__scDAL.search(text)
    def checkExists(self, stcode: str, sucode:str):
        return self.__scDAL.checkExists(stcode, sucode)
    def exportScores(self):
        pass