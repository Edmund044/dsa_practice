def mininimum_number_of_coins(amount,coins):
    cache = [amount + 1] * (amount + 1)
    cache[0] = 0

    for value in range(1,amount +1 ):
        for coin in coins:
            if value - coin >= 0:
                cache[value] = min(cache[value],1 + cache[value-coin])

    return cache[amount]
                       


        
            

    # cache = [amount + 1] * (amount + 1)
    # cache[0] = 0

    # for value in range(1, amount + 1):
    #     for coin in coins:
    #         if value - coin >= 0:
    #             cache[value] = min(cache[value],1 + cache[value-coin])
    # return cache[amount]




    # dp = [amount + 1] * (amount + 1)
    # dp[0] = 0
    # for amount in range(1,amount + 1):
    #     for coin in coins:
    #         if amount - coin >=0:
    #             dp[amount] = min(dp[amount],1 + dp[amount - coin])
    # return dp[amount]                
    # dp = [amount + 1] * (amount + 1)
    # dp[0] = 0

    # for value in range(1, amount + 1):
    #     for coin in coins:
    #         if amount - coin >= 0:
    #             dp[value] = min(dp[value] , 1 + dp[value - coin])

    # return dp[amount] if dp[amount] != amount +1 else -1            



# print(mininimum_number_of_coins(11,[1,2,5]))
# print(mininimum_number_of_coins(5,[1,4,5]))
# print(mininimum_number_of_coins(87,[1,4,5,8]))

# def mininimum_number_of_coins(m,coins):
#     minimum_number_coins = 0
#     if m <=1:
#         minimum_number_coins = m

#     else:
#         for coin in range(0, m):
#             minimum_number_coins = min(minimum_number_coins,mininimum_number_of_coins(m-coin,coins))
#     return minimum_number_coins

print(mininimum_number_of_coins(11,[1,2,5]))
print(mininimum_number_of_coins(5,[1,4,5]))
print(mininimum_number_of_coins(87,[1,4,5,8]))

# print(minimum_coins(3,[1,4,5]))
# import math


# def find_min(a, b):
#     if a <= b:
#         return a
#     else:
#         return b


# def find_min_coins(c, sum):
#     # Storing total number of available coins:
#     size = len(c)

#     # Declaring a 2-D list, filled with zeroes:
#     arr = [[0] * (sum + 1) for x in range(size + 1)]

#     # Initialising first column of list with 0
#     # because a sum of 0 can be made with zero coins:
#     for i in range(size + 1):
#         arr[i][0] = 0

#     # Initialising first row of list with +ve infinity
#     # because a sum cannot be made with 0 coins:
#     for j in range(sum + 1):
#         arr[0][j] = math.inf

#     # Using recursive solution:
#     for i in range(1, size + 1):
#         for j in range(1, sum + 1):
#             if c[i - 1] > j:
#                 arr[i][j] = arr[i - 1][j]
#             else:
#                 arr[i][j] = find_min(1 + arr[i][j - c[i - 1]], arr[i - 1][j])

#     return arr[size][s]


# coins = [1,4,5]
# s = 13
# print("At least %s coins are required to make a sum of %s"
#       % (find_min_coins(coins, s), s))