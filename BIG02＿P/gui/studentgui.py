from utils import clearScreen
from dto import StudentDto
from bll import StudentBLL
from datetime import datetime
import re
from tabulate import tabulate

class StudentGUI:
    def __init__(self):
        self.__stBLL = StudentBLL()

    def insertStudentScreen(self):
        clearScreen()
        try:

            print('*** THÊM MỚI HỌC VIÊN ***')
            # Validate input data
            while True:
                code = input('Mã học viên: ')
                if code == '':
                    print('Không được để trống Mã học viên')
                    continue
                if len(code) != 6:
                    print('Mã học viên phải bao gồm 6 ký tự')
                    continue
                break
            isExists = self.__stBLL.checkExists(code)
            if isExists == True:
                print('Mã học viên đã được sử dụng. Hãy dùng mã khác.')
            else:

                while True:
                    fullName = input('Họ tên: ')
                    if fullName == '':
                        print('Không được để trống Họ tên')
                        continue
                    break
                # Bắt lỗi birthday: ko bỏ trống và lỗi định dạng ngày/tháng/năm
                while True:
                    birthday = input ('Ngày sinh (dd/mm/yyyy): ')
                    if birthday == '':
                        print('Không thể để trống ngày sinh')
                        continue
                    try:
                        d = datetime.strptime(birthday, "%d/%m/%Y")
                    except:
                        print('Hãy nhập đúng định dạng ngày sinh')
                        continue
                    break
                
                # Bắt lỗi cho sex
                while True:
                    sex = input ('Giới tính: (0-nữ; 1-nam): ')
                    if sex == '':
                        print('Không thể để trống giới tính')
                        continue
                    if len(sex) != 1:
                        print('mã học viên phải bao gồm 1 ký tự')
                        continue
                    if sex not in ['0','1']:
                        print('Chỉ có thể nhập 0 hoặc 1')
                        continue
                    break
                
                # Nhập Address
                address = input ('Địa chỉ: ')

                # Bắt lỗi Phone
                while True:
                    phone = input ('SĐT: ')
                    if phone != '': 
                        if phone.isdigit() == False:
                            print('Chỉ được nhập dạng chữ số')
                            continue
                        if len(phone) not in [10,11]:
                            print('Sđt chỉ có độ dài 10-11 ký tự số')
                            continue
                    break

                while True:
                    email = input ('Email: ')
                    if email != '':
                        emailRegex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                        if not re.search(emailRegex, email):
                            print('Nhập đúng định dạng email')
                            continue
                    break

                #Cho dữ liệu nhập từ bàn phím vào túi đựng
                newStudentDto = StudentDto(code, 
                                        fullName, 
                                        birthday,
                                        sex,
                                        address,
                                        phone,
                                        email)
                count = self.__stBLL.insert(newStudentDto)
                if count == 0:
                    print('Thêm học viên thất bại')
                else:
                    print('Đã thêm thành công học viên', fullName)
        except Exception as e:
            print('Lỗi:',e)
        finally:
            print('END')
        
        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
        #Bắt đầu nhập thêm học viên mới
            self.insertStudentScreen()

    def updateStudentScreen(self):
        clearScreen()
        try:

            print('*** CHỈNH SỬA THÔNG TIN HỌC VIÊN ***')
            while True:
                code = input('Mã học viên: ')
                if code == '':
                    print('Không được để trống Mã học viên')
                    continue
                if len(code) != 8:
                    print('Mã học viên phải bao gồm 6 ký tự')
                    continue
                break

            isExists = self.__stBLL.checkExists(code)
            if isExists == False:
                print('Mã học viên không tồn tại trong CSDL.')
            else:
                while True:
                    fullName = input('Họ tên: ')
                    if fullName == '':
                        print('Không được để trống Họ tên')
                        continue
                    break

                # Bắt lỗi birthday: ko bỏ trống và lỗi định dạng ngày/tháng/năm
                while True:
                    birthday = input ('Ngày sinh (dd/mm/yyyy): ')
                    if birthday == '':
                        print('Không thể để trống ngày sinh')
                        continue
                    try:
                        d = datetime.strptime(birthday, "%d/%m/%Y")
                    except:
                        print('Hãy nhập đúng định dạng ngày sinh')
                        continue
                    break
            
                # Bắt lỗi cho sex
                while True:
                    sex = input ('Giới tính: (0-nữ; 1-nam): ')
                    if sex == '':
                        print('Không thể để trống giới tính')
                        continue
                    if len(sex) != 1:
                        print('mã học viên phải bao gồm 1 ký tự')
                        continue
                    if sex not in ['0','1']:
                        print('Chỉ có thể nhập 0 hoặc 1')
                        continue
                    break
            
                # Nhập Address
                address = input ('Địa chỉ: ')

                # Bắt lỗi Phone
                while True:
                    phone = input ('SĐT: ')
                    if phone != '': 
                        if phone.isdigit() == False:
                            print('Chỉ được nhập dạng chữ số')
                            continue
                        if len(phone) not in [10,11]:
                            print('Sđt chỉ có độ dài 10-11 ký tự số')
                            continue
                    break

                while True:
                    email = input ('Email: ')
                    if email != '':
                        emailRegex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                        if not re.search(emailRegex, email):
                            print('Nhập đúng định dạng email')
                            continue
                    break

                # Cho dữ liệu nhận từ bàn phím vào túi đựng
                newStudentDto = StudentDto(code, 
                                        fullName, 
                                        birthday,
                                        sex,
                                        address,
                                        phone,
                                        email)
                count = self.__stBLL.update(newStudentDto)
                if count == 0:
                    print('Chỉnh sửa học viên thất bại')
                else:
                    print('Chỉnh sửa thành công học viên', fullName)
        except Exception as e:
            print('Lỗi:',e)
        finally:
            print('END')
        
        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
        #Bắt đầu sửa học viên khác
            self.updateStudentScreen()


    def deleteStudentScreen(self):
        clearScreen()

        try:
            print('*** XOÁ HỌC VIÊN ***')
            while True:
                code = input('Mã học viên: ')
                if code == '':
                    print('Không được để trống Mã học viên')
                    continue
                if len(code) != 6:
                    print('Mã học viên phải bao gồm 6 ký tự')
                    continue
                break

            isExists = self.__stBLL.checkExists(code)
            if isExists == False:
                print('Mã học viên không tại để thực hiện xoá.')
            else:
                # Remove student by ID
                count = self.__stBLL.delete(code)
                if count == 0:
                    print('Đã xoá Học viên thất bại')
                else:
                    print('Đã xoá Học viên có mã:', code)
        except Exception as e:
            print('Lỗi:',e)
        finally:
            print('END')

        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
            # Bắt đầu Xoá lại từ đầu
            self.deleteStudentScreen()

    def searchStudentScreen(self):
        # Ban đầu cứ in tất cả học viên
        allStudents = self.__stBLL.get()
        self.printStudents(allStudents)

        while True:
            # Lọc các học viên theo nội dung
            text = input('Nhập nội dung tìm kiếm: ')
            if text == '':
                self.printStudents(allStudents)
            else:
                studentsFiltered = self.__stBLL.search(text)
                self.printStudents(studentsFiltered)

            ans = input('Nhập y/Y để tiếp tục: ')
            if ans.lower() != 'y':
                break

    def printStudents(self, students: list):
        clearScreen()
        table = []
        for st in students:
            sex = 'N/A'
            if st.Sex == 0:
                sex = 'Nữ'
            elif st.Sex == 1:
                sex = 'Nam'
            table.append([st.Code, st.FullName, st.Birthday, sex, st.Address, st.Phone, st.Email])
        print(tabulate(table, headers=["Student Code","FullName","Birthday", "Sex", "Address", "Phone", "Email"], tablefmt='orgtbl'))