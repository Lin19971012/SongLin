import pandas as pd
import os
import shutil  # 用于移动文件

# 打开表格文件并读取
f = open("G:\classify\land_classify_train\train.txt", "rb")  # 输入表格所在路径+名称
list = pd.read_csv(f)
list["FILE_ID_JPG"] = ".jpg"  # 建立图片名与类别相对应
list["FILE_ID1"] = list["FILE_ID"] + list["FILE_ID_JPG"]  # 建立图片名与类别相对应

# 创建文件夹
for i in range(51):
    os.mkdir(str(i))


# 进行分类
for i in range(0, 51):
    listnew = list[list["CATEGORY_ID"] == i]
    l = listnew["FILE_ID1"].tolist()
    j = str(i)
    for each in l:
        shutil.move(each, j)