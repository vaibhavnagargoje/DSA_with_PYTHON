def FirstEven(n):
    if n>0:
        FirstEven(n-1)
        print(n*2)

def Reverse(n):
    if n>0:
        print(n*2)
        Reverse(n-1)
FirstEven(5)
Reverse(5)