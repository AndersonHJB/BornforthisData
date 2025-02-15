# -*- coding: utf-8 -*-
# @Time    : 2023/12/14 19:50
# @Author  : AI悦创
# @FileName: 3.9 IntNode&SLList.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# Created by Bornforthis.
class IntNode(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


class SLList(object):
    def __init__(self, x):
        self.first = IntNode(x, None)

    def add_first(self, x):
        self.first = IntNode(x, self.first)

    def get_first(self):
        return self.first.item

    # def get(self, index):
    #     if index == 0:
    #         return self.first.item
    #     else:
    #         return self.first.next.get(index - 1)
    def get(self, index, node=None):
        if node is None:
            node = self.first

        if node is None:
            raise IndexError("Index out of bounds")

        if index == 0:
            return node.item
        else:
            return self.get(index - 1, node.next)

    def get_three(self, index):
        """方法三"""
        return self._get_recursive(self.first, index)

    def _get_recursive(self, node, index):
        if node is None:
            raise IndexError("Index out of bounds")
        if index == 0:
            return node.item
        else:
            return self._get_recursive(node.next, index - 1)

    def get_two(self, index):
        """方法二"""
        current_node = self.first
        for i in range(index):
            if current_node.next is None:
                raise IndexError("Index out of bounds")
            current_node = current_node.next
        return current_node.item

    """
    def get(self, index):
        def get_recursive(node, idx):
            if idx == 0:
                return node.item
            else:
                return get_recursive(node.next, idx - 1)

        if self.first is None:
            raise IndexError("Index out of bounds")
        return get_recursive(self.first, index)
    """

    def get_length(self):
        length = 0
        current_node = self.first
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    """
    def get_length(self):
        def length_recursive(node):
            if not node:  # 基本案例：到达链表末尾
                return 0
            else:
                return 1 + length_recursive(node.next)  # 递归步骤

        return length_recursive(self.first)
    """


# l = SLList(10)
# l = IntList(5, None) 比之前的好
# l = SLList(5)
# l = SLList(10)
# l = SLList(15)
l = SLList(5)
l.add_first(10)
l.add_first(15)
print(l.get(0))
print(l.get(1))
print(l.get(2))
print(l.get_length())
