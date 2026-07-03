class Value:
	def __init__(self, data, _children=(), _op=''):
		self.data = data
		self.grad = 0
		self._backward = lambda: None
		self._prev = set(_children)
		self._op = _op
	def __repr__(self):
		def fmt(x):
			return int(x) if float(x).is_integer() else round(x, 4)
		return f"Value(data={fmt(self.data)}, grad={fmt(self.grad)})"

	def __add__(self, other):
		 # Implement addition here
		other = other if isinstance(other, Value) else Value(other)
		new=Value(self.data+other.data, (self,other), '+')
		def _backward():
			self.grad+=new.grad
			other.grad+=new.grad
		new._backward=_backward
		return new

	def __mul__(self, other):
		# Implement multiplication here
		other = other if isinstance(other, Value) else Value(other)
		new=Value(self.data*other.data, (self,other), '*')
		def _backward():
			self.grad+=other.data*new.grad
			other.grad+=self.data*new.grad
		new._backward=_backward
		return new

	def relu(self):
		# Implement ReLU here
		def _backward():
			if self.data>0:
				self.grad+=new.grad
		new=Value(max(self.data,0), (self,), 'ReLU')
		new._backward=_backward
		return new

	def backward(self):
		# Implement backward pass here
		unique=set()
		backlist=[]
		self.grad=1
		def parents(self):
			for i in self._prev:
				if i not in unique:
					unique.add(i)
					parents(i)
			backlist.append(self)
		parents(self)
		for i in reversed(backlist):
			i._backward()
			