'''Đọc ghi dữ liệu'''
import mysql.connector

class DBProvider:
    def __init__(self):
        # host="localhost",
        # user="root",
        # passwd="root",
        # db = "big02db"
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = 'root'
        self.db = 'big02db'
        self.conn = None
        self.curr = None
        self.__createDBIfNotExists()
    
    #Tạo DB if not exist
    def __createDBIfNotExists(self):
        sql = f'CREATE DATABASE IF NOT EXISTS {self.db}'
        conn = mysql.connector.connect(host=self.host,
                                            user=self.user,
                                            passwd=self.passwd)
        curr = conn.cursor()
        curr.execute(sql)
        conn.close()
    
    #Kết nối CSDL
    def connect(self):
        self.conn = mysql.connector.connect(host=self.host,
                                            user=self.user,
                                            passwd=self.passwd,
                                            db = self.db)
        self.curr = self.conn.cursor()
    
    #Ngắt kết nối CSDL
    def close(self):
        if self.conn is not None and self.curr is not None:
            self.conn.close()
            self.conn = None
            self.curr = None

    #Thực thi câu lệnh SQL dạng chỉnh sửa dữ liệu
    def exec(self, sql: str, *params):
        rowCount = 0
        self.connect()
        try:
            self.curr.execute(sql, *params)
            self.conn.commit()
            rowCount = self.curr.rowcount #Số lượng bản ghi bị thay đổi trong CSDL
        except Exception as e:
            print('Lỗi cú pháp SQL:', e)
        finally:
            self.close()
        return rowCount
    
    #Thực thi câu lệnh SQL, dạng truy vấn dữ liệu (nhiều bản ghi)
    def get(self, sql: str, *params):
        result = []
        try:
            self.connect()

            self.curr.execute(sql, *params)
            result = [row for row in self.curr.fetchall()] #dùng lặp for lấy phần tử vào tạo thành list
        except Exception as e:
            print('Lỗi cú pháp SQL:', e)
        finally:
            self.close()
        return result
    
    #Thực thi câu lệnh SQL, dạng truy vấn dữ liệu (1 bản ghi)
    def getOne(self, sql: str, *params):
        try:
            self.connect()
            self.curr.execute(sql, *params)
            result = self.curr.fetchone()  # result as a row
        except Exception as e:
            print('Lỗi cú pháp SQL:', e)
        finally:
            self.close()

        self.close()
        return result