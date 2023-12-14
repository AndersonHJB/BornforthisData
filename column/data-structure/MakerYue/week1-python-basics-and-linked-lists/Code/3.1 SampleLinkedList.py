# -*- coding: utf-8 -*-
# @Time    : 2023/12/14 15:13
# @Author  : AI悦创
# @FileName: 3.1 SampleLinkedList.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# Created by Bornforthis.
class IntList(object):
    def __init__(self):
        """
        first:存自己本身的数据
        rest:存下一个节点，也就下一个节点是谁
        """
        self.first = None
        self.rest = None


l1 = IntList()
l1.first = 5

l2 = IntList()
l2.first = 10

l3 = IntList()
l3.first = 15
