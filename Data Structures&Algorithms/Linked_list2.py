class Node:
	def __init__(self,data=None):
		self.data = data
		self.next = None

class Linked_list:
	def __init__(self):
		self.head = Node()


	def append(self,data): # this  for adding data or value to the list
		new_node = Node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node # this will be new_node which is added to the list


	def length(self): # this will give us number a number of nodes in a linked list
		cur = self.head
		total = 0
		while cur.next != None:
			total += 1
			cur = cur.next
		return total

	def display(self): # This one diplays us, all elements in our linked list
		elems = []
		cur_node = self.head
		while cur_node.next != None:
			cur_node = cur_node.next
			elems.append(cur_node.data)
		print(elems)

	def get_node(self,index):
		if index>=self.length():
			print("Error: Index out of range")
			return 	None
		cur_idx = 0
		cur_node = self.head
		while True:
			last_node = cur_node
			cur_node = cur_node.next

			


	def delete(self,index):
		if index>=self.length():
			print("Error: Index out of range")
			return 	None
		cur_idx = 0
		cur_node = self.head
		while True:
			last_node = cur_node
			cur_node = cur_node.next
			if cur_idx == index:
				last_node.next = cur_node.next
				return
			cur_idx+=1


# This part depends on your own examples
# This mine one 

my_list = Linked_list()

my_list.append(2)
my_list.append(7)
my_list.append(6)
my_list.append(10)
my_list.append(9)

my_list.display()

