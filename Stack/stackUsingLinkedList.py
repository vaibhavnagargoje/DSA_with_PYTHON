class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=None

class Stack:
    def __init__(self,top=None):
        self.top =top
        self.counter = 0

    def is_empty(self):
        return self.top==None
    
    def push(self,data):
        newtop= Node(data)
        newtop.next = self.top
        self.top=newtop
        self.counter+=1

    def pop(self):
        if self.is_empty():
            print("stack Underflow")
        
        else:
            data = self.top.data
            self.top=self.top.next 
            self.counter-=1
            return data
        

    def peak(self):
        if self.is_empty():
            print("stack Underflow")
        else:
            return self.top.data
    
    def size(self):
        return self.counter
    
    

s1 = Stack()
s1.push(55)
s1.push(33)
print(s1.pop())
s1.push(88)
print(s1.pop())
print(s1.peak())