# -*- coding: utf-8 -*-
# @Time    : 2023/12/14 15:13
# @Author  : AI悦创
# @FileName: 3.4 SampleLinkedList-plus.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# Created by Bornforthis.
class IntList(object):
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest


l1 = IntList(5, None)
l2 = IntList(10, l1)
l3 = IntList(15, l2)


