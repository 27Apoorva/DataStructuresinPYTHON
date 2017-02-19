class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.last=None
        self.next_node = next_node
        

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node
    def set_last(self,last):
   		self.last=last
    def get_last(self):
    	return self.last
    def set_next(self, new_next):
        self.next_node = new_next

class queue:
	def __init__(self,data=None):
		#self.data=data
		self.fromt=None
		self.rear=None
		self.size=0
	def enqueue(self,data):
		self.lastNode=self.fromt
		self.fromt=Node(data,self.fromt)
		if self.lastNode:
			self.lastNode.set_next(self.fromt)
		if self.rear is None:
			self.rear=self.fromt
			self.size+=1
		print 'f',self.fromt.get_data()
		print 'r',self.rear.get_data()
		

	def que_rear(self):
		if self.rear is None:
			print "sorry"
			raise IndexError
		return self.rear.get_data()
	def get_front(self):
		if self.fromt is None:
			print "sorry front"
			raise IndexError
		return self.fromt.get_data()

	
	def dequeue(self):
		if self.rear is None:
			print "sorry"
			raise IndexError
		result=self.rear.get_data()
		self.rear=self.rear.last
		self.size-=1
		return result
		
	def size(self):
		
		
		return self.size


if __name__ == '__main__':
	q=queue()
	q.enqueue("fi")
	print 'front',q.get_front()
	print 'rear',q.que_rear()
	q.enqueue("se")
	print 'front',q.get_front()
	print 'rear',q.que_rear()
	q.enqueue("thi")
	print 'front',q.get_front()
	print 'rear',q.que_rear()
	print 'deqye',q.dequeue()
	print 'front',q.get_front()
	print 'rear',q.que_rear()