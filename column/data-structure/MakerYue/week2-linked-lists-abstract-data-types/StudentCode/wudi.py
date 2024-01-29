# -*- coding: utf-8 -*-
# @Time    : 2024/1/3 15:26
# @Author  : AI悦创
# @FileName: wudi.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# Created by Bornforthis.
class IntNode(object):  # 功能就是生产车厢 不需要连接
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev


class Sllist(object):
    def __init__(self, x=None):
        self.__sentinel = IntNode(None)  # 头部加一个哨兵 设置的值是摆设 所以是None
        self.__end_sentienl = IntNode(None)
        self.__sentinel.next = self.__end_sentienl  # 加上二者的关系
        self.__end_sentienl.prev = self.__sentinel  # 双向链表一定要加上二者的关系
        # self.__end=self.__end_sentienl 不需要这个是因为有了尾部哨兵
        if x is None:  # 如果没有这个if句 当列表为空的时候 会影响操作
            self.__length = 0
        else:
            self.__sentinel.next = IntNode(x, None, self.__sentinel)
            self.__end_sentienl.prev = self.__sentinel.next
            self.__length = 1

    def add_frist(self, x):
        original_first = self.__sentinel.next
        new_first = IntNode(x, original_first, self.__sentinel)
        self.__sentinel.next = new_first
        if original_first is not None:
            original_first.prev = new_first
        else:
            self.__end = new_first  # 因为要跟踪最后一个元素
        self.__length += 1

    def remove_first(self):
        if self.__sentinel.next is not None:
            removed_item = self.__sentinel.next.item
            self.__sentinel.next = self.__sentinel.next.next
            if self.__sentinel.next is not None:
                self.__sentinel.next.prev = self.__sentinel
            else:
                self.__end = self.__sentinel
            self.__length -= 1
            return removed_item
        return None

    def get_first(self):
        if self.__sentinel.next != self.__end_sentienl is not None:
            return self.__sentinel.next.item
        return None

    def add_last(self, x):
        original_node = self.__end_sentienl.prev
        new_node = IntNode(x, self.__end_sentienl, original_node)
        original_node.next = new_node
        self.__end_sentienl.prev = new_node  # 第二层关系
        self.__length += 1

    def remove_last(self):
        if self.__sentinel.next == self.__end_sentienl:
            return None
        else:
            removed_item = self.__end_sentienl.prev.item
            new_last = self.__end_sentienl.prev.prev
            if new_last.item is not None:
                new_last.next = self.__end_sentienl
                self.__end_sentienl.prev = new_last
                self.__length -= 1
            else:
                self.__sentinel.next = self.__end_sentienl
                self.__end_sentienl.prev = self.__sentinel
                self.__length -= 1

    def index_(self):
        if self.__sentinel.next == self.__end_sentienl:
            return None
        else:
            current = self.__sentinel.next
            index = 0
            while current.item is not None:
                current = current.next
                index += 1
            return index

    def get_at(self, index):
        if self.__sentinel.next == self.__end_sentienl:
            return None
        else:
            i = self.index_()
            if index > i:
                return None
            else:
                current = self.__sentinel.next
                while index > 0:
                    current = current.next
                    index -= 1
                return current.item

    def remove_at(self, index):
        if self.__sentinel.next == self.__end_sentienl:
            return None
        else:
            remove_item = self.get_at(index)
            # if remove_item is None:
            #     return None
            # else:
            #     pass
                # current = self.__sentinel.next
                # print(current)
                # while current.item != remove_item:
                #     current = current.next
                # current.prev.next = current.next
                # current.next.prev = current.prev
                # self.__length -= 1
                # return remove_item

    def size(self):
        return self.__length


l = Sllist(10)
l.add_frist(2)
l.add_frist(3)
l.remove_at(0)
# print(l.get_at(1))
# print(l.size())
