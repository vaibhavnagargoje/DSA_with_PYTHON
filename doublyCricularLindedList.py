class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data =data
        self.next=next
        self.prev=prev

class DoublySLL:
    def __init__(self,node=None):
        self.last=node
        self.length=0

    def insertAtBegining(self,data):
        newNode = Node(data)
        newNode.next=newNode
        newNode.prev=newNode
        if self.last==None:
            self.last=newNode
        else:
            current=self.last
            newNode.next= current.next
            newNode.next.prev=newNode
            newNode.prev=current
            current.next=newNode
        self.length+=1

    def InsertAtLast(self, data):
        newNode = Node(data)
        newNode.next=newNode
        newNode.prev = newNode
        if self.last ==None:
            self.insertAtBegining(data)
        else:
            temp = self.last
            newNode.next=temp.next
            temp.next.prev=newNode
            newNode.prev=temp
            temp.next=newNode
            self.last=newNode
        self.length+=1


    def travasers(self):
        if self.last==None:
            print("the list is empty")
        else:
            current = self.last.next
            while current!=self.last:
                print(current.data,end ="-> ")
                current=current.next
            print(current.data)
    

s1 = DoublySLL()
s1.insertAtBegining(2)
s1.insertAtBegining(3)
s1.insertAtBegining(4)
s1.insertAtBegining(5)
s1.InsertAtLast(6)
s1.travasers()
print(s1.last.prev,s1.last.next,s1.last)
