#-*- coding:utf-8 -*-

import os
import pandas as pd
import numpy as np

"""
批量将sample_name列的数据强制转换成string类型
"""

def convert(src_data):
    df = pd.read_excel(src_data, keep_default_na=False)
    df[['sample_name']]=df[['sample_name']].astype('str')  # 将sample_name列的数据强制转换成string类型
    return df


if __name__=="__main__":
    path1 = './data(4)/txt_data(2)/'  # 全部源数据文件所在的文件夹路径
    fileList = os.listdir(path1)  # 文件夹下面所有的文件
    for i in range(len(fileList)):
        try:
            src_data = os.path.join(path1, fileList[i])
            df=convert(src_data)
            print(type(df.at[5, 'sample_name']))
            writer = pd.ExcelWriter(src_data, engine='xlsxwriter')
            df.to_excel(writer, index=False)
            writer.save()
            print("第{0}个文件已经转换完毕,一共有{1}个文件".format(i,len(fileList)))
        except Exception as result:
            print("{0}文件有问题".format(fileList[i]))
            continue



    # src_data="./data(4)/txt_data(2)/P_10916_80974775_raw_meta.xlsx"
    # df=convert(src_data)
    # print("================")
    # print(type(df.at[5, 'sample_name']))
    # writer = pd.ExcelWriter(src_data, engine='xlsxwriter')
    # df.to_excel(writer, index=False)
    # writer.save()
    # print(df)
