def fibonacci(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        yield a
        i = i+1
        future = a + b
        a = b
        b = future


for item in fibonacci(10):
    print(item,end='\t')
print('',end='\n')