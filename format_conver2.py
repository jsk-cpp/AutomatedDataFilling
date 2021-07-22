# file_affilication = open('Affiliations.txt','r')
import xlwt
import os
import sys


def txt_xls(filename, xlsname):
    try:
        f = open(filename)
        xls = xlwt.Workbook()
        # 生成excel的方法，声明excel
        sheet = xls.add_sheet('sheet', cell_overwrite_ok=True)
        x = 0  # 在excel开始写的位置（y）

        while True:  # 循环读取文本里面的内容
            line = f.readline()  # 一行一行的读
            if not line:  # 如果没有内容，则退出循环
                break
            for i in range(len(line.split('\t'))):  # \t即tab健分隔
                item = line.split('\t')[i]
                sheet.write(x, i, item)  # x单元格经度，i单元格纬度
            x += 1  # 另起一行
        f.close()
        xls.save(xlsname)  # 保存为xls文件
    except:
        raise


if __name__ == '__main__':
    filename = './data(4)/P_101_9743352_raw_meta.txt'
    xlsname = './data(4)/P_101_9743352_raw_meta.xlsx'
    txt_xls(filename, xlsname)