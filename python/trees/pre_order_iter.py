from binary_tree import BTOprs
def pre_order(root,l):
	stack = []
	stack.append(root)
	node = None
	while len(stack)!=0:
		node = stack.pop()
		if node!=None:
			l.append(node.data)
			stack.append(node.right)
			stack.append(node.left)
bt = BTOprs()
root = bt.insert(None,10)
n1 = bt.insert(root,20)
n2 = bt.insert(root,30)
n3 = bt.insert(root,40)
n4 = bt.insert(root,50)
n5 = bt.insert(root,60)
l = []
pre_order(root,l)
print l


		