class Node:
	data = None
	link = None

class SingleLL:
	head = None
	def addNodeAtEnd(self,data):
		if self.head==None:
			node = Node()
			node.data = data
			self.head = node
		else:
			temp = self.head
			while temp.link!=None:
				temp = temp.link
			node = Node()
			node.data = data
			temp.link = node
	def addNodeAtBeg(self,data):
		node = Node()
		node.data = data
		if self.head==None:
			self.head = node
		else:
			node.link = self.head
			self.head = node
	def addNodeAtPos(self,data,pos):
		node = Node()
		node.data = data
		temp = self.head
		if pos==1:
			self.addNodeAtBeg(data)
			return
		while pos-2!=0:
			pos-=1
			temp = temp.link
		node.link = temp.link
		temp.link = node

	def delete_node(self,pos):
		if pos==1:
			self.head = self.head.link
			return
		else:
			count = 1
			cur  = self.head
			prev = None
			while count<pos:
				prev = cur
				cur = cur.link
				count += 1
			prev.link = cur.link


	def print_ll(self):
		temp = self.head
		while temp!=None:
			print temp.data
			temp = temp.link

sll = SingleLL()
sll.addNodeAtEnd(1)
sll.addNodeAtEnd(2)
sll.addNodeAtEnd(3)
sll.addNodeAtEnd(4)
sll.addNodeAtBeg(0)
sll.addNodeAtPos(10,2)
sll.addNodeAtPos(11,1)
sll.delete_node(3)
sll.print_ll()


