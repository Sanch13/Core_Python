'''
Стек — это абстрактный тип данных и линейная структура данных, которая позволяет удалять только
последний добавленный элемент. Стек является примером структуры данных «последним вошел, первым вышел»,
или Last In — First Out (LIFO). Последним вошел, первым вышел — структура данных, в которой элемент, помещенный в
структуру последним, является первым элементом, который выходит из нее.
'''


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

for i in range(3):
    print(stack.pop())
