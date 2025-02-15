# -*- coding: utf-8 -*-
# @Time    : 2023/12/14 15:13
# @Author  : AI悦创
# @FileName: 3.1 SampleLinkedList-1.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# Created by Bornforthis.
class IntList(object):
    def __init__(self):
        """
        first:存自己本身的数据
        rest:存下一个节点，也就下一个节点是谁
        """
        self.first = None
        self.rest = None


l1 = IntList()
l1.first = 5

l2 = IntList()
l2.first = 10

l3 = IntList()
l3.first = 15


l1.rest = l2
l2.rest = l3
# 正好使用两行代码连在一起了，也就是火车的两个铁链
# PS: 如果你这么写的话：l1.rest = l2.first > 注意：这将不是链接一个车厢，而是连接一个 Value。
# 所以：l1.rest = l2 才是连接车厢

print("第一节车厢：{}".format(l1.first))
print("第二节车厢：{}".format(l1.rest.first))
print("第三节车厢：{}".format(l1.rest.rest.first))

