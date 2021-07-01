# *_* coding : UTF-8 *_*
# Author ： jiangiaolong
# time   ： 2021/5/6  下午4:52

class Node:
    def __init__(self, elem):
        self.elem = elem  # 数据域
        self.next = None  # 指针域


# 循环队列 会浪费一个存储空间(用来判断是否是已满)
class Queue:

    def __init__(self):
        """
        """
        self.front = 0  # 对头 指向出队列下一个元素存放的位置
        self.rear = 0  # 队尾 指向插入队列下一个元素存放的位置
        self.max_size = 10  # 队列的长度
        self.head = Node(None)  # 头部节点信息

    # 判断是否为空队列
    @property
    def is_empty(self):
        """
        头结点 == 尾节点
        :return:
        """
        status = False
        if self.front == self.rear:
            status = True
        return status

    # 判断队列是否满
    @property
    def is_overflow(self):
        """
        （rear + 1）% max_size 的值 == front
        :return:
        """
        status = False
        if (self.rear + 1) % self.max_size == self.front:
            status = True
        return status

    # 进队列
    def in_queue(self, data):
        """
        rear:值向后+1
        """
        # 判断是否是满队列
        if self.is_overflow:
            return "队列已经满了"
        # 在队尾插入数据
        p = self.head
        for i in range(self.rear):
            p = p.next
        node = Node(data)
        p.next = node
        # 修改 rear 的值
        self.rear = (self.rear + 1) % self.max_size
        return "插入成功"

    # 出队列
    def out_queue(self):
        """
        # 删除第一个元素 并返回数据
        front 向后 + 1
        :return:
        """
        # 判断是否是空队列
        if self.is_empty:
            return "空队列，无值可删"

        p = self.head
        pop_node = p.next  # 需要删除的节点
        p.next = c.next  # 将头结点指向下一个节点的信息

        # 修改 front 的值
        self.front = (self.front + 1) % self.max_size
        return pop_node.elem

    # 打印队列
    def print_queue(self):
        p = self.head
        while p.next:
            print(p.next.elem)
            p = p.next


if __name__ == '__main__':
    queue = Queue()
    queue.in_queue(10)
    queue.in_queue(20)
    queue.in_queue(30)
    queue.out_queue()
    queue.out_queue()
    queue.out_queue()

    queue.print_queue()
    c = queue.out_queue()
    print(c)
