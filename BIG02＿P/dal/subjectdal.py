from .dbprovider import DBProvider
from dto import SubjectDto

class SubjectDAL:
    def __init__(self):
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()
    
    
    #Tạo table nếu chưa tồn tại
    def __createTableIfNotExists(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS Subjects(
                        Code VARCHAR(6) PRIMARY KEY,
                        Name NVARCHAR(50)
            )
        '''

        self.__dbProvider.exec(sql)
    
    
    #Thêm
    def insert(self, su: SubjectDto):
        sql = """
            INSERT INTO Subjects(Code, Name)
            VALUES (%s, %s)
        """
        params = (su.Code, su.Name)
        return self.__dbProvider.exec(sql,params)
    
    
    #Sửa
    def update(self, su: SubjectDto):
        sql = '''
            UPDATE Subjects
            SET 
                Name = %s
            WHERE Code = %s
        '''
        params = (su.Name, su.Code)
        return self.__dbProvider.exec(sql, params)
    
    
    #Xóa
    def delete(self, code: str):
        sql = '''
            DELETE FROM Subjects
            WHERE Code = %s
        '''

        params = (code,) #vì đây là 1 tuple
        return self.__dbProvider.exec(sql, params)
    
    #Lấy nhiều bản ghi
    def get(self):
        sql = '''
            SELECT * FROM Subjects
        '''

        subjects = self.__dbProvider.get(sql) #Type: List <tuple>
        #Chuyển dữ liệu list<tuple> sang "túi đựng" list <StudentDto>
        subjectDtos = list(map(lambda su: SubjectDto(su[0],
                                                     su[1]),
                                        subjects))
        return subjectDtos
    
    
    #Lấy 1 bản ghi
    def getOne(self, code: str):
        sql = '''
            SELECT * FROM Subjects
            WHERE Code = %s
        '''
        params = (code,)

        subject = self.__dbProvider.getOne(sql, params)
        subjectDto = SubjectDto(subject[0],
                                subject[1])
        return subjectDto
    
    
    #Tìm kiếm
    def search (self, text: str):
        sql = '''
            SELECT * FROM Subjects
            WHERE
                Code = %s
                OR Name LIKE %s
        '''
        params = (text, f'%{text}%') #Giống dạng kiểu %a%

        subjects = self.__dbProvider.get(sql, params) #Type: List <tuple>
        #Chuyển dữ liệu list<tuple> sang "túi đựng" list <StudentDto>
        subjectDtos = list(map(lambda su: SubjectDto(su[0],
                                                     su[1]),
                                        subjects))
        return subjectDtos
    
    
    #Kiểm tra tồn tại của ID
    def checkExists(self, code: str):
        isExists = False # Trạng thái có tồn tại hoặc không
        sql = """
            SELECT * FROM Subjects
            WHERE Code = %s
        """
        params = (code,)
        subject = self.__dbProvider.getOne(sql, params)
        if subject is not None:
            isExists = True # Set thành có tồn tại
        return isExists