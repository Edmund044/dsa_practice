#left pointer right pointer sum
#compare and do something {2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
#https://ashutosh-kumar.medium.com/modified-binary-search-algorithm-to-solve-tricky-problems-92399b193206

def binary_search(array,target):
    left_pointer,right_pointer = 0, len(array) -1
    array.sort()
    while left_pointer <right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2

        if target > array[mid_pointer]:
            left_pointer += 1
        elif target < array[mid_pointer]:
            right_pointer = mid_pointer
        else:
            return mid_pointer    
            
            
    

    # left_pointer,right_pointer = 0,len(array) - 1
    # while left_pointer < right_pointer:
    #     mid_pointer = (left_pointer + right_pointer) // 2
    #     if array[mid_pointer] < target:
    #         left_pointer = mid_pointer + 1
    #     elif array[mid_pointer] > target:
    #         right_pointer = mid_pointer
    #     else:
    #         return mid_pointer    
    

    # left_pointer, right_pointer = 0, len(array) - 1

    # while left_pointer < right_pointer:
    #     mid_pointer = (left_pointer + right_pointer) // 2

    #     if array[mid_pointer] == target:
    #         return mid_pointer

    #     elif array[mid_pointer] < target:
    #         left_pointer = mid_pointer + 1
    #     else:
    #         right_pointer = mid_pointer

print(binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91],23))                