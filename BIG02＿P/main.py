from utils import printMenu, clearScreen
from gui import StudentGUI, SubjectGUI, ScoreGUI, convertCSV



class MainGUI:
    def __init__(self):
        self.__stGUI = StudentGUI()
        self.__suGUI = SubjectGUI() 
        self.__scGUI = ScoreGUI()
        self.__csv =  convertCSV()
    
    def mainMenuScreen(self):
        # Xoá trắng màn hình
        clearScreen()

        print('*** MENU CHƯƠNG TRÌNH QUẢN LÝ HỌC VIÊN ***')
        funcs = [
            '[1] Quản lý Học viên',
            '[2] Quản lý Môn học',
            '[3] Quản lý Điểm thi',
            '[4] Xuất file CSV',
            '[0] Thoát'
        ]
        printMenu(funcs)

        cmd = ''
        while cmd not in ['1', '2', '3', '4', '0']:
            cmd = input('Chọn chức năng: ')

        if cmd == '1':
            # Hiển thị màn hình QL Học viên
            self.studentMenuScreen()
        elif cmd == '2':
        # Hiển thị màn hình quản lý môn học
            self.subjectMenuScreen()
        elif cmd == '3':
            self.scoreMenuScreen()
        elif cmd == '4':
            self.convertCSVScreen()
        elif cmd == '0':
            exit()

    def studentMenuScreen(self):
        # Xoá trắng màn hình
        clearScreen()

        print('*** QUẢN LÝ HỌC VIÊN ***')
        funcs = [
            '[1] Thêm',
            '[2] Sửa',
            '[3] Xoá',
            '[4] Tìm kiếm',
            '[0] Quay lại'
        ]
        printMenu(funcs)

        cmd = ''
        while cmd not in ['1', '2', '3', '4', '0']:
            cmd = input('Chọn chức năng: ')

        if cmd == '1':
            self.__stGUI.insertStudentScreen()
            # Nhập xong thì quay lại màn hình studentMenuScreen
            self.studentMenuScreen()
        elif cmd == '2':
            self.__stGUI.updateStudentScreen()
            # Sửa xong thì quay lại màn hình studentMenuScreen
            self.studentMenuScreen()
        elif cmd == '3':
            self.__stGUI.deleteStudentScreen()
            # Xoá xong thì quay lại màn hình studentMenuScreen
            self.studentMenuScreen()
        elif cmd == '4':
            self.__stGUI.searchStudentScreen()
            # Tìm kiếm xong thì quay lại màn hình studentMenuScreen
            self.studentMenuScreen()
        elif cmd == '0':
            # Quay lại màn hình Menu chính
            self.mainMenuScreen()
    
    def subjectMenuScreen(self):
        # Xoá trắng màn hình
        clearScreen()

        print('*** QUẢN LÝ MÔN HỌC ***')
        funcs = [
            '[1] Thêm',
            '[2] Sửa',
            '[3] Xoá',
            '[4] Tìm kiếm',
            '[0] Quay lại'
        ]
        printMenu(funcs)

        cmd = ''
        while cmd not in ['1', '2', '3', '4', '0']:
            cmd = input('Chọn chức năng: ')

        if cmd == '1':
            self.__suGUI.insertSubjectScreen()
            # Nhập xong thì quay lại màn hình subjectMenuScreen
            self.subjectMenuScreen()
        elif cmd == '2':
            self.__suGUI.updateSubjectScreen()
            # Sửa xong thì quay lại màn hình subjectMenuScreen
            self.subjectMenuScreen()
        elif cmd == '3':
            self.__suGUI.deleteSubjectScreen()
            # Xoá xong thì quay lại màn hình subjectMenuScreen
            self.subjectMenuScreen()
        elif cmd == '4':
            self.__suGUI.searchSubjectScreen()
            # Tìm kiếm xong thì quay lại màn hình subjectMenuScreen
            self.subjectMenuScreen()
        elif cmd == '0':
            # Quay lại màn hình Menu chính
            self.mainMenuScreen()

    def scoreMenuScreen(self):
        # Xoá trắng màn hình
        clearScreen()

        print('*** QUẢN LÝ ĐIỂM ***')
        funcs = [
            '[1] Thêm',
            '[2] Sửa',
            '[3] Tra cứu',
            '[0] Quay lại'
        ]
        printMenu(funcs)

        cmd = ''
        while cmd not in ['1', '2', '3', '0']:
            cmd = input('Chọn chức năng: ')

        if cmd == '1':
            self.__scGUI.insertScoreScreen()
            # Nhập xong thì quay lại màn hình scoreMenuScreen
            self.scoreMenuScreen()
        elif cmd == '2':
            self.__scGUI.updateScoreScreen()
            # Sửa xong thì quay lại màn hình scoreMenuScreen
            self.scoreMenuScreen()
        elif cmd == '3':
            self.__scGUI.searchScoreScreen()
            # Tìm kiếm xong thì quay lại màn hình scoreMenuScreen
            self.scoreMenuScreen()
        elif cmd == '0':
            # Quay lại màn hình Menu chính
            self.mainMenuScreen()

    def convertCSVScreen(self):
         # Xoá trắng màn hình
        clearScreen()

        print('*** XUẤT FILE CSV ***')
        funcs = [
            '[1] Xuất file CSV tất cả các học viên',
            '[2] Xuất file CSV các học viên điểm A',
            '[3] Xuất file CSV các học viên điểm B',
            '[4] Xuất file CSV các học viên điểm C',
            '[5] Xuất file CSV các học viên điểm D',
            '[0] Quay lại'
        ]
        printMenu(funcs)

        cmd = ''
        while cmd not in ['1', '2', '3', '4', '5', '0']:
            cmd = input('Chọn chức năng: ')

        if cmd == '1':
            self.__csv.get_all()
            ans = input('Nhập y/Y để tiếp tục: ')

            if ans.lower() == 'y':
            #Bắt đầu nhập thêm môn học mới
                self.convertCSVScreen()
            else:
                self.mainMenuScreen()

            # Nhập xong thì quay lại màn hình covertCSVScreen
            #self.convertCSVScreen()
        elif cmd == '2':
            self.__csv.get_A()

            ans = input('Nhập y/Y để tiếp tục: ')
            if ans.lower() == 'y':
            #Bắt đầu nhập thêm môn học mới
                self.convertCSVScreen()
            else:
                self.mainMenuScreen()
        elif cmd == '3':
            self.__csv.get_B()

            ans = input('Nhập y/Y để tiếp tục: ')
            if ans.lower() == 'y':
            #Bắt đầu nhập thêm môn học mới
                self.convertCSVScreen()
            else:
                self.mainMenuScreen()

        elif cmd == '4':
            self.__csv.get_C()

            ans = input('Nhập y/Y để tiếp tục: ')
            if ans.lower() == 'y':
            #Bắt đầu nhập thêm môn học mới
                self.convertCSVScreen()
            else:
                self.mainMenuScreen()

        elif cmd == '5':
            self.__csv.get_D()
            ans = input('Nhập y/Y để tiếp tục: ')
            if ans.lower() == 'y':
            #Bắt đầu nhập thêm môn học mới
                self.convertCSVScreen()
            else:
                self.mainMenuScreen()

        elif cmd == '0':
            # Quay lại màn hình Menu chính
            self.mainMenuScreen()

if __name__ == '__main__':
    mainGUI = MainGUI()
    mainGUI.mainMenuScreen()