def FirstOdd(num):
  
    if num>0:
        FirstOdd(num-1)
        print(num*2-1)

def Reverse(n):
    if n>0:
        print(n*2-1)
        Reverse(n-1)
FirstOdd(10)

Reverse(10)