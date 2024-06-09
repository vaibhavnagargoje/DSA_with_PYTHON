class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next


class Deque:
    def __init__(self):
        self.front =None
        self.rear=None
        self.count = 0

    def isEmpty(self):
        return self.front ==None 
    
    def insertFront(self,data):
        node = Node(data,None,self.front)

        if self.isEmpty():
            self.front=node
            self.rear=node
        else:
            self.front.prev=node
            node.next=self.front
            self.front=node
        self.count+=1

    def insertRear(self,data):
        node=Node(data,self.rear,None)

        if self.isEmpty():
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node
        self.count+=1

    def traverse(self):
        if self.isEmpty():
            print("Deque is empty")
        else:
            current =self.front
            while current:
                print(current.item,end=">")
                current=current.next
    
    def deleteFront(self):
        if self.isEmpty():
            print("Deque is empty..")
            return 0
        if self.front ==self.rear:
            data = self.front.item
            self.front=self.rear=None
            self.count-=1
            return data 
        else:
            data = self.front.item 
            self.front=self.front.next
            self.front.prev =None
            self.count-=1
            return data 

    def deletRear(self):
        if self.isEmpty():
            print("Deque is empty")
            raise IndexError("Deque is empty")

        if self.front==self.rear:
            data = self.rear.item
            self.front=self.rear=None
            self.count-=1

            return data
        else:
            data = self.rear.item

            self.rear=self.rear.prev
            self.rear.next=None
            self.count-=1
            return data
    
    def getRear(self):
        if (self.isEmpty()):
            raise IndexError("empty Deque")
        return self.rear.item
    
    def getFront(self):
        if(self.isEmpty()):
            raise IndexError("empty Deque")
        return self.front.item

    def size(self):
        return self.count
d1=Deque()

for i in range(5):
    d1.insertFront(i)


d1.traverse()
print()
d1.insertRear(50)
d1.traverse()
print()
d1.deletRear()
d1.deletRear()
d1.traverse()
print(d1.size())
print(d1.getFront())
print(d1.getRear())
