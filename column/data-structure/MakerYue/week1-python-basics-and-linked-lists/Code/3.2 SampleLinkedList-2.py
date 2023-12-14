# -*- coding: utf-8 -*-
# @Time    : 2023/12/14 15:13
# @Author  : AI悦创
# @FileName: 3.2 SampleLinkedList-2.py
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


l = IntList()
l.first = 5
l.rest = None

l.rest = IntList()
l.rest.first = 10
l.rest.rest = None

l.rest.rest = IntList()
l.rest.rest.first = 15

