# *_* coding : UTF-8 *_*
# Author ： jiangxiaolong
# time   ： 2021/4/21  上午9:49

# 顺序表
class SequenceTable:

    # 初始化顺序表(表的最大容量、表的长度、标的数据)
    def __init__(self, max_len):
        self.max_len = max_len  # 最大的容量
        self.num = 0  # 顺序表的当前的长度
        self.data = [None] * self.max_len  # 顺序表的数据

    # 判断该顺序表是否已经满
    def is_full(self):
        """
        :return:
        """
        status = False
        if self.num >= self.max_len:
            status = True
        return status

    # 增(在最后一个位置添加元素)
    def append(self, values):
        """
        :param values:
        :return:
        """
        # 判断是否已经满
        if self.is_full():
            return "顺序表已满"

        # 在最后面添加一个数据
        self.data[self.num] = values
        # 修改表的长度
        self.num += 1
        return "插入成功"

    # 增(在指定的索引后面添加元素)
    def insert(self, index, values):
        """
        :param index:
        :param values:
        :return:
        1. 将第index个到最后一个的元素整体往后移
        2. 把第index 个位置的元素空出来  赋值给values
        3. 表的长度 + 1
        """
        # 判断表是否已经满
        if self.is_full():
            return "顺序表已满"

        # 插入的索引一定要小于表的长度
        if index > self.num + 1 or index < 1:
            return "插入的索引有问题"

        # 将第index个到最后一个的元素整体往后移
        for i in range(self.max_len - 1, index - 1, -1):
            self.data[i] = self.data[i - 1]
        # 赋值
        self.data[index - 1] = values

        # 修改表的长度
        self.num += 1
        return "数据插入成功"

    # 删除某个索引下面的元素
    def delete(self, index):
        """
        :param index:
        :return:
        1. 获取第index-1下面的元素的值
        2. 将 所有的元素统一往前移动一个
        """
        if index > self.num or index < 1:
            return "删除的索引有问题"

        delete_values = self.data[index - 1]
        for i in range(index, self.max_len):
            self.data[i - 1] = self.data[i]
        self.data[self.max_len - 1] = None
        self.num -= 1
        return delete_values

    # 改
    def update(self, index, values):
        """
        :param index:
        :param values:
        :return:
        """
        if index > self.num or index < 1:
            return "索引输入错误"
        self.data[index - 1] = values

        return "更新成功"

    # 判断是否为空
    def is_empty(self):
        """
        :return:
        """
        status = True
        if self.num:
            status = False
        return status

    # 判断某个元素是否在表中
    def is_exist(self, values):
        """

        :param values:
        :return:
        """
        for i in range(0, self.num):
            if values == self.data[i]:
                return True
        else:
            return False

    # 遍历整个顺序表
    def all_values(self):
        """
        :return:
        """
        for i in range(0, self.num):
            print(self.data[i])


if __name__ == '__main__':
    sequence_table = SequenceTable(10)
    sequence_table.append(1)
    sequence_table.append(3)
    sequence_table.insert(2, 2)
    sequence_table.insert(4, 4)
    print(sequence_table.data)
    sequence_table.insert(2, 5)
    print(sequence_table.data)
    # c = sequence_table.insert(4, 4)
    # print(sequence_table.data, sequence_table.num)
    # sequence_table.delete(1)
    # print(sequence_table.data, sequence_table.num)
    # sequence_table.delete(2)
    # print(sequence_table.data, sequence_table.num)
    # sequence_table.append(5)
    # sequence_table.all_values()
    # print(sequence_table.is_exist(2))
