# -*- coding: utf-8 -*-
# @Time    : 2023/12/19 22:37
# @Author  : AI悦创
# @FileName: Code4-plus1.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# Created by Bornforthis.
class IntNode(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


class SLList(object):
    def __init__(self, x=None):
        self.__sentinel = IntNode(49, None)
        self.__end = self.__sentinel  # 尾部指针初始化为哨兵节点
        if x is not None:
            # self.__end.next = IntNode(x, None)
            self.__sentinel.next = IntNode(x, None)  # 和上面等价
            self.__end = self.__end.next
            # self.__end = self.__sentinel.next  # 和上面等价
            self.__length = 1
        else:
            self.__length = 0

    def add_first(self, x):
        original_first = self.__sentinel.next
        new_first = IntNode(x, original_first)
        self.__sentinel.next = new_first
        if self.__end == self.__sentinel:  # 如果链表为空，则更新尾部指针
            self.__end = new_first
        self.__length += 1

    def get_first(self):
        if self.__sentinel.next is not None:
            return self.__sentinel.next.item
        return None

    def add_last(self, x):
        new_end = IntNode(x, None)
        self.__end.next = new_end
        self.__end = new_end
        self.__length += 1

    def size(self):
        return self.__length


if __name__ == '__main__':
    l = SLList(15)
    l.add_first(10)
    l.add_first(5)
    print(l.get_first())  # 应该输出5
    l.add_last(20)
    print(l.size())  # 应该输出4
