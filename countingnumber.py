#Dynamic Programming
#https://cses.fi/problemset/task/2220/
import sys

CACHE = {}
S = "" 
N = 0  

def get_digits_sum_count(index, prev_digit, is_tight, is_leading_zero):
    global S, N, CACHE

    if index == N:
        return 1

    cache_key_pd = 10 if is_leading_zero else prev_digit 
    
    if not is_tight and (index, cache_key_pd) in CACHE:
        return CACHE[(index, cache_key_pd)]

    limit = int(S[index]) if is_tight else 9
    
    result = 0
    
    for d in range(limit + 1):
        
        is_invalid_adjacent = False
        if not is_leading_zero:
            if d == prev_digit:
                is_invalid_adjacent = True
        
        if is_invalid_adjacent:
            continue
            
        new_is_tight = is_tight and (d == limit)
        new_is_leading_zero = is_leading_zero and (d == 0)
        new_prev_digit = d if not new_is_leading_zero else -1
        
        result += get_digits_sum_count(index + 1, new_prev_digit, new_is_tight, new_is_leading_zero)

    if not is_tight:
        CACHE[(index, cache_key_pd)] = result

    return result

def count_up_to(x):
    global S, N, CACHE
    if x < 0:
        return 0
    
    S = str(x)
    N = len(S)
    CACHE = {}
    
    return get_digits_sum_count(0, -1, True, True)

def solve():
    try:
        data = sys.stdin.readline().split()
        if not data:
            return
        a = int(data[0])
        b = int(data[1])
    except:
        return

    result = count_up_to(b) - count_up_to(a - 1)
    
    print(result)

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    solve()
