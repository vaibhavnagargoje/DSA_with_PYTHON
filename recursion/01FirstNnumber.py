def N_numbers(num):
    if num==0:
        return
    N_numbers(num-1)
    print(num)
N_numbers(10)