class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head  # Новая нода ссылается на текущую голову
            self.head = new_node       # Обновляем голову

    def pop(self):
        if self.head is None:
            return None

        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def print_stack(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


# Демонстрация
stack = Stack()
print("Добавляем 10:")
stack.push(10)
stack.print_stack()  # 10 → None

print("Добавляем 20:")
stack.push(20)
stack.print_stack()  # 20 → 10 → None

print("Добавляем 30:")
stack.push(30)
stack.print_stack()  # 30 → 20 → 10 → None

print("Delete 30:")
stack.pop()
stack.print_stack()  # 30 → 20 → 10 → None
