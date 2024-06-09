def reverseN(num):
    if num>0:
        print(num)
        reverseN(num-1)

reverseN(10)