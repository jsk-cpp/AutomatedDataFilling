import xlrd
import xlsxwriter
import os

path = "./data(3)/SplitExcel/"

def get_allxls():  # 获取excel文件列表
    all_xls = []
    for f in os.listdir(path):
        f_name = path + f
        all_xls.append(f_name)
    return all_xls

def open_xls(file):  # 打开一个excel
    fh = xlrd.open_workbook(file)
    return fh

def getsheet(fh):  # 获取excel表中的所有sheet
    return fh.sheets()

def getnrows(fh, sheet):  # 获取sheet表中的行数
    table = fh.sheets()[sheet]
    return table.nrows

def getFilect(file, shnum):  # 读取文件内容并返回内容
    fh = open_xls(file)
    table = fh.sheets()[shnum]
    num = table.nrows
    for row in range(1,num):
        rdata = table.row_values(row)
        datavalue.append(rdata)
    return datavalue

def getshnum(fh):  # 获取sheet表的个数
    x = 0
    sh = getsheet(fh)
    for sheet in sh:
        x += 1
    return x

if __name__ == '__main__':
    allxls = get_allxls()  # 定义要合并的excel文件列表
    datavalue = []
    for fl in allxls:  # 存储所有读取的结果
        fh = open_xls(fl)
        x = getshnum(fh)
        for shnum in range(x):
            print("正在读取文件：" + str(fl) + "的第" + str(shnum) + "个sheet表的内容...")
            rvalue = getFilect(fl, shnum)
    endfile = "./data(3)/Supplemental_Dataset_1(4).xlsx"  # 合并后的文件
    wb1 = xlsxwriter.Workbook(endfile)

    ws = wb1.add_worksheet()
    for a in range(len(rvalue)):
        for b in range(len(rvalue[a])):
            c = rvalue[a][b]
            ws.write(a, b, c)
    wb1.close()
    print("excel合并完成")
