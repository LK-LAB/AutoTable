# Utils for Data which in Magpie

from excel_functions import loading

def element_info_loader(element_list_file):
    # 이 함수의 본 목적은 Magpie table의 데이터를 AutoTable(또는 Mathematica)의 데이터에 추가하는 용도
    # Magpie가 아니더라도 형식만 맞춘다면 사용 가능
    # 원소기호로 나열된 원소 목록들에 대해서만 작동한다
    user_element_list = open(element_list_file, 'r', encoding='UTF8') # 원소 목록 파일의 내용을 가져온다
    user_element_temp = user_element_list.readlines() # 전체 내용을 읽는다
    all_element_list = loading()
    trans_element_list = [] # 빈 리스트를 정의한다
    for element in all_element_list:
        tempelement = open(element, 'r', encoding='UTF8')
        element_id = tempelement.readline() # AutoTable 원소 데이터에서 첫 줄, 즉 원소기호만 읽어온다.
        for i in range(0,112): # Magpie는 주기율표 1번부터 112번까지의 원소들의 데이터를 포함
            if element_id == user_element_temp[i]:
                trans_element_list.append('%s.txt' %element) # AutoTable에서 사용할 수 있게끔 '~.txt' 형식으로 리스트에 추가한다
                break # 추가하고 나면 그 뒤로는 비교할 필요가 없으므로 반복문 탈출
    return trans_element_list # 만들어진 원소 목록 반환

def add_dictionary(feature):
    # 딕셔너리 목록에 새로운 특징 추가
    f_dict = open('dictionary.py', 'r', encoding='UTF8')
    tempdata = f_dict.readlines()
    length = len(tempdata)
    temp = tempdata[length - 2].split(":")
    tempdata[length - 1] = feature + ":" + str(int(temp[1]) + 1) + '\r\n' + '}'
    f_dict = open('dictionary.py', 'w', encoding='UTF8')
    f_dict.writelines(tempdata)
    f_dict.close()
    print('%s : %s'%(feature, str(int(temp[1]) + 1)))


def add_data_line(element, feature_data):
    # 기존 데이터 파일에 새로운 특징 데이터 추가(미완)
    f_element = open('dictionary.py', 'r', encoding='UTF8')
    tempdata = f_element.readlines()
    length = len(tempdata)
    tempdata[length - 1] += '\r\n' + feature_data
    print('%s : %s'%(feature, str(int(temp[1]) + 1)))


def add_feature(element_file, feature_name, feature_data_file):
    f_feature = open(feature_data_file, 'r', encoding='UTF8') # 특징들의 값들이 나열된 파일의 내용을 가져온다
    f_element = open(element_file, 'r', encoding='UTF8')
    (element_list, feature_data) = (f_element.readlines(), f_feature.readlines())  # 파일의 내용을 읽어온다
    all_element_list = loading() # 전체 원소들에 대한 데이터 파일들의 목록을 가져온다
    
    for element in all_element_list:
        tempelement = open(element, 'rt', encoding='UTF8')
        tempdata = tempelement.readlines()