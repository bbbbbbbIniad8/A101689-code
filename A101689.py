import math

def fib(n):
    lst = [0,1]
    if n == 0:
        return 0
    for i in range(1,n + 1):
        lst[i % 2] = lst[i % 2] + lst[(i + 1) % 2]
    return lst[i % 2]

def A101689(zero_index = True):
    result = []
    sum = 0
    n = input("n = ")
    if zero_index == False:
        sum += 1
    for i in range(1, int(n) + 1):
        result.append(fib(i))
        sum += 1/(math.prod(result))
    print(sum)

A101689(False)