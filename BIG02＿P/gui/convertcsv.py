from dal import DBProvider
import pandas as pd

class convertCSV:
    def __init__(self):
        self.__dbProvider = DBProvider()
    
    def get_all(self):
        sql = '''
            WITH sub AS
                    (
                    SELECT st.`Code`, st.`FullName`, st.`Birthday`, 
                            CASE
                                WHEN st.`sex` = 0 THEN "Nữ"
                                ELSE "Nam" 
                            END AS "Sex", 
                                st.`Address`, st.`Phone`, st.`Email`, su.`Name`,round(((sc.`score1` + sc.`score2`*2)/3),2) as `Finalscore`
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

        result = self.__dbProvider.get(sql) #Type: List <tuple>

        #Chuyển thành dataframe
        df = pd.DataFrame(result, columns = ["Code", "Fullname", "Birthday", "Sex", "Address", "Phone", "Email", "Subjectname", "Finalscore", "Rank"])

        #Export to csv
        from pathlib import Path  
        filepath = Path('out\out_all.csv')
        filepath.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(filepath,sep=',', index=False)

        print('Đã xuất file thành công')

    def get_A(self):
        sql = '''
            WITH sub AS
                    (
                     SELECT st.`Code`, st.`FullName`, st.`Birthday`, 
                            CASE
                                WHEN st.`sex` = 0 THEN "Nữ"
                                ELSE "Nam" 
                            END AS "Sex", 
                                st.`Address`, st.`Phone`, st.`Email`, su.`Name`,round(((sc.`score1` + sc.`score2`*2)/3),2) as `Finalscore`
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
                    WHERE `Finalscore` <= 100 AND `Finalscore` >= 90
        '''
        result = self.__dbProvider.get(sql) #Type: List <tuple>
        
        #Chuyển thành dataframe
        df = pd.DataFrame(result, columns = ["Code", "Fullname", "Birthday", "Sex", "Address", "Phone", "Email", "Subjectname", "Finalscore", "Rank"])

        #Export to csv
        from pathlib import Path  
        filepath = Path('out\out_A.csv')
        filepath.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(filepath,sep=',', index=False)

        print('Đã xuất file thành công')

    def get_B(self):
        sql = '''
           WITH sub AS
                    (
                     SELECT st.`Code`, st.`FullName`, st.`Birthday`, 
                            CASE
                                WHEN st.`sex` = 0 THEN "Nữ"
                                ELSE "Nam" 
                            END AS "Sex", 
                                st.`Address`, st.`Phone`, st.`Email`, su.`Name`,round(((sc.`score1` + sc.`score2`*2)/3),2) as `Finalscore`
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
                    WHERE `Finalscore` < 90 AND `Finalscore` >= 70
        '''
        result = self.__dbProvider.get(sql) #Type: List <tuple>
        
        #Chuyển thành dataframe
        df = pd.DataFrame(result, columns = ["Code", "Fullname", "Birthday", "Sex", "Address", "Phone", "Email", "Subjectname", "Finalscore", "Rank"])

        #Export to csv
        from pathlib import Path  
        filepath = Path('out\out_B.csv')
        filepath.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(filepath,sep=',', index=False)

        print('Đã xuất file thành công')
    
    def get_C(self):
        sql = '''
            WITH sub AS
                    (
                     SELECT st.`Code`, st.`FullName`, st.`Birthday`, 
                            CASE
                                WHEN st.`sex` = 0 THEN "Nữ"
                                ELSE "Nam" 
                            END AS "Sex", 
                                st.`Address`, st.`Phone`, st.`Email`, su.`Name`,round(((sc.`score1` + sc.`score2`*2)/3),2) as `Finalscore`
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
                    WHERE `Finalscore` < 70 AND `Finalscore` >= 50
        '''
        result = self.__dbProvider.get(sql) #Type: List <tuple>
        
        #Chuyển thành dataframe
        df = pd.DataFrame(result, columns = ["Code", "Fullname", "Birthday", "Sex", "Address", "Phone", "Email", "Subjectname", "Finalscore", "Rank"])

        #Export to csv
        from pathlib import Path  
        filepath = Path('out\out_C.csv')
        filepath.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(filepath,sep=',', index=False)

        print('Đã xuất file thành công')
    
    def get_D(self):
        sql = '''
            WITH sub AS
                    (
                     SELECT st.`Code`, st.`FullName`, st.`Birthday`, 
                            CASE
                                WHEN st.`sex` = 0 THEN "Nữ"
                                ELSE "Nam" 
                            END AS "Sex", 
                                st.`Address`, st.`Phone`, st.`Email`, su.`Name`,round(((sc.`score1` + sc.`score2`*2)/3),2) as `Finalscore`
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
                    WHERE `Finalscore` < 50
        '''
        result = self.__dbProvider.get(sql) #Type: List <tuple>
        
        #Chuyển thành dataframe
        df = pd.DataFrame(result, columns = ["Code", "Fullname", "Birthday", "Sex", "Address", "Phone", "Email", "Subjectname", "Finalscore", "Rank"])

        #Export to csv
        from pathlib import Path  
        filepath = Path('out\out_D.csv')
        filepath.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(filepath,sep=',', index=False)

        print('Đã xuất file thành công')