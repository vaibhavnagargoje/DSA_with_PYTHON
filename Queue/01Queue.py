
class Queue:
    def __init__(self,limit=5):
        self.que=[]
        self.limit =limit
        self.front=None
        self.rear=None
        self.size = 0
    
    def isEmpty(self):
        return self.size ==0
    
    def enQueue(self,data):
        if self.size ==self.limit:
            print("Queue Full")
            raise IndexError("OverFlow")

        
        else:
            self.que.append(data)

        if self.front ==None:
            self.front =self.rear=0
        else:
            self.rear = self.size
        self.size+=1
        print("Queue after Enqueue ",self.que)
    
    def Dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            raise IndexError(" Empty Queue")
        else :
            data = self.que.pop(0)
            self.size-=1
        if self.size == 0:
            self.front = self.rear =None
        else:
            self.rear =self.size-1
        print("Queue is after Dequeue",self.que)
        return data
    

    def size(self):
        return self.size
    
    def getFornt(self):
        if self.size==0:
            print("queue is empty")
        else:
            return self.front
        
    def get_rear(self):
        if self.size == 0:
            print("queue is empty")
        else:
            return self.rear




q1 =Queue()
q1.enQueue(10)
q1.enQueue(20)
q1.enQueue(40)
print(q1.Dequeue())
print(q1.Dequeue())
print(q1.Dequeue())
print(q1.get_rear())