from collections import namedtuple

a, b, *rest = range(2)
print('rest: ', rest)

*rest, _ = range(3)
print('rest: ', rest)

City = namedtuple('City', ['name', 'country'])
hefei = City(*['合肥', '中国'])  # 解构
# hefei = City('合肥', '中国')
for key, value in hefei._asdict().items():
    print(key + ':', value)

l = list(range(10))
l[:5] = [100]  # 右侧必须是可迭代对象
print(l)

"""
等价于
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)  # 同一个引用添加了3次
"""
# l2 = [['_']*3 for _ in range(3)]
l2 = [['_'] * 3] * 3  # 3 个指向同一对象的引用的列表
l2[1][2] = 'O'
print(l2)


def __test():
    """
    1. 对不可变序列进行重复拼接操作的话, 效率会很低, 因为每次都有一个新对象, 而解释器需要把原来对象中的元素先复制到新的对象里, 然后再追加新的元素.
    2. 增量赋值不是原子操作.
    """
    t = (1, 2, [3, 4])
    t[2] += [5]  # 将计算结果重新赋值给 t[2] 时报错
    print(t)


if __name__ == '__main__':
    print('start')
    __test()