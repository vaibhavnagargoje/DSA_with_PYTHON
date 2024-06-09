class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        self.last=None

    

class Stack:
    def __init__(self,limit =10):
        self.stk=[]
        self.limit=limit
        
    def isEmpty(self):
        return len(self.stk)==0
    
    def push(self,data):
        if len(self.stk)>self.limit:
            print("stak overflow")
            return 0
        else:
            self.stk.append(data)
        print("item  pushed ",self.stk)
    
    def pop(self):
        if self.isEmpty():
            print("stak underflow")
            return 0
        data= self.stk.pop()
        print("item poped ",data)
        print("data poped",self.stk)
    
    def peak(self):
        if not self.isEmpty():
            print(self.stk[-1])
        else:
            print("stack underflow")
        
    def size(self):
        return len(self.stk)
    




        
class Queue:
    def __init__(self,data=None):
        self.front=None
        self.rear=None
        self.size=0
    
    def enqueue(self,data):
        self.lastNone = self.front
             
