# coding:utf-8
# def fb(n,cache=None):
#     if cache is None:
#         cache = {}
#     if n in cache:
#         return cache[n]
#     if n <= 1:
#         return 1
#     cache[n] = fb(n-1,cache) + fb(n-2,cache)
#     return cache[n]
# print(fb(20))

# def fb1(n):
#     fb = [0]*n
#     fb[0] = fb[1] = 1
#     if n >1:
#         for i in range(2,n):
#             fb[i] = fb[i-1] + fb[i-2]
#         return fb[n-1]            
# print(fb1(21))

# def fb1(n): 
#     sum =  0   
#     if n <=1:
#         return n
#     prev = cur =1
#     for i in range(2,n):
#         sum = prev + cur
#         prev = cur
#         cur = sum
#     return cur
# print(fb1(20))

# def coinChange(coins,amount):
    
#     def dp(n):
#         if n == 0:return 0
#         if n < 0:return -1
#         # res的值为正无穷
#         res = 1000000
#         for coin in coins:
#             if dp(n-coin) == -1:continue
#             res = min(res,1+dp(n-coin))
#         return res if res !=1000000 else -1
#     return dp(amount)

# def coinChange(coins,amount):
#     # 备份录
#     memo = {}
#     def dp(n):
#         if n in memo:return memo[n]
#         if n == 0:return 0
#         if n < 0:return -1
#         # res的值为正无穷
#         res = 1000000
#         for coin in coins:
#             if dp(n-coin) == -1:continue
#             res = min(res,1+dp(n-coin))
#         # 记入备忘录
#         memo[n] = res if res !=1000000 else -1
#         return memo[n]
#     return dp(amount)

def coinChange(coins,amount):
    
    dp = [float('inf')]*(amount+1)
    dp[0]=0

    for coin in coins:
        for x in range(coin,amount+1):
            dp[x] = min (dp[x],dp[x-coin]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1

coins = [1, 2, 5]
amount = 11
print(coinChange(coins,amount))