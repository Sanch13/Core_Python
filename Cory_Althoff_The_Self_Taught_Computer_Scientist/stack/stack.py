'''
Стек — это абстрактный тип данных и линейная структура данных, которая позволяет удалять только
последний добавленный элемент. Стек является примером структуры данных «последним вошел, первым вышел»,
или Last In — First Out (LIFO). Последним вошел, первым вышел — структура данных, в которой элемент, помещенный в
структуру последним, является первым элементом, который выходит из нее.
'''


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавить элемент на вершину стека"""
        self.items.append(item)

    def pop(self):
        """Удалить и вернуть верхний элемент"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Попытка извлечения из пустого стека")

    def peek(self):
        """Посмотреть верхний элемент без удаления"""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Проверить, пуст ли стек"""
        return len(self.items) == 0

    def size(self):
        """Размер стека"""
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

for i in range(3):
    print(stack.pop())
