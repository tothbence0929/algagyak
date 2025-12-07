#Removing Digits - Dynamic Programming
#https://cses.fi/problemset/task/1637/
import sys

def solve():
    
    try:
      
        n = int(sys.stdin.readline())
    except:
        return


    dp = [0] * (n + 1)
    
 
    for i in range(1, n + 1):
      
        min_steps = float('inf')
        
       
        s = str(i)
        
      
        for digit_char in s:
            digit = int(digit_char)
            
            
            if digit > 0:
               
                
                
                min_steps = min(min_steps, dp[i - digit])
        
        dp[i] = min_steps + 1
        
    print(dp[n])

if __name__ == "__main__":
    solve()
