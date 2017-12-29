#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import string
import shutil

#获取指定路径下的所有文件名(带后缀)
def get_filename(file_dir):
    filenames = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            filenames.append(file)
    return filenames

#print(get_filename('/Users/vincent/Desktop/test'))

#格式化单个文件名
def format_filename(filename):
    filename1 = filename.rstrip('.json')
    filename2 = filename1.rstrip(string.digits)
    filename3 = filename2.replace('BL_TV_', '')
    filename4 = filename3.strip()
    return filename4

# file_list = get_filename('/Users/vincent/Desktop/test')
# for i in file_list:
#     print(format_filename(i))

filenamelist = get_filename('/Users/vincent/Desktop/redcode')#获取所有文件名的list
brandlist = []
for brand in filenamelist:
    brandlist.append(format_filename(brand))

brands = set(brandlist)#将格式化后文件名存入set去重
#print(brands)

for foldername in brands:
    if not os.path.exists('/Users/vincent/Desktop/results/' + foldername):
        os.makedirs('/Users/vincent/Desktop/results/' + foldername)#以品牌名为文件夹名称建立文件夹
    else:
        pass
    for filename in filenamelist:
        if foldername == format_filename(filename):#将对应红码文件拷贝放入对应品牌文件夹中
            shutil.copy('/Users/vincent/Desktop/redcode/' + filename , '/Users/vincent/Desktop/results/' + foldername)
