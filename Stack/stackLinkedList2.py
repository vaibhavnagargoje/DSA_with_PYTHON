class Node:
    def __init__(self,dada=None,next=None):
        self.data=dada
        self.next=next

class Stack:
    def __init__(self,node=None):
        self.n = 0
        self.head=node

    def isEmpty(self):
        if self.head==None:
            return True
        return False

    def push(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
        self.n+=1
    
    def pop(self):
        if self.isEmpty():                  
            return None
        data =self.head.data
        self.head=self.head.next
        self.n-=1
        return data
    

