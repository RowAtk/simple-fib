# Functon to find the nth fib number in the sequence
def fib(x):
    if x == 0:
        return 0
    elif x < 3:
        return 1
    else:
        return fib(x-1) + fib(x-2)



