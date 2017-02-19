class queue():
	def __init__(self,limit=10):
		self.limit=limit
		self.que=[]
		self.fromt=None
		self.rear=None
		self.size=0
	def enqueue(self,data):
		if self.size >=self.limit:
			return 0
		else:
			self.que.append(data)
		if self.fromt is None:
			self.fromt=self.rear=0
		else:
			self.rear=self.size
		self.size+=1
		print 'enque',self.que
	def dequeue(self):
		if self.size<=0:
			return 0
		else:
			print 'pop',self.que.pop(0)
			self.size-=1
			if self.size==0:
				self.fromt=self.rear=None
			else:
				self.rear=self.size-1
			print 'deque',self.que
	def size(self):
		return self.size

if __name__ == '__main__':
	q=queue()
	q.enqueue (10)
	q.enqueue(77)
	l={1,2,3}
	q.enqueue(l)
	q.dequeue()
	q.dequeue()
	q.dequeue()


