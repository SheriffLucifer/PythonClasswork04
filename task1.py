def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(7))

########################################

num = int(input('Please input number: '))


def fibonachy(n):
    if n <= 1:
        return n
    return fibonachy(n - 1) + fibonachy(n - 2)


print(fibonachy(num))