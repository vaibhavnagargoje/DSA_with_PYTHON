
class Node:
    def __init(self,data=None,next=None):
        self.data=data
        self.next =next
    
class LinkedList:
    def __init__(self,head=None):
        self.head=head
        self.n=0

    def InsertAtFirst(self,data):
        newNode=Node()
        newNode.data=data
        newNode.next=self.head
        self.head=newNode
        self.n+=1


    def traverse(self):
        current =self.head

        while current!=None:
            print(current.data,end="-> ")
            current=current.next

    def makeLoop(self,data):
        current= self.head
        count=0
        temp= self.head
        while current.next!=None:
            if count<=4:
                temp=temp.next
                count+=1

            current=current.next
        current.next=temp

    def deletCycleStart(self):
        if self.head ==None or self.head.next==None:
            return None
        slow = self.head.next
        fast = slow.next

        while slow!=fast:
            slow=slow.next
            try:
                fast=fast.next.next
            except AttributeError:
                return None
        slow=self.head
        while slow!=fast:
            slow = slow.next
            fast=fast.next
        return slow 


    def detectCycle(self):
        if  self.head==None or  self.head.next==None:
            return False
        

        slowptr=self.head
        fastptr=self.head.next

        while fastptr!=None and fastptr.next!=None:
            if slowptr == fastptr:
                return True
            slowptr  = slowptr.next
            fastptr =fastptr.next.next
        return False

        


    def ReverseList(self):
        #Iterative Version
        prev = None
        current =self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        self.head = prev
    
    def EvenOrOdd(self):
        current = self.head
        while current!= None and current.next!=None:
            current=current.next.next
            if current==None:
                return 1
            
        return 0
            
                


l1=LinkedList()
l1.InsertAtFirst(10)
l1.InsertAtFirst(20)
l1.InsertAtFirst(30)
l1.InsertAtFirst(40)
l1.InsertAtFirst(50)
l1.InsertAtFirst(60)
l1.InsertAtFirst(70)
l1.InsertAtFirst(80)
l1.InsertAtFirst(90)
# l1.makeLoop(100)
# print(l1.deletCycleStart())
print(l1.detectCycle())


# l1.traverse()
print(l1.EvenOrOdd())
print()

# l1.ReverseList()

l1.traverse()

