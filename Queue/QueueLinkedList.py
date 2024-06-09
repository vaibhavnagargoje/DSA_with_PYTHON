class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.Counter =0

    def is_empty(self):
        return self.front ==None

    def enqueue(self,data):
        n= Node()
        n.data=data
        if self.is_empty():
            self.front=n
            self.rear=n
        else:
            self.rear.next=n
            self.rear=n
        self.Counter+=1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty" )

        elif (self.front==self.rear):
            data=self.front.data
            self.front=None 
            self.rear=None
            return data
        else:
            data = self.front.data
            self.front=self.front.next 
            self.Counter-=1
            return data
    def get_front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.front.data
        
    def get_rear(self):
        
        if self.is_empty():
            print("Empty Queue")
        
        else:
            return self.rear.data
    def size(self):
        return self.Counter

    def traverse(self):
        if self.is_empty():
            print("queue is empty")
        else:
            current = self.front
            while current!=None:
                print(current.data,end=" < ")
                current=current.next

        
    

q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print(q1.size())
q1.traverse()
print("dequeue element " ,q1.dequeue())
print("dequeue element " ,q1.dequeue())
# print("dequeue element " ,q1.dequeue())
# print("dequeue element " ,q1.dequeue())
# print("dequeue element " ,q1.dequeue())
print(q1.get_front())
print(q1.rear.data)
print(q1.get_rear())