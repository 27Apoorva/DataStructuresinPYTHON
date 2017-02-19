class Node:
	def __init__(self,data=None):
		self.data=data
		self.left=None
		self.right=None
		self.root=None
	def get_data(self):
		return self.data
	def get_left(self):
		return self.left
	def get_right(self):
		return self.right
class BinaryTree:
	# def __init__(self,data=None):
	# 	self.data=data
	# 	self.left=None
	# 	self.right=None
	# 	self.root=None
	# def set_data(self,data):
	# 	self.data=data
	def __init__(self):
		self.root=None
	
	# def Insert_left(self,data):
	# 	if self.left==None:
	# 		self.left=BinaryTree(data)
	# 	else:
	# 		temp=BinaryTree(data)
	# 		temp.left=self.left
	# 		self.left=temp
	# def Insert_Right(self,data):
	# 	if self.right == None:
	# 		self.right=BinaryTree(data)
	# 	else:
	# 		temp=BinaryTree(data)
	# 		temp.right=self.right
	# 		self.right=temp
	def create(self,val):
		if self.root == None:
			self.root = Node(val)
		else:
			current = self.root
			while 1:
				if val < current.data:
					if current.left:
						current = current.left
					else:
						current.left = Node(val)
						break;
				elif val > current.data:
					if current.right:
						current = current.right
					else:
						current.right = Node(val)
						break;
				else:
					break 
	def search(self,search_val):
		current=self.root
		while current:
			if search_val==current.data:
				print 'found'
				return current.data
			elif search_val>current.data:
				current=current.right
			else:
				current=current.left
		return None
	def findMIN(self):
		current=self.root
		while current:
			if current.left !=None:
				current=current.left
			else:
				return current.data
	def findMAX(self):
		current=self.root
		while current:
			if current.right !=None:
				current=current.right
			else:
				return current.data


	def inorder(self,node):
		if node is not None:
			self.inorder(node.left)
			print node.data
			self.inorder(node.right)
	def delete(self,node,data):
		root=node
		print 'out',root.data,data
		if root.data==data:
			print 'in'
			if root.right and root.left:
				print 'm in',root.right,root
				[parent,succ]=self.findM(root.right,root)
				print parent,succ
				if parent.left==succ:
					parent.left=succ.right
				else:
					parent.right=succ.right
				succ.left=root.left
				succ.right=root.right
				print 'succ',succ.data
				return succ
			else:
				if root.left:
					print 'is it'
					return root.left
				else:
					return root.right
				# else:
				# 	print 'deleted',data
		else:
			if root.data>data:
				if root.left:
					print 'roo',root.left
					print data,root.data
					return self.delete(root.left,data)
			else:
				if root.right:
					return self.delete(root.right,data)
		return node
	def findM(self,root,parent):
		print'fff'
		if root.left:
			print 'check',root.left
			return self.findM(root.left,root)
		else:
			print 'check2',parent,root
			
			return parent,root

def preorderREC(root):
	if not root:
		return
	
	print root.data
	preorderREC(root.left)
	preorderREC(root.right)
def find(root,data):
	current=root
	while current:
		if data==current.get_data():
			return current
		if data<current.get_data():
			current=current.get_left()
		else:
			current=current.get_right()
	return None


# def printTree(tree):
#         if tree != None:
#             printTree(tree.get_left()) #print all left recursivley
#             print(tree.get_data())	#print data
#             printTree(tree.get_right()) #print all right child recursively
            


# test tree
if __name__ == '__main__':
	
    myTree = BinaryTree()
    arr = [8,3,1,6,4,7,10,14,13,70,9]
    for i in arr:
    	myTree.create(i)
    # print myTree.search(0)
    # print myTree.findMIN()
    # print myTree.findMAX()
        # myTree.Insert_left(4)
    #d=myTree.get_left()
    # myTree.Insert_left(2)
    # myTree.Insert_Right(9)
    # myTree.Insert_Right(5)
   
    #printTree(myTree)
    
    #myTree.inorder(myTree.root)
    print myTree.delete(myTree.root,10)
    # print myTree.search(6)




    
    #preorderREC(myTree)
        


		