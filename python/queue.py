class Stack(object):
	"""docstring for Stack"""
  """隊列（Queue）是一種常見的資料結構，它遵循先進先出（FIFO）的原則，這意味著在隊列中添加的元素將按照它們被添加的順序被移除。"""
	def __init__(self):
		super(Stack, self).__init__()
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		self.stack.pop()

	def size(self):
		return len(self.stack)

	def peek(self):
		return self.stack[-1]

	def is_empty(self):
		if len(self.stack) < 1:
			return "Yes, it's empty"
		return "No, the size is {}".format(stack.size())

	def display(self):
		return self.stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(2)
print(stack.peek())
print(stack.is_empty())
print(stack.display())
stack.pop()
print(stack.display())
stack.pop()
print(stack.display())
stack.pop()
stack.pop()
print(stack.display())
stack.pop()
print(stack.display())
print(stack.is_empty())
