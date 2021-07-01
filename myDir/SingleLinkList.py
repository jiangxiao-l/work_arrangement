# 初始化节点
class createNode:
    def __init__(self, data):
        self.data = data  # 数据域
        self.next = None  # 指针域


class SingleLinkList:
    # 初始化出空链表
    def __init__(self):
        # 空链表:数据域为None, 指针域为None
        self.head = createNode(None)

    # 初始化出链表
    def init_node(self, data):
        """
        :param data: []
        :return:
        """
        # 头结点信息
        p = self.head
        for i in data:
            # 初始化出头结点信息
            node = createNode(i)
            p.next = node
            p = p.next

    # 遍历所有的节点信息
    def all_values(self):
        """
        遍历
        :return:
        """
        # 判断链表是否为空
        if self.is_empty():
            return 0
        p = self.head
        while p.next:
            print(p.next.data, end=',')
            p = p.next

    # 在节点i后，插入一个节点
    def insert(self, i, data):
        """
        在i节点之前插入
        :param i:
        :param data:
        :return:
        """
        # 判断i是否超出了链表的长度
        if i > self.len_list() + 1 or i < 1:
            return "插入失败 输入的索引位置有误"
        index = 0
        p = self.head
        while index < i - 1:
            p = p.next
            index += 1
        # 初始化出插入的节点数据
        insert_node = createNode(data)
        insert_node.next = p.next
        p.next = insert_node

    # 删除第i个节点的信息
    def delete(self, i):
        """
        删除第i个节点
        :param i:
        :return:
        """
        # 判断是否是空链表、i的长度是否大于链表的长度
        if self.is_empty() or i > self.len_list() or i < 1:
            return "删除失败"

        p = self.head
        pre = p.next
        index = 0
        while index < i - 1:
            p = p.next
            pre = p.next
            index += 1
        p.next = pre.next
        pre.next = None

    # 更新第i个节点的数据
    def update(self, i, data):
        """
        修改某个节点的值
        :param i:
        :param data:
        :return:
        """
        if self.is_empty() or i > self.len_list() or i < 1:
            return "删除失败"
        p = self.head
        index = 0
        while index < i:
            p = p.next
            index += 1
        p.data = data

    # 判断是否是空节点
    def is_empty(self):
        """
        判断是否为空
        :return:
        """

        status = False
        if not self.head.next:
            status = True
        return status

    # 获取链表的长度
    def len_list(self):
        """
        获取链表的长度
        :return:
        """
        length = 0
        p = self.head
        while p.next:
            length += 1
            p = p.next
        return length


if __name__ == '__main__':
    ll = SingleLinkList()
    ll.init_node([1, 2, 3, 4, 5, 6])
    # ll.insert(7, 7)
    # ll.all_values()
    # ll.delete(3)
    ll.update(7, 5.5)
    ll.all_values()
