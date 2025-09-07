"""
Правила:
1. Все узлы в левом поддереве любого узла имеют значения МЕНЬШЕ значения самого узла.
2. Все узлы в правом поддереве любого узла имеют значения БОЛЬШЕ
(или равны, в зависимости от реализации) значения самого узла.
3. Оба поддерева (левое и правое) каждого узла также должны быть деревьями двоичного поиска.
Строгий порядок: левые потомки < узел < правые потомки.

Деревья позволяют хранить иерархическую информацию, которую было бы сложно или
невозможно представить в такой линейной структуре данных, как массив.

Depth-First (DFS)	Обход в глубину				Стратегия	Рекурсивно уходим "вглубь" по одному из путей, потом возвращаемся.
→ Preorder			Прямой обход				Вид DFS		корень -> левое поддерево -> правое поддерево
→ Inorder			Симметричный/Центрированный	Вид DFS		левое поддерево -> корень -> правое поддеревоо
→ Postorder			Обратный обход				Вид DFS		левое поддерево -> правое поддерево -> корень
Breadth-First (BFS)	Обход в ширину				Стратегия	Уровень 0 -> Уровень 1 -> Уровень 2 -> ... (слева направо на каждом уровне)
"""


class TreeNode:
	"""Внутренний узел BinarySearchTree.

	Дети: `left` (< value) и `right` (> value).
	"""

	def __init__(self, value):
		self.value = value  # Значение узла
		self.left = None  # Левый потомок
		self.right = None  # Правый потомок
		self.parent = None  # Родительский узел (опционально, но полезно для удаления)


class BinarySearchTree:
	"""Простое (несбалансированное) бинарное дерево поиска.

	Инвариант: для любого узла n —
	- все значения в n.left строго меньше n.value
	- все значения в n.right строго больше n.value

	Важные заметки:
	* Это НЕ сбалансированная структура. В худшем случае высота = O(n).
	* Оценки сложности ниже — для случайных данных/среднего случая:
	- поиск/вставка/удаление: O(log n) в среднем, O(n) в худшем
	* Значения должны поддерживать операции сравнения (<, >, ==).
	"""

	def __init__(self):
		self.root = None  # Корневой узел дерева

	def insert(self, value):
		"""Вставка элемента в BinarySearchTree"""
		if self.root is None:
			self.root = TreeNode(value)
		else:
			self._insert_recursive(self.root, value)

	def _insert_recursive(self, node, value):
		"""Рекурсивная вставка
		Алгоритм: Сравнение с текущим узлом и рекурсивный спуск влево (если меньше)
		или вправо (если больше)
		Сложность: O(log n) в среднем, O(n) в худшем случае (вырожденное дерево)
		"""
		if value < node.value:
			if node.left is None:
				node.left = TreeNode(value)
			else:
				self._insert_recursive(node.left, value)
		elif value > node.value:
			if node.right is None:
				node.right = TreeNode(value)
			else:
				self._insert_recursive(node.right, value)

	# Если value == node.value, дубликаты игнорируем

	def search(self, value):
		"""Поиск элемента в BinarySearchTree"""
		return self._search_recursive(self.root, value)

	def _search_recursive(self, node, value):
		"""Рекурсивный поиск
		Алгоритм: сравнение и рекурсивный спуск
		Сложность: O(log n) в среднем, O(n) в худшем
		Возвращает: True/False
		"""
		if node is None:
			return False

		if value == node.value:
			return True
		elif value < node.value:
			return self._search_recursive(node.left, value)
		else:
			return self._search_recursive(node.right, value)

	def delete(self, value):
		"""Удаление элемента из BinarySearchTree"""
		self.root = self._delete_recursive(self.root, value)

	def _delete_recursive(self, node, value):
		"""Рекурсивное удаление
		Критически важно: результат рекурсивного вызова присваивается обратно!
		Это позволяет "переподключить" поддеревья после удаления узла.
		Функция всегда должна вернуть ссылку на корень (возможно, обновленного) поддерева.
		Это обеспечивает правильное переподключение на всех уровнях рекурсии.
		"""
		if node is None:
			return node

		# Поиск узла для удаления
		if value < node.value:
			node.left = self._delete_recursive(node.left, value)
		elif value > node.value:
			node.right = self._delete_recursive(node.right, value)
		else:
			# Найден узел для удаления

			# Случай 1: узел без детей (лист)
			if node.left is None and node.right is None:
				return None

			# Случай 2: узел с одним ребенком
			if node.left is None:
				return node.right
			if node.right is None:
				return node.left

			# Случай 3: узел с двумя детьми
			# Находим наименьший элемент в правом поддереве (инордер-преемник)
			min_node = self._find_min(node.right)  # Находим преемника
			node.value = min_node.value  # Копируем значение
			# Удаляем инордер-преемника
			node.right = self._delete_recursive(node.right, min_node.value)  # Удаляем преемника

		return node

	def _find_min(self, node):
		"""Поиск минимального элемента в поддереве"""
		while node.left is not None:
			node = node.left
		return node

	def _find_max(self, node):
		"""Поиск максимального элемента в поддереве"""
		while node.right is not None:
			node = node.right
		return node

	def find_min(self):
		"""Поиск минимального элемента в дереве"""
		if self.root is None:
			return None
		return self._find_min(self.root).value

	def find_max(self):
		"""Поиск максимального элемента в дереве"""
		if self.root is None:
			return None
		return self._find_max(self.root).value

	def height(self):
		"""Высота дерева"""
		return self._height_recursive(self.root)

	def _height_recursive(self, node):
		"""Рекурсивный подсчет высоты"""
		if node is None:
			return -1  # Высота пустого дерева = -1

		left_height = self._height_recursive(node.left)
		right_height = self._height_recursive(node.right)

		return max(left_height, right_height) + 1

	def size(self):
		"""Количество узлов в дереве"""
		return self._size_recursive(self.root)

	def _size_recursive(self, node):
		"""Рекурсивный подсчет узлов"""
		if node is None:
			return 0
		return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

	def is_empty(self):
		"""Проверка на пустоту"""
		return self.root is None

	def inorder_traversal(self):
		"""Инордерный обход (левое поддерево -> корень -> правое поддерево)
		Симметричный обход
		Выводит элементы в отсортированном порядке для BST"""
		result = []
		self._inorder_recursive(self.root, result)
		return result

	def _inorder_recursive(self, node, result):
		"""Рекурсивный инордерный обход"""
		if node is not None:
			self._inorder_recursive(node.left, result)
			result.append(node.value)
			self._inorder_recursive(node.right, result)

	def preorder_traversal(self):
		"""Преордерный обход (корень -> левое поддерево -> правое поддерево)
		Прямой обход
		Используется для создания копии дерева"""
		result = []
		self._preorder_recursive(self.root, result)
		return result

	def _preorder_recursive(self, node, result):
		"""Рекурсивный преордерный обход"""
		if node is not None:
			result.append(node.value)
			self._preorder_recursive(node.left, result)
			self._preorder_recursive(node.right, result)

	def postorder_traversal(self):
		"""Постордерный обход (левое поддерево -> правое поддерево -> корень)
		Обратный обход
		Используется для безопасного удаления дерева"""
		result = []
		self._postorder_recursive(self.root, result)
		return result

	def _postorder_recursive(self, node, result):
		"""Рекурсивный постордерный обход"""
		if node is not None:
			self._postorder_recursive(node.left, result)
			self._postorder_recursive(node.right, result)
			result.append(node.value)

	def level_order_traversal(self):
		"""Обход в ширину (по уровням)
		Использует очередь для итеративного обхода"""
		if self.root is None:
			return []

		result = []
		queue = [self.root]

		while queue:
			node = queue.pop(0)  # Извлекаем первый элемент (FIFO)
			result.append(node.value)

			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

		return result

	def print_tree(self):
		"""Простая визуализация дерева"""
		if self.root is None:
			print("Дерево пустое")
			return

		self._print_tree_recursive(self.root, "", True)

	def _print_tree_recursive(self, node, prefix, is_tail):
		"""Рекурсивная печать дерева"""
		if node is not None:
			print(prefix + ("└── " if is_tail else "├── ") + str(node.value))

			children = []
			if node.left is not None:
				children.append(node.left)
			if node.right is not None:
				children.append(node.right)

			for i, child in enumerate(children):
				is_last = i == len(children) - 1
				extension = "    " if is_tail else "│   "
				if child == node.left:
					self._print_tree_recursive(child, prefix + extension,
											   is_last and node.right is None)
				else:  # child == node.right
					self._print_tree_recursive(child, prefix + extension, is_last)

	def is_valid_bst(self):
		"""Проверка корректности BST"""
		return self._is_valid_recursive(self.root, float('-inf'), float('inf'))

	def _is_valid_recursive(self, node, min_val, max_val):
		"""Рекурсивная проверка корректности BST"""
		if node is None:
			return True

		if node.value <= min_val or node.value >= max_val:
			return False

		return (self._is_valid_recursive(node.left, min_val, node.value) and
				self._is_valid_recursive(node.right, node.value, max_val))

	def invert_tree_dfs_recursive(self):
		"""Публичный метод для инвертирования дерева"""
		self.root = self._invert_dfs_recursive(self.root)

	def _invert_dfs_recursive(self, node):
		if node is None:
			return None

		# Меняем местами детей
		node.left, node.right = node.right, node.left

		# Рекурсивно обрабатываем поддеревья
		self._invert_dfs_recursive(node.left)
		self._invert_dfs_recursive(node.right)

		return node

	def invert_tree_bfs(self):
		if self.root is None:
			return self

		queue = [self.root]

		while queue:
			current = queue.pop(0)  # FIFO

			# Меняем детей
			current.left, current.right = current.right, current.left

			# Добавляем детей в очередь
			if current.left:
				queue.append(current.left)
			if current.right:
				queue.append(current.right)

	def invert_tree_dfs_iterative(self):
		if self.root is None:
			return self

		stack = [self.root]

		while stack:
			current = stack.pop()  # LIFO

			# Меняем детей
			current.left, current.right = current.right, current.left

			# Добавляем детей в стек
			if current.left:
				stack.append(current.left)
			if current.right:
				stack.append(current.right)


if __name__ == '__main__':
	print("=== ДЕМОНСТРАЦИЯ BINARY SEARCH TREE ===\n")

	# Создание и заполнение дерева
	bst = BinarySearchTree()
	values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]
	for value in values:
		bst.insert(value)
	# print(f"Вставлен: {value}")

	# el = 30
	# found = bst.search(el)
	# print(f"Element {el} found in bst: {found}:")

	# print("\n2. Структура дерева:")
	bst.print_tree()

	print(f"\nДерево построено. Размер: {bst.size()}, Высота: {bst.height()}")
	print(f"Минимум: {bst.find_min()}")
	print(f"Максимум: {bst.find_max()}")

	# print(f"Инордерный (отсортированный): {bst.inorder_traversal()}")
	# print(f"Преордерный: {bst.preorder_traversal()}")
	# print(f"Постордерный: {bst.postorder_traversal()}")
	# print(f"По уровням: {bst.level_order_traversal()}")

	bst.invert_tree_dfs_recursive()
	bst.print_tree()




# Для визуализатора python
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.parent = None
#
#
# class BinarySearchTree:
#
#     def __init__(self):
#         self.root = None
#
#     def insert(self, value):
#         if self.root is None:
#             self.root = TreeNode(value)
#         else:
#             self._insert_recursive(self.root, value)
#
#     def _insert_recursive(self, node, value):
#         if value < node.value:
#             if node.left is None:
#                 node.left = TreeNode(value)
#             else:
#                 self._insert_recursive(node.left, value)
#         elif value > node.value:
#             if node.right is None:
#                 node.right = TreeNode(value)
#             else:
#                 self._insert_recursive(node.right, value)
#
#     def search(self, value):
#         return self._search_recursive(self.root, value)
#
#     def _search_recursive(self, node, value):
#         if node is None:
#             return False
#
#         if value == node.value:
#             return True
#         elif value < node.value:
#             return self._search_recursive(node.left, value)
#         else:
#             return self._search_recursive(node.right, value)
#
#     def delete(self, value):
#         self.root = self._delete_recursive(self.root, value)
#
#     def _delete_recursive(self, node, value):
#         if node is None:
#             return node
#
#         if value < node.value:
#             node.left = self._delete_recursive(node.left, value)
#         elif value > node.value:
#             node.right = self._delete_recursive(node.right, value)
#         else:
#             if node.left is None and node.right is None:
#                 return None
#
#             if node.left is None:
#                 return node.right
#             if node.right is None:
#                 return node.left
#
#             min_node = self._find_min(node.right)
#             node.value = min_node.value
#             node.right = self._delete_recursive(node.right, min_node.value)
#
#         return node
#
#     def _find_min(self, node):
#         while node.left is not None:
#             node = node.left
#         return node
#
#
# bst = BinarySearchTree()
# values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]
# for value in values:
#     bst.insert(value)
#     print(f"Вставлен: {value}")
#
# delete_values = [30, 50]
#
# for val in delete_values:
#     print(f"\nУдаляем: {val}")
#     bst.delete(val)
