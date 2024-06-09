from SinglyLinkedList import *

class Stack:
    def __init__(self,top=None):
        self.MyList= LinkedList()
        self.top=top

    def is_empty(self):
        if self.MyList.n==0:
            return True
        
    def push(self,data):
        self.MyList.insertAtBeginning(data)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            self.MyList.deletionFromBegining()

    def peak(self):
        if self.is_empty():
            print("stack is empty")
        else:
            return self.MyList.head.data
s1 = Stack()
print(s1.is_empty())
s1.push(10)
s1.push(20)
print(s1.MyList.n)
s1.pop()
print(s1.peak())