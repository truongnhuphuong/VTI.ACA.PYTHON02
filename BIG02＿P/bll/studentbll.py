from dal import StudentDAL
from dto import StudentDto

class StudentBLL:
    def __init__(self):
        self.__stDAL = StudentDAL()
    def insert(self, st: StudentDto):
        return self.__stDAL.insert(st)
    def update(self, st: StudentDto):
        return self.__stDAL.update(st)
    def delete(self, code: str):
        return self.__stDAL.delete(code)
    def get(self):
        return self.__stDAL.get()
    def getOne(self, code: str):
        return self.__stDAL.getOne(code)
    def search (self, text: str):
        return self.__stDAL.search(text)
    def checkExists(self,code:str):
        return self.__stDAL.checkExists(code)