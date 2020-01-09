class Node :
	def __init__(self,value=None):
		self.value=value
		self.next=None

	def GetData(self):
		return self.value

	def GetNext(self):
		return self.next

	def SetNext(self,NewNode):
		self.next=NewNode

class LinkedList:
	def __init__(self):
		self.head=None

	def Print(self):
		node=self.head
		if node==None:
			print("linked-list is empty")
		else:
			while node.next!=None:
				print(node.value.value,'-->',end=' ')
				node=node.next
			print(node.value.value)

	def InsertAtBegining(self,data):
		NewNode=Node(data)
		NewNode.next=self.head
		self.head=NewNode

	def InsertAtEnd(self,data):
		NewNode=Node(data)
		if self.head==None:
			self.head=NewNode
		else:
			node=self.head
			while(node.next!=None):
				node=node.next
			node.next=NewNode
	def Add(self,data):
		self.InsertAtEnd(data)

	def Size(self):
		count=0
		current=self.head
		while current!=None:
			count+=1
			current=current.next
		return count

	def DeleteAtEnd(self):
		current=self.head
		if current==None :
			print("linkedlist is empty")
			return None
		elif current.next==None:
			self.head=None
			return current.value
		else:
			follow=current
			while(current.next!=None):
				follow=current
				current=current.next
			follow.next=None
			return current.value

	def DeleteAtBegining(self):
		current=self.head
		if current==None or current.next==None:
			return self.DeleteAtEnd()
		self.head=current.next
		return current.value if current!=None else None

	def Delete(self):
		return self.DeleteAtBegining()

	def InsertThroughList(self,listeddata):
		for key in listeddata:
			self.InsertAtEnd(key)

	def InsertAfterData(self,Afterdata,data):
		NewNode=Node(data)
		current=self.head
		if current==None:
			print("invalid operation")
		else:
			while (current.value!=Afterdata):
				if current.next==None:
					print("invalid operation ")
					print('Element is not present ')
				current=current.next
			NewNode.next=current.next
			current.next=NewNode

	def DeleteAfterData(self,Afterdata):
		current=self.head
		if current==None:
			print("invalid operation ")
			return
		while current.value!=Afterdata:
			if current.next==None:
				print("invalid operation ")
				print('Element is not present ')
				return
			current=current.next
		if current.next==None:
			print("invalid operation")
			return
		else:
			DeletedNode=current.next
			current.next=DeletedNode.next
			return DeletedNode







#data=linkedlist()
#data.InsertThroughList([1,2,3,4,5,6])
#value=data.DeleteAfterData(6)
#print(value)
#data.Print()
