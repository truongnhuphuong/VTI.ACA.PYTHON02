from .dbprovider import DBProvider
from dto import ScoretDto

class ScoreDAL:
    def __init__(self):
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()
    
    #Tạo table nếu chưa tồn tại
    def __createTableIfNotExists(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS Scores(
                StudentCode VARCHAR(6),
                SubjectCode VARCHAR(6),
                Score1 INT,
                Score2 INT,
                PRIMARY KEY (StudentCode, SubjectCode),
                FOREIGN KEY(StudentCode) REFERENCES Students(Code) ON DELETE CASCADE,
                FOREIGN KEY(SubjectCode) REFERENCES Subjects(Code) ON DELETE CASCADE
            )
        '''

        self.__dbProvider.exec(sql)
    
    #Thêm
    def insert(self, sc: ScoretDto):
        sql = """
            INSERT INTO Scores(StudentCode, SubjectCode, Score1, Score2)
            VALUES (%s, %s, %s, %s)
        """
        params = (sc.STcode, sc.SUcode, sc.SC1, sc.SC2)
        return self.__dbProvider.exec(sql,params)
    
    #Sửa
    def update(self, sc: ScoretDto):
        sql = '''
            UPDATE Scores
            SET 
                Score1 = %s,
                Score2 = %s
            WHERE StudentCode = %s AND SubjectCode = %s
        '''
        params = (sc.SC1, sc.SC2, sc.STcode, sc.SUcode )
        return self.__dbProvider.exec(sql, params)
    #Lấy nhiều bản ghi
    def get(self):
        sql = '''
            SELECT * FROM Scores
        '''

        scores = self.__dbProvider.get(sql) #Type: List <tuple>
        #Chuyển dữ liệu list<tuple> sang "túi đựng" list <StudentDto>
        scoreDtos = list(map(lambda sc: ScoretDto(sc[0],
                                                     sc[1],
                                                     sc[2],
                                                     sc[3]),
                                        scores))
        return scoreDtos
   
    #Lấy 1 bản ghi
    def getOne(self, stcode: str, sucode:str):
        sql = '''
            SELECT * FROM Scores
            WHERE StudentCode = %s AND SubjectCode = %s
        '''
        params = (stcode, sucode)

        score = self.__dbProvider.getOne(sql, params)
        scoreDto = ScoretDto(score[0],
                            score[1],
                            score[2],
                            score[3])
        return scoreDto
    #Tìm kiếm
    def search (self, text: str):
        sql = '''
            SELECT * FROM Scores
            WHERE StudentCode = %s OR SubjectCode = %s
        '''
        params = (text, text) #Giống dạng kiểu %a%

        scores = self.__dbProvider.get(sql, params) #Type: List <tuple>
        #Chuyển dữ liệu list<tuple> sang "túi đựng" list <StudentDto>
        scoreDtos = list(map(lambda sc: ScoretDto(sc[0],
                                                  sc[1],
                                                  sc[2],
                                                  sc[3]),
                                        scores))
        return scoreDtos
    #Kiểm tra tồn tại của ID
    def checkExists(self, stcode: str, sucode:str):
        isExists = False # Trạng thái có tồn tại hoặc không
        sql = """
            SELECT * FROM Scores
            WHERE StudentCode = %s AND SubjectCode = %s
        """
        params = (stcode, sucode)
        score = self.__dbProvider.getOne(sql, params)
        if score is not None:
            isExists = True # Set thành có tồn tại
        return isExists

    def exportScores(self, rank=''):
        '''
        : get all
        A: 90-100
        B:...
        C
        D
        '''
        sql = '''
            WITH sub AS (
                SELECT st.`Code`, st.`FullName`, st.`Birthday`, 
                    CASE
                        WHEN st.`sex` = 0 THEN "Nữ"
                        ELSE "Nam" 
                    END AS "Sex", 
                    st.`Address`,
                    st.`Phone`, st.`Email`, su.`Name`,
                    round(((sc.`score1` + sc.`score2`*2)/3),2) as `Finalscore`
                FROM `students` st
                INNER JOIN `scores` sc
                ON st.`Code` = sc.StudentCode
                INNER JOIN `subjects` su 
                ON sc.`SubjectCode` = su.`Code`
            )
            SELECT *,
                CASE
                    WHEN `Finalscore` <=100 AND `Finalscore` >= 90 THEN "A"
                    WHEN `Finalscore` >= 70 THEN "B"
                    WHEN `Finalscore` >= 50 THEN "C"
                    ELSE "D" 
                END AS "Rank"
            FROM sub
        '''
        if rank == 'A':
            sql += 'WHERE <a>'
        elif rank == 'B':
            pass

        return self.__dbProvider.get(sql) #Type: List <tuple>