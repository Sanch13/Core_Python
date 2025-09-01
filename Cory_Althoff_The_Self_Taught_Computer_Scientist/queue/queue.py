"""
Очередь как абстрактный тип данных описывает структуру
данных, работающую подобно кассовым очередям в продуктовом магазине:
первый человек в очереди является первым на оплату, а вновь приходящие
встают в конец очереди. Очередь является примером структуры данных «первым вошел, первым
вышел», или First In — First Out (FIFO).
"""


class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


class Queue:
	def __init__(self):
		self.front = None
		self.rear = None
		self._size = 0

	def enqueue(self, item):
		self._size += 1
		node = Node(item)
		if self.rear is None:
			self.front = node
			self.rear = node
		else:
			self.rear.next = node
			self.rear = node

	def dequeue(self):
		if self.front is None:
			raise IndexError('pop from empty queue')

		self._size -= 1
		temp = self.front
		self.front = self.front.next
		if self.front is None:
			self.rear = None
			return temp.data

	def size(self):
		return self._size

	def print_queue(self):
		current = self.front
		while current:
			print(current.data, end=" → ")
			current = current.next
		print("None")


if __name__ == '__main__':
	queue = Queue()
	queue.enqueue(1)
	queue.print_queue()
	queue.enqueue(2)
	queue.print_queue()
	queue.enqueue(3)
	queue.print_queue()
	print('size', queue.size())
	queue.dequeue()
	queue.print_queue()
	queue.dequeue()
	queue.print_queue()
	queue.dequeue()
	queue.print_queue()
	print('size', queue.size())

# 1 → None
# 1 → 2 → None
# 1 → 2 → 3 → None
# size 3
# 2 → 3 → None
# 3 → None
# None
# size 0