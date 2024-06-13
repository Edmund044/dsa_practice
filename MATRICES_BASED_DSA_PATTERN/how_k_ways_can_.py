def how_many_ways(amount, coins):
   cache = [amount + 1] * (amount + 1)
   cache[0] = 0
   for value in range(1,amount+1):
      for coin in coins:
         if value - coin >= 0:
            cache[value] = cache[value] + cache[value-coin]

   return cache[amount]             




    # dp = [amount + 1 ] * (amount + 1)
    # dp[0] = 0

    # for value in range(1,amount + 1):
    #     for coin in coins:
    #         if value - coin >= 0:
    #             dp[value] = dp[value] + dp[value - coin]

    # return dp[amount]


print(how_many_ways(5,[5]))
print(how_many_ways(11,[1]))