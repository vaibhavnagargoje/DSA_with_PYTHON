class Stack:
    def __init__(self,Capacity=1):
        self.top=-1
        self.Capacity = Capacity
        self.A = [None]*Capacity

    def isFull(self):
        if self.Capacity==self.top+1:
            return True
        return False
             
    def isEmpty(self):
        if self.top ==-1:
            return True
        return False
    
    def resize(self):
        self.Capacity = self.Capacity*2
        Newarray = [None]*self.Capacity
        if Newarray is None :
            print(" Your Machine is not Capabal ! Use big machine")
            return
        else:
            for i in range(self.top+1):
                Newarray[i]=self.A[i]
            self.A=Newarray
            print("Your Stack is Resized !")

    def push(self,data):
        if self.Capacity==self.top+1:
            print("Stack is full")
            print("Trying to Resize ")
            self.resize()

        if self.isFull():
            print("stack is Overfull")
            return
        self.top=self.top+1
        self.A[self.top]=data
        print("Data is pushed !")

    def pop(self):
        if self.isEmpty():
            print("stack underflow")
            return
        data = self.A[self.top]
        self.top-=1
        if self.top<self.Capacity//2:
            print("resize the Capacity Of Stacks")
            self.Capacity//=2
            newArray=[None]*self.Capacity
            for i in range(self.top+1):
                newArray[i]=self.A[i]
            self.A=newArray
        return data
    
    def peak(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("The Top Element is : ",self.A[self.top])
            


s1 = Stack()
s1.push(10)
print(s1.top,s1.Capacity)
s1.push(20)
print(s1.top,s1.Capacity)
s1.push(30)
print(s1.top,s1.Capacity)
s1.push(40)
print(s1.top,s1.Capacity)
s1.push(50)
print(s1.top,s1.Capacity)
s1.push(60)
print(s1.top,s1.Capacity)
s1.push(70)
print(s1.top,s1.Capacity)
s1.push(80)
print(s1.top,s1.Capacity)
s1.push(90)
print(s1.top,s1.Capacity)
s1.peak()

s1.pop()
print(s1.top,s1.Capacity)
s1.pop()
print(s1.top,s1.Capacity)
s1.pop()
print(s1.top,s1.Capacity)
s1.pop()
print(s1.top,s1.Capacity)
s1.pop()
print(s1.top,s1.Capacity)
