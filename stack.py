class stack:
	def __init__(self,limit=10):
		self.stk=[]
		self.limit=limit
	def isEmpty(self):
		return llen(self.stk)<=0
	def push(self,item):
		if len(self.stk)>=self.limit:
			print 'stack overflow'
		else:
			self.stk.append(item)
		print 'stack after push',self.stk
	def pop(self):
		if len(self.stk)<=0:
			print 'stack underflow'
			return 0
		else:
			self.stk.pop()
		print 'stack after pop',self.stk
	def peek(self):
		if len(self.stk)<=0:
			return 0
		else:
			return self.stk[-1]
	def size(self):
		print 'size',len(self.stk)

if __name__ == '__main__':
	s1=stack()
	s1.push(10)
	s1.push(13)
	# s1.push(4)
	# s1.push(2)
	# s1.push(33)
	# s1.push(11)
	# s1.push(1)
	# s1.push(22)
	# s1.push(3333)
	# s1.push(33)
	print s1.peek()
	s1.size()
