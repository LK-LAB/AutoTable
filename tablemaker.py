import openpyxl as pyxl
import excel_functions
from dictionary import features

filename = input("만들 표의 이름 : ")
inputfeature = input("표에 넣을 특징들을 나열하세요 : ")
featurelist = inputfeature.split()

elementlist = excel_functions.loading()
excel_functions.auto_table(filename, elementlist, featurelist)

print("종료합니다")
