def iterative_fib(n):
    result = 0
    result2 = 1
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        holder = result
        for i in range(n-1):
            result = result2 + holder
            holder = result2
            result2 = result

    return (result)


print(iterative_fib(8))


# recursion

def rec_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        num1 = rec_fib(n-1)
        return num1 + rec_fib(n-2)


print(rec_fib(8))
