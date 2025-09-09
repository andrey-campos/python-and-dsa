# Solving minimum coin problems
from collections import defaultdict
# possible coin options
coins = [1, 2, 5, 10, 20, 50, 100, 200]

def min_ignore_none(a, b):
    if a is None:
        return b 
    if b is None:
        return a
    
    # return minimum of either a or b otherwise
    return min(a, b)

# solving using naive recursive approach
def naive_min_coins(m, coins):
    if m == 0:
        answer = 0
    else:
        # no solution state
        answer = None 

        for coin in coins:
            # subtracting the coin 
            subproblem = m - coin
            if subproblem < 0:
                # skip solutions where we try to reach [m]
                # from a negative subproblem
                continue
            
            # for a valid sub problem we recursively solve subproblem
            answer = min_ignore_none(
                answer,
                # add 1 can we are using the current coin 
                naive_min_coins(subproblem, coins) + 1
            )
    return answer
                
# init memo dict to solve
memo = {}
def dp_min_coins(m, coins):
    if m in memo:
        return memo[m]
    
    # base case 
    if m == 0:
        answer = 0
    else:
        # no solution state
        answer = None 

        for coin in coins:
            # subtracting the coin 
            subproblem = m - coin
            if subproblem < 0:
                # skip solutions where we try to reach [m]
                # from a negative subproblem
                continue
            
            # for a valid sub problem we recursively solve subproblem
            answer = min_ignore_none(
                answer,
                # add 1 can we are using the current coin 
                naive_min_coins(subproblem, coins) + 1
            )

    memo[m] = answer
    return answer
                
# bottom up solution for minimum coins
def bu_min_coins(m, coins):
    memo = {0:0}
    
    for i in range(1, m+1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0: 
                continue
            memo[i] = min_ignore_none(memo.get(i), memo.get(subproblem) + 1)
        
    return memo[m]

print(bu_min_coins(4, coins))

# dif ways to form the sum m w/ given coins:
def how_many_ways(m, coins):
    memo = defaultdict(lambda: 0)

    # base case "1 way to construct sum of 0"
    memo[0] = 1
    for i in range(1, m+1):

        memo[i] = 0 # init count for this sum as 0 
        for coin in coins:
            subproblem = i - coin 
            if subproblem < 0:
                continue
            
            # add different ways from the subproblem
            memo[i] = memo[i] + memo[subproblem]

    return memo[m]

# example set coins = {1, 2, 5}
def optimal_how_many_ways(m, coins):
    # memo array with filled w/0s and length of m+1 
    memo = [0] * (m+1)
    memo[0] = 1

    for coin in coins:
        # for each coin update all possible sums from coin value to m (sum)
        for i in range(coin, m+1):
            memo[i] += memo[i - coin]
    
    return memo[m]

def LIC(t1, t2):
    # top down DP
    # time O(m*n)
    memo = {}
    m, n = len(t1), len(t2)

    def longest(i, j):
        # base case (if one of the two strings are empty)
        if i == m or j == n:
            return 0 
        
        # pointing to equal chars?
        elif t1[i] == t2[j]:
            # getting 1 char from this so add 
            return 1 + longest(i+1, j+1) # remainder of both the strings
        
        else:
            return max(longest(i, j+1), longest(i+1, j))

    return longest(0, 0 )

def bu_lic(t1, t2):
    # bottom up 
    # time O(n)
    pass