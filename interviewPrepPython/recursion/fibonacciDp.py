def fib_iter(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a+b

    return a

def fib_rec(n):
    # Base case
    if n == 0 or n ==1:
        return n
    # Recursive case
    else:
        return fib_rec(n-1) + fib_rec(n-2)
    
print(fib_rec(6))

n = 10
cache = [None]*(n+1)   
def fib_dp(n):
    # Base case
    if n == 0 or n ==1:
        return n


    # Check Cache
    if cache[n] != None:
        return cache[n]

    #Keep Setting Cache
    cache[n] = fib_dp(n-1) + fib_dp(n-2)

    return cache[n]
