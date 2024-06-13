#results current
#base
#append_recursively pop recursilvely
def subsets(numbers_array):
    results = []

    def dfs(index,current_array):
        if index >= len(numbers_array):
            return
        
        current_array.append(numbers_array[index])
        dfs(index+1,current_array)
        current_array.pop()
        dfs(index+1,current_array)



    dfs(0,[])
    return results

    # #initialize
    # results = []
    # #contraints
    # def dfs(index,subsets):
    # #choice
    #     if index >= len(numbers_array):
    #         results.append(subsets.copy())
    #         return 
        
    #     subsets.append(numbers_array[index])
    #     dfs(index+1,subsets)
    #     subsets.pop()
    #     dfs(index+1,subsets)
    # #goal
    # dfs(0,[])
    # return results







    # results = []
    # def dfs(index,subsets):
    #     if index >= len(numbers_array):
    #         results.append(subsets.copy())
    #         return 

    #     subsets.append(numbers_array[index])
    #     dfs(index + 1,subsets)
    #     subsets.pop()
    #     dfs(index + 1,subsets)

    # dfs(0,[])
    # return results







    # results = []
    # subsets = []
    # def depth_first_search(index):
    #     if(index>=len(numbers_array)):
    #         results.append(subsets.copy())
    #         return 
        
    #     subsets.append(numbers_array[index])
    #     depth_first_search(index + 1)
    #     subsets.pop()
    #     depth_first_search(index + 1)
    # depth_first_search(0)
    # return results    



print(subsets([1,2,4,3,5]))
print(len(subsets([1,2,4,3,5])))