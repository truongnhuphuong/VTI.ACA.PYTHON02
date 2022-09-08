from dal import SubjectDAL
from dto import SubjectDto

class SubjectBLL:
    def __init__(self):
        self.__suDAL = SubjectDAL()
    def insert(self, su: SubjectDto):
        return self.__suDAL.insert(su)
    def update(self, su: SubjectDto):
        return self.__suDAL.update(su)
    def delete(self, code: str):
        return self.__suDAL.delete(code)
    def get(self):
        return self.__suDAL.get()
    def getOne(self, code: str):
        return self.__suDAL.getOne(code)
    def search (self, text: str):
        return self.__suDAL.search(text)
    def checkExists(self,code:str):
        return self.__suDAL.checkExists(code)