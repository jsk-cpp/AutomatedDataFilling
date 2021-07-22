#encoding: utf-8
from ctypes import *
import time
import win32com.client as win32
import os

# 批量格式转换。文件夹下之前的txt文件虽然改了后缀名后表面变成了xlsx文件，但是其本质仍然不是xlsx文件，需要将其另存为xlsx格式
# 故此函数的作用是将文件夹中的文件全部另存为xlsx格式的文件，这样便能为之后用pandas处理数据做准备

def transform(parent_path,out_path):
    fileList = os.listdir(parent_path)  #文件夹下面所有的文件
    num = len(fileList)
    for i in range(num):
        file_Name = os.path.splitext(fileList[i])   #文件和格式分开
        if file_Name[1] == '.xlsx':
            transfile1 = parent_path+'\\'+fileList[i]  #要转换的excel
            transfile2 = out_path+'\\'+file_Name[0]    #转换出来excel
            excel=win32.gencache.EnsureDispatch('excel.application')
            pro=excel.Workbooks.Open(transfile1)   #打开要转换的excel
            pro.SaveAs(transfile2 + ".xlsx", FileFormat=51)  # 另存为xlsx格式
            pro.Close()
            excel.Application.Quit()

if __name__=='__main__':
    path1=r"E:\研究生\stage1\pro1\data(1)\txt_data"  #待转换文件所在目录
    path2=r"E:\研究生\stage1\pro1\data(1)\txt_data(2)"  #转换文件存放目录
    transform(path1, path2)
