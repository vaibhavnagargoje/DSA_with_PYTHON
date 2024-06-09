class Queue():
    def __init__(self,limit=5):
        self.que = []
        self.front = None
        self.rear = None
        self.limit = limit
        self.size =0

    def Enqueue(self,data):
        if self.size >= self.limit:
            print("Queue is Full .. Resizing the Queue")
            self.resize()
        self.que.append(data)
        if self.front==None:
            self.front=self.rear=0
        else:
            self.rear=self.size
        self.size+=1
        print("after Enque:",self.que)

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return 0
        data = self.que.pop(0)
        self.size-=1
        self.rear=self.size
        print("after dequeue:",self.que)

        return data
    
    def getFront(self):
        if self.is_empty():
            print("Queue is empty")
            return None 
        else:
            return self.que[self.front]
        
    def getRear(self):
        if self.is_empty(self):
            print("Queue is empty")
            return None
        return self.que[self.rear]


    def is_empty(self):
        return self.size==0
        


    
    def resize(self):
        newQueue = list(self.que)
        self.limit = self.limit*2
        self.que=newQueue
        print("Resize Done ")


    
q1= Queue()
q1.dequeue()
q1.Enqueue(5)
q1.Enqueue(10)
q1.Enqueue(15)
q1.Enqueue(20)
q1.Enqueue(25)
q1.Enqueue(30)
# q1.dequeue()
print(q1.size)
print(q1.limit)
