from dto.scoredto import ScoretDto
from utils import clearScreen
from dto import ScoretDto
from bll import StudentBLL,SubjectBLL, ScoreBLL
from tabulate import tabulate

class ScoreGUI:
    def __init__(self):
        self.__scBLL = ScoreBLL()
        self.__suBLL = SubjectBLL()
        self.__stBLL = StudentBLL()
    
    def insertScoreScreen(self):
        clearScreen()
        try:
            print('*** THÊM MỚI ĐIỂM ***')
            # Validate input data
            while True:
                stcode = input('Mã học viên: ')
                if stcode == '':
                    print('Không được để trống mã học viên')
                    continue
                if len(stcode) != 6:
                    print('Mã học viên phải bao gồm 6 ký tự')
                    continue
                #Check sự tồn tại của stcode trong subject table
                isExists = self.__stBLL.checkExists(stcode)
                if isExists == False:
                    print('Mã học viên không tồn tại trong CSDL. Hãy nhập mã khác')
                    continue
                break
            while True:
                sucode = input('Mã môn học: ')
                if sucode == '':
                    print('Không được để trống mã môn học')
                    continue
                if len(stcode) != 6:
                    print('Mã môn học phải bao gồm 6 ký tự')
                    continue
                #Check sự tồn tại của sucode trong subject table
                isExists = self.__suBLL.checkExists(sucode)
                if isExists == False:
                    print('Mã môn học không tồn tại trong CSDL. Hãy nhập mã khác')
                    continue
                break

            #Check sự cùng tồn tại của stcode và sucode trong CSDL
            isExists = self.__scBLL.checkExists(stcode,sucode)
            if isExists == True:
                print('Mã học viên và mã môn học đã được sử dụng. Hãy dùng mã khác.')    
            else:
                while True:
                    sc1 = int(input('Điểm thành phần: '))
                    if sc1 == '':
                        print('Không được để trống điểm thành phần')
                        continue
                    if sc1 < 0 or sc1 >100:
                        print('Điểm chỉ nằm trong khoảng từ 0-100')
                        continue
                    break
                while True:
                    sc2 = int(input('Điểm kết thúc: '))
                    if sc2 == '':
                        print('Không được để trống điểm thành phần')
                        continue
                    if sc2 < 0 or sc2 >100:
                        print('Điểm chỉ nằm trong khoảng từ 0-100')
                        continue
                    break

                #Cho dữ liệu nhập từ bàn phím vào túi đựng
                newScoreDto = ScoretDto(stcode, sucode, sc1, sc2)
                count = self.__scBLL.insert(newScoreDto)
                if count == 0:
                    print('Thêm môn học thất bại')
                else:
                    print('Đã thêm thành công điểm của mã học viên', stcode, 'thuộc mã môn',sucode)
        except ValueError as e:
            print('Lỗi:', e)
        except Exception as e2:
            print('Lỗi:', e2)
        finally:
            print('End')
            
        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
        #Bắt đầu nhập thêm môn học mới
            self.insertScoreScreen()


    def updateScoreScreen(self):
        clearScreen()
        try:
            print('*** CHỈNH SỬA THÔNG TIN ĐIỂM ***')
            while True:
                stcode = input('Mã học viên: ')
                if stcode == '':
                    print('Không được để trống mã học viên')
                    continue
                if len(stcode) != 6:
                    print('Mã học viên phải bao gồm 6 ký tự')
                    continue
                break
            while True:
                sucode = input('Mã môn học: ')
                if sucode == '':
                    print('Không được để trống mã môn học')
                    continue
                if len(stcode) != 8:
                    print('Mã môn học phải bao gồm 8 ký tự')
                    continue
                break

            isExists = self.__scBLL.checkExists(stcode, sucode)
            if isExists == False:
                print('Mã học viên và môn học không tồn tại trong CSDL')
            else:
                while True:
                    sc1 = int(input('Điểm thành phần: '))
                    if sc1 == '':
                        print('Không được để trống điểm thành phần')
                        continue
                    if sc1 < 0 or sc1 >100:
                        print('Điểm chỉ nằm trong khoảng từ 0-100')
                        continue
                    break
                while True:
                    sc2 = int(input('Điểm kết thúc: '))
                    if sc2 == '':
                        print('Không được để trống điểm thành phần')
                        continue
                    if sc2 < 0 or sc2 >100:
                        print('Điểm chỉ nằm trong khoảng từ 0-100')
                        continue
                    break

                # Cho dữ liệu nhận từ bàn phím vào túi đựng
                newScorecDto = ScoretDto(stcode, sucode, sc1, sc2)
                count = self.__scBLL.update(newScorecDto)
                if count == 0:
                    print('Chỉnh sửa điểm thất bại')
                else:
                    print('Đã chỉnh sửa thành công điểm của mã học viên', stcode, 'thuộc mã môn',sucode)
        except  ValueError as e1:
            print('Lỗi nhập không đúng kiểu dữ liệu:', e1)
        except Exception as e2:
            print('Lỗi:', e2)
        finally:
            print('END')
        
        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
        #Bắt đầu sửa môn học
            self.updateScoreScreen()

    def searchScoreScreen(self):
        try:
            # Ban đầu cứ in tất cả học viên
            allScores = self.__scBLL.get()
            self.printScores(allScores)

            while True:
                # Lọc các học viên theo nội dung
                text = input('Nhập thông tin tìm kiếm: ')
                if text == '':
                    self.printScores(allScores)
                else:
                    scoresFiltered = self.__scBLL.search(text)
                    self.printScores(scoresFiltered)

                ans = input('Nhập y/Y để tiếp tục: ')
                if ans.lower() != 'y':
                    break
        except Exception as e:
            print('Lỗi:',e)
        finally:
            print('END')

    def printScores(self,scores: list):
        clearScreen()
        table = []
        for sc in scores:
            score1 = int(sc.SC1)
            score2 = int(sc.SC2)
            finalScore = self.getFinalScore(score1, score2)
            table.append([sc.STcode, sc.SUcode, sc.SC1, sc.SC2, finalScore])
        print(tabulate(table, headers=["Student Code","SubjectCode","Score1", "Score2", "Final Score"], tablefmt='orgtbl'))
    
    def getFinalScore(self, sc1:int, sc2:int):
        finalScore = (sc1 + sc2*2)/3
        aliasScore = 'N/A'
        if finalScore >= 90 and finalScore <= 100:
            aliasScore = 'A'
        elif finalScore >= 70:
            aliasScore = 'B'
        elif finalScore >= 50:
            aliasScore = 'C'
        elif finalScore >= 0:
            aliasScore = 'D'
        return aliasScore


    # def exportScoresScreen(self):
    #     pass