# *_* coding : UTF-8 *_*
# Author ： jiangxiaolong
# time   ： 2021/4/26  下午4:47

# 栈
class Stack:

    # 栈的初始化
    def __init__(self):
        self.__item = []

    # 判断是否为空栈
    def is_empty(self):
        """
        默认：判断栈顶的位置和栈低的位置是否在同一个位置
        top == bottom
        :return:
        """
        status = True
        if self.stack_len:
            status = False
        return status

    #  获取栈的长度
    @property
    def stack_len(self):
        return len(self.__item)

    # 入栈 在表尾添加一个元素
    def push(self, values):
        self.__item.append(values)

    # 出栈 删除表的最后一个元素
    def pop(self):
        # 判断是否空栈
        if self.is_empty():
            return "空栈, 无可删除的元素"
        self.__item.pop(self.stack_len - 1)

    # 获取栈顶的元素
    def peek(self):
        # 判断是否为空栈
        if self.is_empty():
            return "空栈， 无元素可查"
        return self.__item[self.stack_len - 1]


# 栈的应用
class StackApplication:
    # 判断括号是否对称
    @classmethod
    def balanced_parentheses(cls, parentheses):
        """
        思路：
          只要遇到 ( 就进栈
          遇到 ) 就把栈顶的 ( 出栈
          如果是这两个符号以外的其他字符，则不执行任何操作

          在执行 ( 出栈的时候，栈已经为空，则表示符号不平衡【说明 ）更多】
          在执行完所有的出栈后，栈不为空，则符号也不平衡【说明（ 更多】
        :param parentheses
        :return:
        """
        # 初始化出一个空栈
        stack = Stack()

        for i in parentheses:
            if i == "(":
                stack.push(i)
            elif i == ")":
                # 判断是否还存在
                if stack.is_empty():
                    return False
                stack.pop()

        return stack.is_empty()


if __name__ == '__main__':
    stack_app = StackApplication()
    status = stack_app.balanced_parentheses("() (  )")
    print(status)
    # stack = Stack()
    # # 入栈
    # stack.push(1)
    # stack.push(2)
    # # 获取栈的信息
    # # 出栈
    # stack.pop()


