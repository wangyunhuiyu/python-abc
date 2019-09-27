# 模拟进程
class Queue:
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        # 往队列中添加一个item元素
        self.__list.append(item)

    def dequeue(self,n):
        # 从队列中删除一个元素
        if n in self.__list:
            return self.__list.remove(n)
        else:
            print('找不到该进程')
            return None

    def is_empty(self):
        # 判断一个队列是否为空
        return self.__list == []

    def size(self):
        # 返回队列大小
        return len(self.__list)

    def bianli(self):
        for i in self.__list:
            print(i,end='')
        print('\n')


if __name__ == "__main__":
    s = Queue()
    x = input('请输入进程队列：')
    for i in x:
        s.enqueue(i)
    s.bianli()
    y = input('增加入队进程:')
    for j in y:
        s.enqueue(j)
    s.bianli()
    h = input('输入出队进程：')
    s.dequeue(h)
    print('出队后进程队列: ')
    s.bianli()
    print('\n')
    v = input('供显示，无需输入！')