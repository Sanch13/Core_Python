"""разработать структуру данных, поддерживающую такие операции
стека, как проталкивание и выталкивание, и включающую в себя метод возврата
наименьшего элемента. Временная сложность всех операций стека должна быть
равна О(1)"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, n):
        if len(self.stack) == 0:
            self.min_val.append(n)
        elif n < self.stack[-1]:
            self.min_val.append(n)
        else:
            self.min_val.append(self.min_val[-1])
        self.stack.append(n)

    def pop(self):
        self.min_val.pop()
        return self.stack.pop()

    def get_min_val(self):
        return self.min_val[-1]


min_stack = MinStack()
min_stack.push(10)
print(min_stack.stack)
print(min_stack.min_val)
min_stack.push(20)
print(min_stack.stack)
print(min_stack.min_val)
min_stack.push(30)
print(min_stack.stack)
print(min_stack.min_val)
min_stack.push(5)
print(min_stack.stack)
print(min_stack.min_val)
min_stack.pop()
print(min_stack.stack)
print(min_stack.min_val)
min_stack.pop()
print(min_stack.stack)
print(min_stack.min_val)
min_stack.pop()
print(min_stack.stack)
print(min_stack.min_val)
min_stack.pop()
print(min_stack.stack)
print(min_stack.min_val)
