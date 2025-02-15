# -*- coding: utf-8 -*-
# @Time    : 2023/12/19 17:36
# @Author  : AI悦创
# @FileName: Code1.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# Created by Bornforthis.
class IntNode(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


class SLList(object):
    def __init__(self, x):
        self.__first = IntNode(x, None)
        self.__length = 1

    def add_first(self, x):
        self.__first = IntNode(x, self.__first)
        self.__length += 1

    def get_first(self):
        return self.__first.item

    def add_last(self, x):
        p = self.__first
        while p.next is not None:
            p = p.next
        p.next = IntNode(x, None)
        self.__length += 1

    def __size(self, p):
        """
        循环获取链表长度
        """
        if p.next is None:
            return 1
        else:
            return 1 + self.__size(p.next)

    def size(self):
        return self.__length


if __name__ == '__main__':
    l = SLList(15)
    l.add_first(10)
    l.add_first(5)
    print(l.get_first())
    l.add_last(20)
    print(l.size())
