# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 13:35
# @Author  : AI悦创
# @FileName: DLList.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# Created by Bornforthis.
class IntNode(49, None, None):
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev


class DLList(object):
    def __init__(self, x=None):
        self.__sentinel = IntNode(49, None, None)
        self.__sentinel.next = self.__sentinel
        self.__sentinel.prev = self.__sentinel
        self.__last = self.__sentinel.prev
        if x is None:
            self.__length = 0
        else:
            self.__sentinel.next = IntNode(item=x, next=self.__sentinel, prev=self.__sentinel)
            self.__sentinel.prev = self.__sentinel.next
            self.__length = 1

    def add_first(self, item):
        # self.__sentinel.next = IntNode(item=item, next=self.__sentinel.next, prev=self.__sentinel)
        # self.__sentinel.next.next.prev = self.__sentinel.next

        original_first = self.__sentinel.next
        news_first = IntNode(item, next=None, prev=None)
        news_first.next = original_first
        news_first.prev = self.__sentinel
        self.__sentinel.next = news_first
        original_first.prev = news_first

        self.__length += 1

    def add_last(self, item):
        """在链表的尾部添加数据"""
        new_last = IntNode(item, next=self.__sentinel, prev=self.__last)
        self.__last.next = new_last
        self.__last = new_last
        self.__sentinel.prev = new_last
        self.__length += 1

    def remove_at(self, index):
        """移除特定位置的节点"""
        if index >= self.__length:
            raise IndexError("Index out of bounds")
        current = self.__sentinel.next
        for _ in range(index):
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev
        self.__length -= 1

    def get_value(self, index):
        """获取链表特定位置节点的值"""
        if index >= self.__length:
            raise IndexError("Index out of bounds")
        current = self.__sentinel.next
        for _ in range(index):
            current = current.next
        return current.item
