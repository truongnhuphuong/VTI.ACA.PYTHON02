'''Tổng hợn functions tiện ích hỗ trợ cho toàn dự án'''
import os

#Hàm in Menu
def printMenu(funcs: list):
    for func in funcs:
        print(func)

#Hàm giúp clear màn hình phía trên
def clearScreen():
    #cls (win) hoặc clear (mac/linux)
    os.system('cls||clear')

