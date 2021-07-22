# 导入需要的库
import os
import pandas as pd
import shutil
import stat


def copyFiles(data,sourceDir,targetDir):
    data_list = list(data['Proj'].drop_duplicates())  # 去重处理
    for item in data_list:
        file_name=item+'_.xlsx'
        sourceFile = os.path.join(sourceDir, file_name)
        targetFile = os.path.join(targetDir,file_name)

        #如果是文件则处理
        if os.path.isfile(sourceFile):
            #如果目的路径不存在该文件就创建空文件,并保持目录层级结构
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            #如果目的路径里面不存在某个文件或者存在那个同名文件但是文件有残缺，则复制，否则跳过
            if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                open(targetFile, "wb").write(open(sourceFile, "rb").read())
                print( targetFile+" copy succeeded")

        #如果是文件夹则递归
        if os.path.isdir(sourceFile):
            copyFiles(sourceFile, targetFile)

if  __name__ =="__main__":
    sourceDir='./data(3)/SplitExcel(2)/'
    targetDir='./data(3)/target(2)/'
    data_source='./data(3)/positive_20210518.xlsx'
    data = pd.read_excel(data_source, keep_default_na=False)
    copyFiles(data,sourceDir,targetDir)
