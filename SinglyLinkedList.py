

class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList():
    def __init__(self,node=None):
        self.n = 0
        self.head = node

    def length(self):
        current = self.head
        count =0
        while count!=None:
            count+=1
            current= current.next
        return count
    
    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.data=data
        if self.n == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.n+=1


    def insertAtEnd(self,data):
        newNode= Node()
        newNode.data=data
        current = self.head
        while current.next!=None:
            current= current.next
        current.next=newNode
        self.n +=1
    
    def insertAtGivenPosition(self, data,pos):
        if (pos>self.n or pos<0):
            return None
        else:
            if pos==0:
                self.insertAtBeginning(data)
            else:
                if pos==self.n:
                    self.insertAtEnd(data)
                else:
                    newNode= Node()
                    newNode.data = data
                    count =1
                    current = self.head
                    while count< pos-1:
                        count +=1
                        current= current.next
                    newNode.next =current.next
                    current.next = newNode
                    self.n+=1
    
    #### deletion singly Linked list

    def deletionFromBegining(self):
        if self.n==0:
            print("The list is Empty")
        else:
            self.head=self.head.next
            self.n-=1
    
    def deleteLastNode(self):
        if self.n==0:
            print("empty linked List")
        else:
            current = self.head
            prevnode = self.head
            while current.next!=None:
                prevnode = current
                current=current.next
            prevnode.next =None
            self.n-=1
    

    def deleteWithValue(self,value):
        current= self.head
        prevnode = self.head
        while (current.next != None or current.data==value):
            
            if current.data == value:
                prevnode.next =current.next
                self.n-=1
                return
            else:
                prevnode=current
                current=current.next
        print("the value provided is not present")
    

    def deleteAtPosition(self,pos):
        count = 0
        current = self.head
        prevnode = self.head
        if pos>self.n or pos<0:
            print("the position Does Not Exit..")
        else:
            while count<pos:
                count+=1
                if count == pos:
                    prevnode.next=current.next
                    self.n-=1
                    return
                else:
                    prevnode=current
                    current=current.next
        
    def deletLinkedlistNode(self,node):
        if self.n ==0:
            raise ValueError("List is Empty")
        
        else:
            current = self.head
            prevnode = None
            found = False
            
            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError("Node not in Linked List")
                
                else:
                    prevnode = current
                    current= current.next
        if prevnode is None:
            self.head = current.next
        else:
            prevnode= current.next
        self.n-=1

    
    def traverse(self):
        currnt = self.head

        while( currnt!=None):

        
            print(currnt.data, end =", ")
            currnt = currnt.next
        
        




    def delsinglylinkedList(self):
        self.head=None



if __name__=="__main__":


    s1 = LinkedList()
    s1.insertAtBeginning(11)
    s1.insertAtBeginning(55)
    s1.insertAtBeginning(22)
    s1.insertAtBeginning(43)
    s1.insertAtBeginning(16)
    s1.insertAtBeginning(50)
    s1.traverse()
    s1.insertAtBeginning(11)
    print()
    s1.traverse()
    print()
    # s1.deleteLastNode()
    print(s1.n)
    s1.deleteWithValue(11)
    s1.deleteAtPosition(3)



    s1.insertAtEnd(777)
    s1.traverse()
    print()
    s1.insertAtGivenPosition(999,2)
    s1.traverse()
    print()
    print(s1.n)
