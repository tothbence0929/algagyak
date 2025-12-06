#https://www.spoj.com/problems/COINS/
#Dynamic Programming
import sys
sys.setrecursionlimit(10000000)

memo = {}

def solve(n):
    if n < 12:
        return n
    if n in memo:
        return memo[n]
    memo[n] = max(n, solve(n//2) + solve(n//3) + solve(n//4))
    return memo[n]

for line in sys.stdin:
    n = int(line.strip())
    print(solve(n))
