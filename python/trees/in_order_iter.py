from binary_tree import BTOprs
def in_order(root,l):
	stack = []
	stack.append(root)
	node = root
	while len(stack)!=0 or node!=None:
		if node.left:
			stack.append(node.left)
		else:
			node = stack.pop()
			l.append(node.data)
			if node.right:
				stack.append(node.right)
			else:
				node = stack.pop()