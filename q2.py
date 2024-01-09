"""
Вопрос №2

На языке Python написать минимум по 2 класса реализовывающих циклический буфер
FIFO. Объяснить плюсы и минусы каждой реализации.

Оценивается:

Полнота и качество реализации
Оформление кода
Наличие сравнения и пояснения по быстродействию
"""

import numpy as np


# первая и самая "простая" реализация FIFO
# плюсы: простота исполения
# минусы: отсутствие оптимизации, атрибут queue является публичным
class FIFO1:

    def __init__(self):
        self.queue = []

    def get(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def add(self, val):
        self.queue.append(val)


# вторая реализация FIFO
# плюсы: оптимизация за счет __slots__, атрибут queue является приватным,
# определен метод __len__ и __bool__
# минусы: уступает по скорости 3-й реализации
class FIFO2:
    __slots__ = ['__queue']

    def __init__(self):
        self.__queue = []

    def get(self):
        if len(self.__queue) > 0:
            return self.__queue.pop(0)
        return None

    def add(self, val):
        self.__queue.append(val)

    def __len__(self):
        return len(self.__queue)

    def __bool__(self):
        return bool(self.__queue)


# третья реализация FIFO
# плюсы: как у FIFO2 + использование np.array - более быстрого массива, чем
# обычный list
# минусы: требование дополнительных библиотек,
# другая логика работы со списками и другими наборами данных.

class FIFO3:
    __slots__ = ['__queue']

    def __init__(self):
        self.__queue = np.array([])

    def get(self):
        if len(self.__queue) > 0:
            item = self.__queue[0]
            self.__queue = np.delete(self.__queue, 0)

            return item
        return None

    def add(self, val):
        self.__queue = np.append(self.__queue, val)

    def __len__(self):
        return len(self.__queue)

    def __bool__(self):
        return bool(self.__queue)


if __name__ == '__main__':
    # проверим правильность работы очереди
    fifo1 = FIFO1()
    fifo1.add(1)
    fifo1.add([1, 2, 3])
    fifo1.add('привет')
    print(fifo1.get())
    print(fifo1.get())
    print(fifo1.get())

    fifo2 = FIFO2()
    fifo2.add(1)
    fifo2.add([1, 2, 3])
    fifo2.add('привет')
    print(fifo2.get())
    print(fifo2.get())
    print(fifo2.get())

    fifo3 = FIFO3()
    fifo3.add(1)
    fifo3.add(1)
    fifo3.add('привет')
    print(fifo3.get())
    print(fifo3.get())
    print(fifo3.get())
