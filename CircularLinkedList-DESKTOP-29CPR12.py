class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class CircularLinkedList:
    def __init__(self,node=None):
        self.length= 0
        self.head=node
    
    def traverse(self):
        if self.head == None:
            print("list is empty")
            return
        else:
            current = self.head
            
            while current.next!=self.head:
                print(current.data, end=" ")
                current= current.next
            print(current.data)
    
    def InsertAtBegining(self,data):
        current = self.head
        newNode = Node()
        newNode.data=data
        newNode.next=newNode
        if self.head==None:
            self.head=newNode
            newNode.next=self.head
            
            

        else:
            while current.next!=self.head:
                current=current.next
            current.next=newNode
            newNode.next=self.head
            self.head=newNode
        self.length+=1


    def InsertAtEnd(self,data):
        current = self.head 
        newnode = Node(data)
        newnode.next= newnode

        if current==None:
            self.head=newnode
        
        else:
            while current.next!=self.head:
                current= current.next
            current.next = newnode
            newnode.next=self.head
        self.length+=1
      
            
    
    def insertAtPosition(self,pos,data):

        if pos>self.length or pos<=0:
            print("Invalid Index or Out Of range Index")
        
        else:
            if pos==1:
                self.InsertAtBegining(data)
            elif pos == self.length:
                self.InsertAtEnd(data)
            else:
                current = self.head
                counter =1
                newNode = Node(data)
                while counter<pos-1:
                    counter+=1
                    current = current.next
                newNode.next= current.next
                current.next= newNode
                self.length+=1

    def deletAtBegining(self):
      
        
        current = self.head
        while current.next!= self.head:
            current=current.next
        current.next=self.head.next
        self.head=current.next
        self.length-=1


    def search(self,data):
        temp = self.head
        if temp==None:
            print("list is Empty")
        else:
            while temp.next!=self.head:
                if temp.data==data:
                    return temp
                temp =temp.next
            if temp.data==data:
                return temp
            return None


class CLLIterrator:
    def __init__(self,start):
        self.current=start
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current==None:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        if self.current


s1 = CircularLinkedList()

s1.InsertAtBegining(3)
s1.InsertAtBegining(33)
s1.InsertAtBegining(22)

s1.InsertAtEnd(55)

s1.insertAtPosition(2,222)
s1.deletAtBegining()
s1.deletAtBegining()
print(s1.search(55).data)

print(s1.length)
s1.traverse()