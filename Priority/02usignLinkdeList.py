class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item = item
        self.priority= priority
        self.next = next


class PriorityQueue:
    def __init__(self,node=None):
        self.size=0
        self.head=node

    def isEmpt(self):
        return self.size==0
    
    def push(self,data,priority):
        newNode= Node(data,priority)

        if not self.head or priority<self.head.priority:
            newNode.next=self.head
            self.head=newNode

        else:
            current= self.head
            prev= self.head
            while current.next and current.next.priority<=priority:
                current=current.next
            newNode.next=current.next
            current.next=newNode

        self.size+=1

    def traverse(self):
        if self.isEmpt():
            print("list is empty")
        
        else:
            current=self.head
            while current!=None:
                print(current.item,"-",current.priority ,end="<- :")
                current=current.next
    
    def pop(self):
        if self.isEmpt():
            print("Linked List is empty")
            return 

        data,priority = self.head.item,self.head.priority
        self.head=self.head.next
        self.size-=1
        return data,priority
    @staticmethod
    def siz():
        return pq.size


pq= PriorityQueue()
pq.push(10,1) 
pq.push(10,3)
pq.push(10,5)
pq.push("vaibhav",1)
print(pq.pop())
pq.traverse()
print(pq.siz())