
class Stack(list):    

    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)    
    
    def pop(self):
        if not self.is_empty():

            return super().pop()
       

    

            


def ValidateExpression(expression):
        stack = Stack()
        mapping={")":"(","}":"{","]":"["}

      
        for symbol in expression:
            if symbol in mapping:
                print(symbol)
                top_element = stack.pop() if stack else "#"
                if mapping[symbol]!=top_element:
                     return False
            else:
                stack.push(symbol)
        return not stack

print(ValidateExpression(")"))




