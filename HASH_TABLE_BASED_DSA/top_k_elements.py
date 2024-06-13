#frequency of arrays
def topKelements(numbers_array,k):
    count = {}
    result = []

    for number in numbers_array:
        count[number] = 1 + count.get(number,0)

    sorted_items = sorted(count.items(),lambda i:i[1],reverse=True)

    for number,count in range(sorted_items):
        result.append(number)
        if len(result) == k:
            return result    
        


    # count = {}
    # result = []

    # for number in numbers_array:
    #     count[number] = 1 + count.get(number,0)

    # for number, count in sorted(count.items(),key= lambda i: i[1],reverse=True):
    #     result.append(number)
    #     if len(result) == k:
    #         return result    

    
    # count = {}
    # result = []

    # for number in numbers_array:
    #     count[number] = 1 + count.get(number,0)

    # for number,count in dict(sorted(count.items(),key = lambda x :x[1],reverse=True)).items():
    #     result.append(number)
    #     if len(result) == k:
    #         return result

print(topKelements([1,1,1,2,2,3],2))
print(topKelements([1,1,1,2,2,3,4,4,4,4],3))
print(topKelements([1,1,2,2,2,2,3,3,3],2))
