# -*- coding: utf-8 -*-
# @Time    : 2023/12/20 16:31
# @Author  : AI悦创
# @FileName: demo.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# Created by Bornforthis.
class IntNode(object):
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev


class DLList(object):
    def __init__(self, x=None):
        self.__sentinel = IntNode(None)  # 使用哨兵节点
        self.__sentinel.next = self.__sentinel
        self.__sentinel.prev = self.__sentinel
        self.__length = 0
        if x is not None:
            self.add_last(x)

    def add_first(self, x):
        new_first = IntNode(x, self.__sentinel.next, self.__sentinel)
        self.__sentinel.next.prev = new_first
        self.__sentinel.next = new_first
        self.__length += 1

    def get_first(self):
        if self.__sentinel.next is not self.__sentinel:
            return self.__sentinel.next.item
        return None

    def add_last(self, x):
        new_end = IntNode(x, self.__sentinel, self.__sentinel.prev)
        self.__sentinel.prev.next = new_end
        self.__sentinel.prev = new_end
        self.__length += 1

    def size(self):
        return self.__length


if __name__ == '__main__':
    l = DLList(15)
    l.add_first(10)
    l.add_first(5)
    print(l.get_first())  # 应该输出5
    l.add_last(20)
    print(l.size())  # 应该输出4
