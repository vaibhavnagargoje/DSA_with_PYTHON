class Stack:
    def __init__(self,Capacity=5):
        self.top=-1
        self.Capacity =Capacity
        self.A=[None]*Capacity
    
    def push(self,data):
        if self.Capacity == self.top+1:
            print("Stack Overflow")
        else:
            self.top+=1
            self.A[self.top]=data
    
    def pop(self):
        if self.top ==-1:
            print("stack Underflow")
            return
        else:
            temp = self.A[self.top]
            self.top -=1
            if self.top < self.Capacity//2:
                print("trying to resize: Decrease")
                self.Capacity=self.Capacity//2
                newArray =[None]*self.Capacity
                for i in range(0,self.top+1):
                    newArray[i]=self.A[i]
                self.A=newArray
            return temp
    def peak(self):
        if self.top ==-1:
            print("stack is Underflow")
            return
        return self.A[self.top]  # here we can also  write/ return self.A[-1] , because  in python -ve indexing is present for -1 is return last element of the Array .
    
    def isFull(self):
        return self.Capacity ==self.top+1
    
    def isEmpty(self):
        return self.top ==-1
    

stack=Stack()
stack.push(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.peak())
print(stack.isFull())
print(stack.isEmpty())