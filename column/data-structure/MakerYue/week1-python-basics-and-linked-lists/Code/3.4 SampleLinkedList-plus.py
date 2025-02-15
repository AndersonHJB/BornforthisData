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

    def size(self):
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

    def get_index(self, index):
        '''第二种查询方法'''
        if index < 0:
            return -1
        node = self
        for _ in range(index):
            node = node.rest
        return node.first


# l1 = IntList(5, None)
# l2 = IntList(10, l1)
# l3 = IntList(15, l2)


l = IntList(5, None)
l = IntList(10, l)
l = IntList(15, l)
# print(l.size())
# print(l.get_length(l))
# print(l.iterative_size())
# print(l.get_index(0))
# print(l.get_index(1))
# print(l.get_index(2))

print(l.get(0))
print(l.get(1))
print(l.get(2))