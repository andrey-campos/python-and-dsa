# use dynamic programming to return nth fib number

# this needs 2 base cases
def fib_bu(n):
    memo = {1:1, 2:1}
    if n == 0: return 0 
    for i in range(1, n+1):
        if i <= 2: 
            result = 1
        else:
            result = memo[i -1] + memo[i - 2]
        memo[i] = result
    return memo[n]


def fib_memo(n):
    memo = {1:1, 2:1}

    if n in memo:
        return memo[n]
    
    result = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = result
    return memo[n]

print(fib_bu(5))
print(fib_memo(5))