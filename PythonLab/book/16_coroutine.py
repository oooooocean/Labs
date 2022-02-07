from functools import wraps
from collections import namedtuple
Result = namedtuple('Result', 'count average')


def coroutine(func):
    """
    预激协程的装饰器
    """
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@coroutine
def averager():
    """
    计算移动平均值
    :return: 平均值
    """
    total, count, average = 0.0, 0, None
    while True:
        receive = yield average
        total += receive
        count += 1
        average = total / count


def averager2():
    """
    在结束时返回平均值
    :return: 平均值
    """
    total, count, average = 0.0, 0, None
    while True:
        receive = yield
        if receive is None:
            break  # 结束协程
        total += receive
        count += 1
        average = total / count
    return Result(count, average)  # 返回值保存在 StopIteration 的 value属性中


def gen():
    """
    yield from 可以简化从for循环中 yield 表达式
    """
    yield from 'AB'
    yield from range(1, 3)


if __name__ == '__main__':
    print('🚀')
    print('🌺')