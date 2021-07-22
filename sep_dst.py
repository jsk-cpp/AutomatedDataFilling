#-*- coding = utf-8 -*-

import pandas as pd
import os

"""
将目标文件Supplemental_Dataset_1(3).xlsx拆分成一个个小的文件，
相同项目号的数据在一个文件P_77_.xlsx
"""

data = pd.read_excel('./data(3)/Supplemental_Dataset_1(3).xlsx',keep_default_na=False)
data_list = list(data['Proj'].drop_duplicates())  # 去重处理
longth = len(data_list)
# print(data_list)
# print(longth)
path = './data(3)/SplitExcel(2)/'  # 将拆分的Excel文件保存到此目录下
if not os.path.exists(path):  # 当前文件夹下是否有此文件夹
    os.mkdir(path)  # 创建此文件夹
# count = 0
for item in data_list:  # 遍历Proj列表，按照名字将目的文件分成一个个小的Excel
    data_select = data[data['Proj']==item]  # 选出Proj列相同的值为一组组成DataFrame
    file_name=item+'_.xlsx'
    currentdir=os.path.join(path, file_name)
    data_select.to_excel(currentdir,index=False)
