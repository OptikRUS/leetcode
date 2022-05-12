"""
1.1 Написать класс "Тумбочка", у которой определить поле items, который представлял бы собой список. Реализовать метод
add_item, который на вход будет принимать произвольный объект и добавлять к списку items.
Сделать так, чтобы объект класса "тумбочка" был итерируемым: перебор должен осуществляться точно также, как если бы мы
итерировались по списку items.

1.2 Написать кастомный итератор для тумбочки и реализовать в нём метод to_start, который возвращал бы перебор элементов
к началу, метод to_custom, который бы ставил курсор перебора на определенный элемент в списке по индексу.
"""


class Iterator:
    def __init__(self, iter_object):
        self.iter_object = iter_object
        self.count = 0

    def to_start(self):
        self.count = 0

    def to_custom(self, n):
        max_index = len(self.iter_object) - 1
        if n < 0 or n > max_index:
            raise IndexError("max index %d but %d was given" % (max_index, n))
        self.count = n

    def __next__(self):
        while True:
            if self.count < len(self.iter_object):
                element = self.iter_object[self.count]
                self.count += 1
                return element
            raise StopIteration


class Tumba:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        return self.items.append(item)

    def __iter__(self):
        iteration = Iterator(self.items)
        # iteration.to_custom()
        return iteration


tumbochka = Tumba()
tumbochka.add_item(1)
tumbochka.add_item('item')
tumbochka.add_item([1, 2, 3])
tumbochka.add_item({3, 4, 5})

for i in tumbochka:
    print(i)
