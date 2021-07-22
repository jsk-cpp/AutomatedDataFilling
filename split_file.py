import os
import shutil

def splitFile(src,dst1,dst2):
    """
    将文件夹中的.txt文件和.gz文件分别放到不同的文件夹
    :param src: 原数据存放的文件夹
    :param dst1: 存放.txt文件的文件夹
    :param dst2: 存放.gz文件的文件夹
    :return: None
    """

    # 将两种文件名分别放到不同的列表
    txt=[]
    gz=[]
    for f in os.listdir(src):  # os.listdir:用于返回一个文件名和目录名组成的列表
        if f.endswith(".txt"):  # endswith:判断字符串是否以指定字符或子字符串结尾
            txt.append(f)
        elif f.endswith(".gz"):
            gz.append(f)

    # 创建文件夹
    if not os.path.isdir(dst1):
        os.makedirs(dst1)
    if not os.path.isdir(dst2):
        os.makedirs(dst2)

    # 将文件拷贝到目标文件夹
    for t in txt:
        _txt=os.path.join(src,t)  # os.path.join:路径名与文件名合并,合并的一定是字符串格式
        shutil.copy(_txt,dst1)  # shutil.copy:将文件拷贝到目标文件夹中
    for g in gz:
        _gz=os.path.join(src,g)
        shutil.copy(_gz,dst2)

    print("finish")

if __name__ == '__main__':
    base_filename=".\data(1)"
    src=os.path.join(base_filename,"raw_data")
    dst1=os.path.join(base_filename,"txt_data")
    dst2=os.path.join(base_filename,"gz_data")

    splitFile(src,dst1,dst2)
