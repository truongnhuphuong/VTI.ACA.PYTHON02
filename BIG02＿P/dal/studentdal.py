from dto import StudentDto
from .dbprovider import DBProvider

class StudentDAL:
    def __init__(self):
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    #Tạo table nếu chưa tồn tại
    def __createTableIfNotExists(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS Students(
                Code VARCHAR(6) PRIMARY KEY,
                FullName NVARCHAR(30),
                Birthday VARCHAR(20),
                Sex TINYINT(1),
                Address NVARCHAR(50),
                Phone VARCHAR(20),
                Email VARCHAR(50)
            )
        '''

        self.__dbProvider.exec(sql)

    #Thêm
    def insert(self, st: StudentDto):
        sql = """
            INSERT INTO Students(Code, FullName, Birthday, Sex, Address, Phone, Email)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (st.Code, st.FullName, st.Birthday, st.Sex, st.Address, st.Phone, st.Email)
        return self.__dbProvider.exec(sql,params)
    
    #Sửa
    def update(self, st: StudentDto):
        sql = '''
            UPDATE Students
            SET 
                FullName = %s,
                Birthday = %s,
                Sex = %s,
                Address = %s,
                Phone = %s,
                Email = %s
            WHERE Code = %s
        '''

        params = (st.FullName, st.Birthday, st.Sex, st.Address, st.Phone, st.Email, st.Code)
        return self.__dbProvider.exec(sql, params)

    #Xóa
    def delete(self, code: str):
        sql = '''
            DELETE FROM Students
            WHERE Code = %s
        '''

        params = (code,) #vì đây là 1 tuple
        return self.__dbProvider.exec(sql, params)


    #Lấy nhiều bản ghi
    def get(self):
        sql = '''
            SELECT * FROM Students
        '''

        students = self.__dbProvider.get(sql) #Type: List <tuple>
        #Chuyển dữ liệu list<tuple> sang "túi đựng" list <StudentDto>
        studentDtos = list(map(lambda st: StudentDto(st[0],
                                                     st[1],  
                                                     st[2], 
                                                     st[3], 
                                                     st[4], 
                                                     st[5], 
                                                     st[6]),
                                        students))
        return studentDtos
    
    
    #Lấy 1 bản ghi
    def getOne(self, code: str):
        sql = '''
            SELECT * FROM Students
            WHERE Code = %s
        '''
        params = (code,)

        student = self.__dbProvider.getOne(sql, params)
        studentDto = StudentDto(student[0],
                                student[1],
                                student[2],
                                student[3],
                                student[4],
                                student[5],
                                student[6])
        return studentDto
    #Tìm kiếm
    def search (self, text: str):
        sql = '''
            SELECT * FROM Students
            WHERE
                Code = %s
                OR FullName LIKE %s
                OR Email LIKE %s
        '''
        params = (text, f'%{text}%' ,f'%{text}%') #Giống dạng kiểu %a%

        students = self.__dbProvider.get(sql, params) #Type: List <tuple>
        #Chuyển dữ liệu list<tuple> sang "túi đựng" list <StudentDto>
        studentDtos = list(map(lambda st: StudentDto(st[0],
                                                     st[1],  
                                                     st[2], 
                                                     st[3], 
                                                     st[4], 
                                                     st[5], 
                                                     st[6]),
                                        students))
        return studentDtos

    #Kiểm tra tồn tại của ID
    def checkExists(self, code: str):
        isExists = False # Trạng thái có tồn tại hoặc không
        sql = """
            SELECT * FROM Students
            WHERE Code = %s
        """
        params = (code,)
        student = self.__dbProvider.getOne(sql, params)
        if student is not None:
            isExists = True # Set thành có tồn tại
        return isExists