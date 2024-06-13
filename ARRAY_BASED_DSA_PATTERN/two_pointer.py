#left pointer right pointer sum
#compare and do something

def two_sum(nums, target):
    left_pointer,right_pointer = 0,len(nums)-1
    nums.sort()
    while left_pointer < right_pointer:
        current_sum  = nums[left_pointer] + nums[right_pointer]
        if current_sum > target:
            right_pointer -= 1
        elif current_sum < target:
            left_pointer += 1
        else:
            return [left_pointer,right_pointer]
            


        

    # nums.sort()
    # left_pointer, right_pointer = 0, len(nums) - 1
    # while left_pointer < right_pointer:
    #     if nums[left_pointer] + nums[right_pointer] == target:
    #         return [left_pointer,right_pointer]
    #     elif nums[left_pointer] + nums[right_pointer] > target:
    #         right_pointer -= 1
    #     else: 
    #         left_pointer += 1             

    # nums.sort()
    # left_pointer, right_pointer = 0, len(nums) -1
    # while left_pointer < right_pointer:
    #  current_sum = nums[left_pointer] + nums[right_pointer]
    #  if current_sum == target:
    #     return [left_pointer,right_pointer]
    #  elif current_sum < target:
    #     left_pointer += 1
    #  else:
    #     right_pointer -= 1       
       
    # nums.sort()
    # left_pointer = 0
    # right_pointer = len(nums) -1

    # while left_pointer < right_pointer:
    #     current_sum = nums[left_pointer] + nums[right_pointer]
    #     if(current_sum == target):
    #         return [left_pointer, right_pointer]

    #     elif(current_sum>target):
    #         right_pointer -=1

    #     else:
    #         left_pointer +=1

print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))
print(two_sum([3,3],6)) 

       
                