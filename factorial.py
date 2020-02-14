def factorial_loop(n):
    result = n
    for i in range(1, n):
        result = result * i
    return result


print(factorial_loop(5))


# Recursion
def fact_recursion(n):
    if n == 1:
        return n
    else:
        return n*fact_recursion(n-1)


print(fact_recursion(6))
