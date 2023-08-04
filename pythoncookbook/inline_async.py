# 7.11 内联回调函数
# 生成器和协程将回调函数内联到一个函数中

# def apply_async(func, args, *, callback):
#     result = func(*args)
#     callback(result)

from queue import Queue
from functools import wraps


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    # 在包装函数 wrapper 上面保留原始函数 func 的元数据
    @wraps(func)
    # args 来自 func 接受参数
    def wrapper(*args):
        f = func(*args)
        # 这个队列将用于在异步任务之间传递结果
        result_queue = Queue()
        result_queue.put(None)
        while True:
            # 首先从 result_queue 队列中获取一个结果值
            result = result_queue.get()
            try:
                # a 是一个包含异步任务函数和参数的命名元组
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper


def add(x, y):
    return x + y

# 装饰器本质上是一个函数（或类），它接受一个函数作为输入，并返回一个新的函数
@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(f"[1] add(2, 3) = {r}")
    r = yield Async(add, ('hello', 'world'))
    print(r)

    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')


if __name__ == "__main__":
    import multiprocessing
    
    pool = multiprocessing.Pool()
    # pool.apply_async 方法是异步执行的，即函数提交后会立即返回，不会阻塞主进程
    # 可以使用 ApplyResult 对象的 get() 方法来阻塞主进程，直到函数执行完毕并返回结果
    apply_async = pool.apply_async

    test()