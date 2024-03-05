"""
so I have been having a tough time understanding the tabulation implementation of the two problems mentioned in the title.
the top-down DP approach of using recursion along with memoization is a good first DP solution but it may lead to issues like stack overflow on large string / input sizes

I will just walk through the top down solution of each with the goal of understanding what each 'cache' is actually storing and then attempt to tabulate that
"""

cache = dict()

def topDownSearch(coins, target):

    if target in cache:
        return cache[target]
    
    if target == 0:
        return 0
    
    if target < 0:
        return -1
    
    mini = float('inf')
    for coin in coins:
        ans = topDownSearch(coins, target - coin)
        if ans >= 0:
            # if method returns 0, ans becomes "1" implying that there is one more way to get to the target
            # if method returns 1, ans becomes "0" implying that there is no valid way to get to the target; but this case does not trigger since we have used conditional
            mini = min(mini, ans + 1)
    
    if mini == float('inf'):
        mini = -1

    # so cache is basically holding keys of target and lowest number of coins get there, as values.
    # possible values are -1, and any positive value and never zero
    # so how about possible keys? with how target - coin is passed in to the recursion call, the keys can be [1, target] inclusive (again, not zero)

    cache[target] = mini

    return mini

coins = [5, 2, 1]
target = 11

cache = {
    1: 1
    2: 1
}

tds(11)
    mini = inf
    coin = 5
    ans = tds(6)
        mini = inf
        coin = 2 // 5(0)
        ans = tds(4)
            mini = inf
            coin = 2(1) // 5(-1)
            ans = 1
            # this was getting way too long, I gave up and decided to rewatch https://www.youtube.com/watch?v=A3FHNCAkhxE&list=PLDzeHZWIZsTomOPnCiU3J95WufjE36wsb&index=3


def bottomUpSearch(coins, target):

    # initialize a cache of [1, target] as we discussed at line 34
    # TODO answer why are we doing target + 1, instead of just target?
    cache = [0] * (target + 1)

    for target_i in range(target + 1):
        for coin in coins:
            target_reduced = target_i - coins
            if target_reduced >= 0:
                cache[target_i] = min(cache[target_i], cache[target_reduced])
    
    return cache[target + 1]