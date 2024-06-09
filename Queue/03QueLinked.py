class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    


class Queue:
    def __init__(self):
        self.fornt =None
        self.rear=None
        self.size=0
    
    def traverse(self):
        if self.is_empty():
            print("cannot print ! stack empty")
        else:
            current =self.fornt
            while current!=None:
                print(current.data,end="<-")
                current=current.next


    def Enqueue(self,data):
        node =Node()
        node.data=data
        if self.fornt==None:
            self.fornt=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node
        self.size+=1
        self.traverse()
        print()
    def Dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return 0
        else:
            data = self.fornt.data
            self.fornt=self.fornt.next
            self.size-=1
            return data
    
    def is_empty(self):
        return self.size==0
    


q1= Queue()
q1.Enqueue(10)
q1.Enqueue(20)
q1.Enqueue(30)
q1.Dequeue()
q1.Dequeue()
q1.Dequeue()
q1.Dequeue()


q1.traverse()