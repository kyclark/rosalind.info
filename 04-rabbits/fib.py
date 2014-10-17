
def fib(n):
    last = [0,1]
    for i in range(n):
        next = sum(last)
        last.pop(0)
        last.append(next)
        yield next
