# -*- coding: utf-8 -*-
# @Time    : 2023/12/15 12:16
# @Author  : AI悦创
# @FileName: demo.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# Created by Bornforthis.
# filename: compare.py
class IntList(object):
    def __init__(self, f, r):
        """
        first:存自己本身的数据
        rest:存下一个节点，也就下一个节点是谁
        """
        self.first = f
        self.rest = r

    def size(self):
        """方法一"""
        # l == self 抽象理解
        if self.rest is None:
            return 1
        else:
            return 1 + self.rest.size()

    def get_length(self, linked):
        """方法二"""
        length = 0
        while linked:
            length += 1
            linked = linked.rest
        return length

    def iterative_size(self):
        # l == self 抽象理解
        p = self
        total_size = 0
        while p is not None:
            total_size += 1
            p = p.rest
        return total_size

    def get(self, index):
        if index == 0:
            return self.first
        else:
            return self.rest.get(index - 1)


l1 = IntList(5, None)
l2 = IntList(10, l1)
l3 = IntList(15, l2)
# print(l1.first)
# print(l2.first)
# print(l3.first)
print(l3.get(0))
print(l3.get(1))
print(l3.get(2))
