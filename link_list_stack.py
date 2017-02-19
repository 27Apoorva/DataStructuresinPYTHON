class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
class stack:
	def __init__(self,data,head=None):
		self.head=head
		if data:
			for data in data:
				self.push(data)

	def push(self, data):
	    new_node = Node(data)
	    new_node.set_next(self.head)
	    self.head = new_node
	def pop(self):
		current = self.head
		new=current.get_next()
		self.head=new
		return current.get_data()
	def peek(self):
		if self.head is None:
			raise indexerror
		return self.head
if __name__ == '__main__':
	li=["f","sec","third","1"]
	s1=stack(li)
	
	
	print s1.pop()
	print s1.pop()

