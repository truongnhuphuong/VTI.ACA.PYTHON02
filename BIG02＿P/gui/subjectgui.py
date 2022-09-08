from utils import clearScreen
from dto import SubjectDto
from bll import SubjectBLL
from tabulate import tabulate

class SubjectGUI:
    def __init__(self):
        self.__suBLL = SubjectBLL()
    
    def insertSubjectScreen(self):
        clearScreen()

        try:
            print('*** THÊM MỚI MÔN HỌC ***')
            # Validate input data
            while True:
                code = input('Mã môn học: ')
                if code == '':
                    print('Không được để trống Mã môn học')
                    continue
                if len(code) != 6:
                    print('Mã môn học phải bao gồm 6 ký tự')
                    continue
                break
            isExists = self.__suBLL.checkExists(code)
            if isExists == True:
                print('Mã môn học đã được sử dụng. Hãy dùng mã khác.')
            else:

                while True:
                    name = input('Tên môn học: ')
                    if name == '':
                        print('Không được để trống tên môn học')
                        continue
                    break

                #Cho dữ liệu nhập từ bàn phím vào túi đựng
                newSubjectDto = SubjectDto(code, name)
                count = self.__suBLL.insert(newSubjectDto)
                if count == 0:
                    print('Thêm môn học thất bại')
                else:
                    print('Đã thêm thành công môn học', name)
        except Exception as e:
            print('Lỗi:',e)
        finally:
            print('END')
        
        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
        #Bắt đầu nhập thêm môn học mới
            self.insertSubjectScreen()
    
    def updateSubjectScreen(self):
        clearScreen()

        try:
            print('*** CHỈNH SỬA THÔNG TIN MÔN HỌC ***')
            while True:
                code = input('Mã môn học: ')
                if code == '':
                    print('Không được để trống Mã môn học')
                    continue
                if len(code) != 6:
                    print('Mã học viên phải bao gồm 6 ký tự')
                    continue
                break

            isExists = self.__suBLL.checkExists(code)
            if isExists == False:
                print('Mã môn học không tồn tại trong CSDL.')
            else:
                while True:
                    name = input('Tên môn học: ')
                    if name == '':
                        print('Không được để trống tên môn học')
                        continue
                    break

                # Cho dữ liệu nhận từ bàn phím vào túi đựng
                newSubjetcDto = SubjectDto(code, name)
                count = self.__suBLL.update(newSubjetcDto)
                if count == 0:
                    print('Chỉnh sửa môn học thất bại')
                else:
                    print('Chỉnh sửa thành công môn học', name)
        except Exception as e:
            print('Lỗi:',e)
        finally:
            print('END')
        
        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
        #Bắt đầu sửa môn học
            self.updateSubjectScreen()
    
    def deleteSubjectScreen(self):
        clearScreen()
        try:
            print('*** XOÁ MÔN HỌC ***')
            while True:
                code = input('Mã môn học: ')
                if code == '':
                    print('Không được để trống Mã môn học')
                    continue
                if len(code) != 6:
                    print('Mã học viên phải bao gồm 6 ký tự')
                    continue
                break

            isExists = self.__suBLL.checkExists(code)
            if isExists == False:
                print('Mã môn học không tại để thực hiện xoá.')
            else:
                # Remove student by ID
                count = self.__suBLL.delete(code)
                if count == 0:
                    print('Đã xoá môn học thất bại')
                else:
                    print('Đã xoá môn học có mã:', code)
        except Exception as e:
            print('Lỗi:',e)
        finally:
            print('END')

        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
            # Bắt đầu Xoá lại từ đầu
            self.deleteSubjectScreen()

    def searchSubjectScreen(self):
        try:
            # Ban đầu cứ in tất cả học viên
            allSubjects = self.__suBLL.get()
            self.printSubjects(allSubjects)

            while True:
                # Lọc các học viên theo nội dung
                text = input('Nhập nội dung tìm kiếm: ')
                if text == '':
                    self.printSubjects(allSubjects)
                else:
                    subjectsFiltered = self.__suBLL.search(text)
                    self.printSubjects(subjectsFiltered)

                ans = input('Nhập y/Y để tiếp tục: ')
                if ans.lower() != 'y':
                    break
        except Exception as e:
            print('Lỗi:',e)
        finally:
            print('END')

    def printSubjects(self, subjects: list):
        clearScreen()
        table = []
        # using map()
        for su in subjects:
            table.append([su.Code, su.Name])
           
        print(tabulate(table, headers=["Subject Code","Subject Name"], tablefmt='orgtbl'))