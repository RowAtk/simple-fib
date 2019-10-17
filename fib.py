def fib_check(lst):
    target = lst[0]
    counter = 0
    while target > fib(counter):
        counter+=1
    if counter != target:
        return False
    return lst == genFib(counter, counter + len(lst))


def fib(x):
    if x == 0:
        return 0
    elif x < 3:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def genFib(start, end):
    lst = []
    for i in range(start, end):
        lst += [fib(i)]
    return lst

# print(genFib(0,6))
print(fib_check([0,1,1,2,3,5]))
    

