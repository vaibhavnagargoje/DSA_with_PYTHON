class stack:
    def __init__(self,):
        self.list =[]
        

    def push(self,data):
        self.list.append(data)

    def is_empty(self):
        return len(self.list)==0
    
    def lenght(self):
        return len(self.list)
    
    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        else:
            raise IndexError("statck is empty")
    
    def peak(self):
        if not self.is_empty():
            return self.list[-1]
        raise ValueError("stack is emppty")
    
    def insert(self,*args):
        raise ValueError("attribut not found")



s1= stack()
s1.push(5)
s1.push(5)
s1.push(5)
s1.push(33)
print(s1.lenght())
# print(s1.pop())
print(s1.peak())
s1.insert(43,34)