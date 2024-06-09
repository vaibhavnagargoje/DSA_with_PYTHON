class Deque:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return len(self.items)==0
    
    def insertFront(self,data):
        self.items.insert(0,data)

    def insertRear(self,data):
        self.items.append(data)
    
    def deletFront(self):
        if not self.isEmpty():

            self.items.pop(0)
        else:
            print("list is not empty")
            return 0
    
    def deletRear(self):
    
        if not self.isEmpty():
            self.items.pop()
        else:
            print("list is not empty")
            return 0 
    
    def getFront(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            print("deque is empty")
        
    def getRear(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("deque is empty")
    
    def size(self):
        return len(self.items)




d1 = Deque()
d1.insertFront(1)
d1.insertFront(2)
d1.insertRear(3)
d1.insertRear(4)
d1.insertRear(5)

print(d1.items)
d1.deletFront()
d1.deletRear()
print(d1.getFront(),d1.getRear())
print(d1.items)