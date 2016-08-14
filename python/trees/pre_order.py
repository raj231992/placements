from binary_tree import BTOprs
def preOrder(node,l):
	if not node:
		return
	l.append(node.data)
	preOrder(node.left,l)
	preOrder(node.right,l)

bt = BTOprs()
root = bt.insert(None,10)
n1 = bt.insert(root,20)
n2 = bt.insert(root,30)
n3 = bt.insert(root,40)
n4 = bt.insert(root,50)
n5 = bt.insert(root,60)
l = []
preOrder(root,l)
print l