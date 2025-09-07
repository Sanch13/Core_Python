"""
Дерево - это нелинейный абстрактный тип данных, состоящий из узлов,
объединенных в иерархическую структуру. Общие операции с деревом включают вставку,
поиск и удаление.
Двоичное дерево поиска — это древовидная структура данных, в которой
у каждого узла может быть только два дочерних узла, причем дерево хранит
свои узлы в отсортированном порядке, где значение каждого узла больше
любого значения в его левом поддереве и меньше любого значения в его
правом поддереве.
Как и в случае с ключами хеш-таблицы, нельзя
хранить дубликаты значений в двоичном дереве поиска. В отличие от таких линейных структур данных,
как массивы и связные списки, вы не можете все время перемещаться по дереву без возврата назад.
Вы можете попасть в каждый узел дерева, начав с корневого узла, но как только вы ушли от
корневого узла, вы можете попасть только в потомки узла.
"""


class BinaryTree:
	def __init__(self, value):
		self.key = value
		self.left_child = None
		self.right_child = None

	def insert_left(self, value):
		if self.left_child is None:
			self.left_child = BinaryTree(value)
		else:
			bin_tree = BinaryTree(value)
			bin_tree.left_child = self.left_child
			self.left_child = bin_tree

	def insert_right(self, value):
		if self.right_child is None:
			self.right_child = BinaryTree(value)
		else:
			bin_tree = BinaryTree(value)
			bin_tree.right_child = self.right_child
			self.right_child = bin_tree

	def breadth_first_search(self, n):
		'''
		обход в ширину - поиск в ширину
		'''
		current = [self]
		next = []
		while current:
			for node in current:
				if node.key == n:
					return True
				if node.left_child:
					next.append(node.left_child)
				if node.right_child:
					next.append(node.right_child)
			current = next
			next = []
		return False


def inorder(tree):
	if tree:
		inorder(tree.left_child)
		print(tree.key)
		inorder(tree.right_child)


def preorder(tree):
	if tree:
		print(tree.key)
		preorder(tree.left_child)
		preorder(tree.right_child)


def postorder(tree):
	if tree:
		postorder(tree.left_child)
		postorder(tree.right_child)
		print(tree.key)


tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.insert_left(4)
tree.left_child.insert_right(6)
tree.insert_right(5)
print(tree.breadth_first_search(6))
print(preorder(tree))
