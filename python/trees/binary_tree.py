import Queue
class BinaryTree():
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
class BTOprs():
	def insert(self,root,data):
		newnode = BinaryTree(data)
		if root == None:
			root = newnode
			return root
		q = Queue.Queue()
		q.put(root)
		node = None
		while not q.empty():
			node = q.get()
			if node.left==None:
				node.left = newnode
				return root
			else:
				q.put(node.left)
			if node.right==None:
				node.right = newnode
				return root
			else:
				q.put(node.right)

bt = BTOprs()
root = bt.insert(None,10)
n1 = bt.insert(root,20)
n2 = bt.insert(root,30)
n3 = bt.insert(root,40)
n4 = bt.insert(root,50)
n5 = bt.insert(root,60)
