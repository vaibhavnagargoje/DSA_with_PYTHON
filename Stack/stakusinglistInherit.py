class stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,data):
        
        self.append(data)
        
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            print("stack is empty")
    
    def peak(self):
        if not self.is_empty():
            return self[-1]
        else:
            print("stack is empty")

    def size(self):
        return len(self)

    def insert(self,**args):
        return AttributeError(" No attribute 'insert' in stack ")
    

s1 = stack()
s1.push(44)
print(s1.peak())
s1.push(55)
print(s1.pop())
s1.pop()
print(s1.size())