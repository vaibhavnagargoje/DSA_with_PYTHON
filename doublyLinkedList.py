class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next = next
        self.prev= prev


class DoublyLinkedList:

    def __init__(self,node= None):
        self.n =0
        self.head = node
        
    
    def insertAtBegining(self,data):
        
        newNode= Node()
        newNode.data = data

        if self.n ==0:
            self.head = newNode

        
        else:
            newNode.prev=None
            newNode.next =self.head
            self.head.prev = newNode
            self.head = newNode
        self.n+=1

    def traverse(self):
        
        current = self.head
        while current!= None:
            print(current.data, end=" ")
            current = current.next
        
    def insertAtEnt(self,data):
        if(self.head == None):
            newNode = Node()
            newNode.data=data
            self.n+=1
        else:
            newNode = Node()
            newNode.data=data
            current = self.head
            while current.next!=None:
                current= current.next
            newNode.prev = current
            current.next= newNode
            newNode.next = None
            self.n+=1

    def insertAtGivenPosition(self,pos,data):
        if pos<=0 or pos>self.n:
            print("Invalid index or Out of Range")
        else:
            if pos ==1 or self.head==None:
                self.insertAtBegining(data)
            elif(pos==self.n):
                self.insertAtEnt(data)
            else:
                newNode = Node()
                newNode.data=data
                current = self.head

                counter =1
                while  counter<pos-1:
                    counter+=1
                    current =current.next
                newNode.next=current.next
                current.next.prev= newNode
                current.next=newNode
                newNode.prev= current

    ### deletion 

    def deletfirst(self):
        if self.head ==None:
            print("List is Empty ")
        else:
            temp= self.head
            self.head = self.head.next
            self.head.prev= None
            self.n-=1
            return temp
    
    def deleteLast(self):
        if self.head==None:
            print("List Is empty")
        else:
            current = self.head
            prev = self.head
            while current.next!=None:
                prev= current
                current= current.next
            current.prev = None
            prev.next=None
            self.n-=1



    def deletAtPosition(self,pos):
        if self.n==0:
            print("List is Emplty ")
        elif pos <0 or pos > self.n:
            print("Invalid Position Given")
        else:
            if pos ==self.n:
                self.deleteLast()
            elif pos == 1:
                self.deletfirst()
            else:
                counter = 1
                current = self.head
                prev = self.head

                while counter !=pos:
                    prev = current
                    current= current.next
                    counter+=1
                prev.next= current.next
                current.next.prev = prev
                return current
            

n1 = DoublyLinkedList()

n1.insertAtBegining(3)
n1.insertAtBegining(3)
n1.insertAtBegining(2)

n1.insertAtEnt(333)



n1.traverse()
print(n1.n)
n1.insertAtBegining(872)
n1.insertAtEnt(200)
print()
n1.traverse()
print()
n1.insertAtGivenPosition(-1,999)
n1.traverse()

print("Deletiig Operations ")
print("node is deleted form begining ",n1.deletfirst().data)
print(n1.head.prev)
n1.traverse()
print()
n1.deleteLast()
n1.traverse()
print(n1.head.next.next.next.prev.data)


n1.deletAtPosition(3)
n1.traverse()

# print(n1.head.next.next)

