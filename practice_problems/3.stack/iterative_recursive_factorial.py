def recursive_factorial(n):
    def _factorial(n, product):
        if n == 1:
            return product
        else:
            return _factorial(n - 1, product*n)
    return _factorial(n, 1)


print(recursive_factorial(3))


def iterative_factorial(n):
    result = 1
    for num in range(1, n+1):
        result *= num
    return result


print(iterative_factorial(3))


def iterative_stack_factorial(n):
    from impl.stack import Stack
    result = Stack()
    result.push(1)

    for num in range(1, n+1):
        result.push(result.pop * num)
    return result.top


print(iterative_factorial(3))
