"""разработать структуру данных, поддерживающую такие операции
стека, как проталкивание и выталкивание, и включающую в себя метод возврата
наименьшего элемента. Временная сложность всех операций стека должна быть
равна О(1)"""


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_val = []

    def push(self, n):
        if len(self.stack) == 0:
            self.max_val.append(n)
        elif n > self.stack[-1]:
            self.max_val.append(n)
        else:
            self.max_val.append(self.max_val[-1])
        self.stack.append(n)

    def pop(self):
        self.max_val.pop()
        return self.stack.pop()

    def get_min_val(self):
        return self.max_val[-1]


max_stack = MaxStack()
max_stack.push(10)
print(max_stack.stack)
print(max_stack.max_val)
max_stack.push(20)
print(max_stack.stack)
print(max_stack.max_val)
max_stack.push(30)
print(max_stack.stack)
print(max_stack.max_val)
max_stack.push(5)
print(max_stack.stack)
print(max_stack.max_val)
max_stack.pop()
print(max_stack.stack)
print(max_stack.max_val)
max_stack.pop()
print(max_stack.stack)
print(max_stack.max_val)
max_stack.pop()
print(max_stack.stack)
print(max_stack.max_val)
max_stack.pop()
print(max_stack.stack)
print(max_stack.max_val)
