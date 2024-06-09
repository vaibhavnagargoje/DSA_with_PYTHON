class Queue:
    def __init__(self,limit =10):
        self.items=[]
        # self.front =None
        # self.rear = None
        self.limit =limit

    def is_empty(self):
        return len(self.items)==0
    
    def enqueue(self,data):
        self.items.append(data)
       

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def get_fornt(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return False
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return False 
    def size(self):
        return len(self.items)
    
    def traverse(self):
        for i in range(len(self.items)):
            print(self.items[i],end="<")

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.traverse()
q.dequeue()
print()
q.traverse()
print()
print(q.get_fornt())
print(q.get_rear())