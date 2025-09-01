from Cory_Althoff_The_Self_Taught_Computer_Scientist.stack.stack import Stack


class TextEditor:
	def __init__(self):
		self.text = ""
		self.history = Stack()

	def type(self, chars):
		self.history.push(chars)
		self.text += chars

	def undo(self):
		if not self.history.is_empty():
			self.text = self.history.pop()


editor = TextEditor()
editor.type("Hello")
editor.type(" World")
print(editor.text)  # "Hello World"
editor.undo()
print(editor.text)  # "Hello"
