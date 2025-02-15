# -*- coding: utf-8 -*-
# @Time    : 2023/12/20 14:11
# @Author  : AI悦创
# @FileName: Code5-plus2.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# Created by Bornforthis.
# TODO：环状链表
# 定义一个双向链表节点类
class IntNode(object):
    def __init__(self, item, prev=None, next=None):
        self.item = item  # 节点存储的元素
        self.prev = prev  # 指向前一个节点的引用
        self.next = next  # 指向后一个节点的引用


# 定义双向链表类
class DLList(object):
    def __init__(self, x=None):
        self.__sentinel = IntNode(49, None)  # 创建一个哨兵节点（哨兵节点不存储实际数据）
        # 初始化时，哨兵的前后都指向自己，形成一个循环
        self.__sentinel.next = self.__sentinel
        self.__sentinel.prev = self.__sentinel
        self.__length = 0  # 链表长度初始化为0
        if x is not None:
            self.add_last(x)  # 如果初始化时有元素，添加到链表末尾

    # 向链表头部添加元素
    def add_first(self, x):
        new_first = IntNode(x, self.__sentinel, self.__sentinel.next)
        self.__sentinel.next.prev = new_first  # 更新原来第一个节点的前驱
        self.__sentinel.next = new_first  # 更新哨兵节点的下一个节点为新节点
        self.__length += 1  # 链表长度增加

    # 获取链表的第一个元素
    def get_first(self):
        if self.__sentinel.next is not self.__sentinel:  # 如果链表不为空
            return self.__sentinel.next.item  # 返回第一个节点的数据
        return None  # 如果链表为空，返回None

    # 向链表尾部添加元素
    def add_last(self, x):
        new_end = IntNode(x, self.__sentinel.prev, self.__sentinel)
        self.__sentinel.prev.next = new_end  # 更新原来最后一个节点的后继
        self.__sentinel.prev = new_end  # 更新哨兵节点的前一个节点为新节点
        self.__length += 1  # 链表长度增加

    # 获取链表的长度
    def size(self):
        return self.__length  # 返回链表的长度


# 测试代码
if __name__ == '__main__':
    l = DLList(15)
    l.add_first(10)
    l.add_first(5)
    print(l.get_first())  # 应该输出5，因为5是最后添加到链表头部的
    l.add_last(20)
    print(l.size())  # 应该输出4，链表中现在有4个元素
