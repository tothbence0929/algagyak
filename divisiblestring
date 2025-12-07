#string adatszerkzetet
import sys

def min_deletions_to_divisible(S, T):
    if not S:
        return 0 
    n, m = len(S), len(T)
    i = 0   
    cnt = 0 
    while i < n:
        j = 0
       
        while i < n and j < m:
            if S[i] == T[j]:
                j += 1
            i += 1
        if j == m:
            cnt += 1
        else:
            break
    return n - cnt * m

def main():
    data = sys.stdin.read().splitlines()
    q = int(data[0].strip())
    out = []
    idx = 1
    for _ in range(q):
        S = data[idx].strip(); idx += 1
        T = data[idx].strip(); idx += 1
        out.append(str(min_deletions_to_divisible(S, T)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
