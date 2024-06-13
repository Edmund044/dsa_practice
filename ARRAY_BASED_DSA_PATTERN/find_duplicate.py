#double loop
def findDuplicateNumbers(numbers_array):
    slow_pointer,slow_pointer_2,fast_pointer = 0,0,0

    while True:
        slow_pointer = numbers_array[slow_pointer]
        fast_pointer = numbers_array[numbers_array[fast_pointer]]
        if slow_pointer == fast_pointer:
            break

    while True:
        slow_pointer = numbers_array[slow_pointer]
        slow_pointer_2 = numbers_array[slow_pointer_2]
        if slow_pointer == slow_pointer_2:
            return slow_pointer
                   
            
    # slow_pointer_1,slow_pointer_2,fast_pointer = 0,0,0
    # while True:
    #     slow_pointer_1 = numbers_array[slow_pointer_1]
    #     fast_pointer = numbers_array[numbers_array[fast_pointer]]
    #     if slow_pointer_1 == fast_pointer:
    #         break

    # while True:
    #     slow_pointer_1 = numbers_array[slow_pointer_1]
    #     slow_pointer_2 = numbers_array[slow_pointer_2]
    #     if slow_pointer_1 == slow_pointer_2:
    #         return slow_pointer_1
            
    # slow_pointer_1,slow_pointer_2,fast_pointer = 0,0,0

    # while True:
    #     slow_pointer_1 = numbers_array[slow_pointer_1]
    #     fast_pointer = numbers_array[numbers_array[fast_pointer]]
    #     if slow_pointer_1 == fast_pointer:
    #         break

    # while True:
    #     slow_pointer_1 = numbers_array[slow_pointer_1]
    #     slow_pointer_2 = numbers_array[slow_pointer_2]

    #     if slow_pointer_1 == slow_pointer_2:
    #         return slow_pointer_1
        

print(findDuplicateNumbers([1,3,4,2,2]))
print(findDuplicateNumbers([3,1,3,4,2]))
print(findDuplicateNumbers([3,3,3,3,3]))
print(findDuplicateNumbers([1,2,3,3,4,5]))