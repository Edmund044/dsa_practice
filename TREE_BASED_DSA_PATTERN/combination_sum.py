# rc bin
def combination_sum(candidates,target):    
    results = []
    def dfs(index,current_array,total):
        if total == target:
            results.append(current_array.copy())
            return
        if index >= len(candidates) or total > target:
            return
        
        current_array.append(candidates[index])
        dfs(index,current_array,total + candidates[index])
        current_array.pop()
        dfs(index + 1,current_array,total)



    dfs(0,[],0)
    return results    




    # results = []
    # def depth_first_search(index,current_array,total):
    #     if total == target:
    #         results.append(current_array.copy())
    #         return
    #     if index >= len(candidates) or total > target:
    #         return

    #     current_array.append(candidates[index])
    #     depth_first_search(index,current_array,total + candidates[index])
    #     current_array.pop()
    #     depth_first_search(index + 1,current_array,total)

    # depth_first_search(0,[],0)
    # return results    



print(combination_sum([2,4,3,6,7],7))