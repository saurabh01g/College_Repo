def fun(x,y):
    return x+y

print(fun(10,20))

def mul(x,y):
    return x*y

print(mul(20,10))


# decorator to calculate execution time
from time import time
def mydeco(func):
    def wrapper(n):
        start_time = time()
        func(n)
        end_time = time()
        total_time = end_time -start_time
        print(total_time)
    return wrapper

@mydeco     #custom decorator
def myfunc(n):
    for i in range(n):
        n += 1
    
myfunc(100000)