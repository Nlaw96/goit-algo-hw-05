def  caching_fibonachi():
    cache = dict()
    def fibonachi(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]


        cache[n] = fibonachi(n-1) + fibonachi(n -2)
        return cache[n]
    
    return fibonachi

fib = caching_fibonachi()

print(fib(15))