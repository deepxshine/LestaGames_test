from q2 import FIFO1, FIFO2, FIFO3


# проверим время работы для каждой из реализаций FIFO


def test1(count):
    cls = FIFO1()
    for i in range(count):
        cls.add(i)
    for _ in range(count):
        cls.get()


def test2(count):
    cls = FIFO2()
    for i in range(count):
        cls.add(i)
    for _ in range(count):
        cls.get()


def test3(count):
    cls = FIFO3()
    for i in range(count):
        cls.add(i)
    for _ in range(count):
        cls.get()


if __name__ == '__main__':
    from time import time
    c = 2000
    t = time()
    test1(c)
    t1 = time() - t
    t = time()
    test2(c)
    t2 = time() - t

    t = time()
    test3(c)
    t3 = time() - t

    print(t1, t2, t3, sep='\n')
    print(min(t1, t2, t3))
    # в итоге самый быстрой оказалась втрая реализация FIFO
