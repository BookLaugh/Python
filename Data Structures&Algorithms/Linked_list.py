class Node:
	def __init__(self,data=None):
		self.data = data
		self.next = None

def count_Nodes(head):
	# assuming that head != None
	count = 1
	current = head
	while current.next != None:
		current = current.next
		count+=1
	return count

nodeA = Node(2)
nodeB = Node(3)
nodeC = Node(10)
nodeD = Node(2)
nodeE = Node(5)
nodeF = Node(7)
nodeG = Node(8)
nodeH = Node(4)


nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG
nodeG.next = nodeH

print("The length of linked list is : ") # should be 5
print(count_Nodes(nodeA)) # should return us 6
