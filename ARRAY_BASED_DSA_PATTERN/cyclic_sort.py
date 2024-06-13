# https://blog.stackademic.com/coding-pattern-cyclic-sort-96511b0f60ac
def cyclic_sort(numbers):
    for index in range(len(numbers)):
        position = numbers[index] - 1
        if index != position:
            numbers[index], numbers[position] = numbers[position], numbers[index]
        else:
            index +=1
    return numbers            
                 


    # for index in range(len(numbers)):
    #     position = numbers[index] - 1
    #     if numbers[index] != numbers[position]:
    #         numbers[index], numbers[position] = numbers[position], numbers[index]
    #     else:
    #         index+=1
    # return numbers
    # for index in range(len(numbers)):
    #     position = numbers[index] - 1
    #     if (numbers[index] != numbers[position]):
    #         numbers[index], numbers[position] = numbers[position], numbers[index]

    #     else:
    #         index += 1
    # return numbers            



print(cyclic_sort([2, 6,7, 4, 3, 1, 5]))