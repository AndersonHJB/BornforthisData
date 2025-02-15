class IntNode(object):
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev


class DLList(object):
    def __init__(self, x=None):
        self.__sentinel_front = IntNode(None)  # 头部哨兵
        self.__sentinel_end = IntNode(None)  # 尾部哨兵
        self.__sentinel_front.next = self.__sentinel_end  # 初始化时哨兵节点相连
        self.__sentinel_end.prev = self.__sentinel_front
        self.__length = 0

        if x is not None:
            self.add_last(x)

    def add_first(self, x):
        new_first = IntNode(item=x, next=self.__sentinel_front.next, prev=self.__sentinel_front)
        self.__sentinel_front.next.prev = new_first
        self.__sentinel_front.next = new_first
        self.__length += 1

    def get_first(self):
        if self.__sentinel_front.next != self.__sentinel_end:
            return self.__sentinel_front.next.item
        return None

    def add_last(self, x):
        new_end = IntNode(item=x, next=self.__sentinel_end, prev=self.__sentinel_end.prev)
        # new_end = IntNode(item=x, next=self.__sentinel_end, prev=self.__sentinel_front)  # 目前和上面等价，但是推荐上面的写法。这个写法在链表不为空的时候，会出现节点错误
        self.__sentinel_end.prev.next = new_end
        # self.__sentinel_front.next = new_end  # 目前和上面等价，但是推荐上面的写法。这个写法在链表不为空的时候，会出现节点错误
        self.__sentinel_end.prev = new_end
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
