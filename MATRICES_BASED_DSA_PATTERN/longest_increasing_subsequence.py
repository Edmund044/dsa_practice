def longest_increasing_subsequence(array_of_numbers):
    cache = [1] * len(array_of_numbers)
    for index in range(len(array_of_numbers)):
        subproblems = [cache[j] for j in range(index) if array_of_numbers[j] < array_of_numbers[index]]
        cache[index] = 1 + max(subproblems,default=0)

    return max(cache,default=0)          



# #initialize
#     cache = [1] * len(array_of_numbers) 
# #constraint and choice
#     for i in range(1, len(array_of_numbers)):
#         subproblems = [cache[j] for j in range(i) if array_of_numbers[j] < array_of_numbers[i]]
#         cache[i] = 1 + max(subproblems,default=0)

# #goal
#     return max(cache,default=0)        
             
            


    # cache =  [1] * len(array_of_numbers)

    # for value in range(1,len(array_of_numbers)):
    #     subproblems = [cache[index] for index in range(value) if array_of_numbers[index] < array_of_numbers[value]]
    #     print(subproblems)
    #     print(max(subproblems,default=0))
    #     cache[value] = 1 + max(subproblems,default=0)

    # return max(cache,default=0)    


print(longest_increasing_subsequence([10,9,2,5,3,7,101,18]))
print(longest_increasing_subsequence([0,1,0,3,2,3]))