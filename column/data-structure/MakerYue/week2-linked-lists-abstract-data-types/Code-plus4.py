# -*- coding: utf-8 -*-
# @Time    : 2023/12/21 23:19
# @Author  : AI悦创
# @FileName: Code-plus4.py
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
        self.__sentinel = IntNode(49)
        self.__end = self.__sentinel  # 尾部指针初始化为哨兵节点
        if x is not None:
            self.__sentinel.next = IntNode(item=x, next=None, prev=self.__sentinel)
            self.__end = self.__sentinel.next
            self.__length = 1
        else:
            self.__length = 0

    def add_first(self, x):
        original_first = self.__sentinel.next
        new_first = IntNode(item=x, next=original_first, prev=self.__sentinel)
        self.__sentinel.next = new_first
        if original_first is not None:  # 如果原本的不是空节点，则需要把原本的第一节车厢的 prev 指向新添加的
            original_first.prev = new_first
        else:  # 如果原来链表是空的
            self.__end = new_first
        self.__length += 1

    def get_first(self):
        if self.__sentinel.next is not None:
            return self.__sentinel.next.item
        return None

    def add_last(self, x):
        new_end = IntNode(x, None, self.__end)
        self.__end.next = new_end
        self.__end = new_end
        self.__length += 1

    def size(self):
        return self.__length

    def get_end(self):
        return self.__end.item


if __name__ == '__main__':
    l = DLList(15)
    l.add_first(10)
    l.add_first(5)
    # print(l.get_first())  # 应该输出5
    l.add_last(20)
    l.add_last(211)
    # print(l.size())  # 应该输出4
    print(l.get_end())
