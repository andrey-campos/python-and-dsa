# recursively add all nonnegative integers up to n

def recursive_sum(n):
    if n == 0: return 0
    return n + recursive_sum(n-1)

print(recursive_sum(0))

# grid paths
def grid_paths(n, m):
    if n == 1 or m == 1: return 1
    else:
        return grid_paths(n-1, m ) + grid_paths(n, m-1)

print(grid_paths(2, 3))