#-*- coding = utf-8 -*-

import pandas as pd
import os


if __name__=='__main__':
    sourceDir='./data(3)/target(3)/'
    dst_file='./data(3)/test.xlsx'
    dst = pd.read_excel(dst_file,keep_default_na=False)
    data_list = list(dst['Proj'].drop_duplicates())  # 去重处理
    longth = len(data_list)
    # print(longth)
    # dst = pd.read_excel(dst_file, keep_default_na=False)
    count=0
    for item in data_list:
        file_name=item+'_.xlsx'
        source_data=os.path.join(sourceDir, file_name)
        src=pd.read_excel(source_data,keep_default_na=False)
        try:
            for s in src.index[0:]:  # 遍历单个源文件中的数据
                ID=src.at[s,'ID']
                for d in dst.index[0:]:
                    _ID=dst.at[d,'ID']
                    if ID==_ID:
                        dst.at[d, 'Latitude'] = src.at[s, 'Latitude']
                        dst.at[d, 'Longitude'] = src.at[s, 'Longitude']
        except Exception as result:
            print("{0}文件有问题".format(file_name))
            continue
        count+=1
        print('The outermost loop has been traversed for {0} times,a total of {1} times'.format(count,longth))

    # 用XlsxWriter创建一个pandas的excel表格
    writer = pd.ExcelWriter(dst_file, engine='xlsxwriter')
    # 把DataFrame转换成XlsxWriter Excel对象
    dst.to_excel(writer, sheet_name='positive', index=False)
    # workbook = writer.book
    # worksheet = writer.sheets['positive']
    writer.save()
    print("finished!")