# -*- coding: utf-8 -*-
# @Time    : 2023/12/20 10:54
# @Author  : AI悦创
# @FileName: ExcelWrite.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# Created by Bornforthis.
# xlsx
# xl: xlwt xls + write => xlwt
# 安装命令：pip install xlwt
# 制作出：常规操作 or 创建 Excel 的流程：
import xlwt

wb = xlwt.Workbook()  # 新建一个 Workbook 对象

sheet = wb.add_sheet("第一个 sheet 表")

head_data = ['姓名', '地址', '手机号', '城市']
for head in head_data:
    sheet.write(0, head_data.index(head), head)
    # sheet.write(行, 列, 写入数据)
"""
TODO: 三种写法
for head in head_data:
    sheet.write(0, head_data.index(head), head)
    
for index, head in enumerate(head_data):
    # print(head)
    sheet.write(0, index, head)
    # sheet.write(行, 列, 插入的数据)

i = 0
for head in head_data:
    sheet.write(0, i, head)
    i += 1
    
for index in range(len(head_data)):
    sheet.write(0, index, head_data[index])
"""
wb.save('虚假用户数据.xls')


