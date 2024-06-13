def LCS(s1,s2):
   cache = [[0] * len(s1)] * len(s2)

   for i in range(s1):
      for j in range(s2):
         if s1[i-1] == s2[j-1]:
            cache[i][j] = 1 + cache[i-1][j-1]
         else:
            cache[i][j] = max(cache[i-1][j],cache[i][j-1])

   return cache[i][j]               






   # dp = [[0]*len(s1)]*len(s2)
   # # dp = [[0 for j in range(len(s2)+1)] for i in range (len(s1) + 1)]
   # print(dp)

   # for i in range(len(s1)):
   #  for j in range(len(s2)):
   #      if s1[i - 1] == s2[j - 1]:
   #         dp[i][j] = dp[i - 1][j - 1] + 1
   #      else:
   #         dp[i][j] = max(dp[i - 1][j],dp[i][j -1])

   # print(len(s1),len(s2)) 
   # return dp[0][0]         
           





print(LCS([3, 5, 1, 9 ], [3, 3, 5, 3, 8 ]))