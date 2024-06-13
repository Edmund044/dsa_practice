def fibonacci(n,cache):
    if n in cache:
        return cache[n]
    
    if n <= 1:
        return n
    else:
        cache[n] = fibonacci(n-1,cache) + fibonacci(n-2,cache)
    return cache[n]    

    # if n in cache:
    #     return cache[n]
    # if n <= 1:
    #     return n
    # else:
    #     cache[n] = fibonacci(n-1,cache) + fibonacci(n-2,cache)
    # return cache[n]       
    

    # if n <= 1:
    #    return n

    # else:
    #     if n in cache:
    #         return cache[n]
        
    #     cache[n] = fibonacci(n-1,cache) + fibonacci(n-2,cache) 
   
    # return cache[n]

print(fibonacci(9,cache={}))    