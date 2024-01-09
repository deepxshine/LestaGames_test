"""Вопрос №3
На языке Python предложить алгоритм, который быстрее всего
(по процессорным тикам) отсортирует данный ей массив чисел.
Массив может быть любого размера со случайным порядком чисел
(в том числе и отсортированным). Объяснить, почему вы считаете,
что функция соответствует заданным критериям.
"""
from random import randint

"""Алгоритм быстрой сортировки имеет временную сложность O(nlogn) в среднем 
случае, а также использует простые операции сравнения и сложения
"""
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    key = arr[(len(arr) // 2)]
    left = [i for i in arr if i < key]
    center = [i for i in arr if i == key]
    right = [i for i in arr if i > key]
    return quicksort(left) + center + quicksort(right)


mass = [randint(1, 20) for _ in range(10)]
print(mass)
print(quicksort(mass))

