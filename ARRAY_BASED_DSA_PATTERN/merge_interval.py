#left pointer right pointer sum
#compare and do something

def merge_interval(intervals):
    intervals.sort(lambda i:i[0])
    result = [intervals[0]]
    for first_value,second_value in intervals:
        last_value = intervals[-1][1]
        if last_value < second_value:
            result = max(last_value,second_value)
        else:
            result.append([first_value,second_value])               

    # intervals.sort(key = lambda i : i[0])
    # result = [intervals[0]]
    # for first_element,second_element in intervals[1:]:
    #     if first_element <= result[-1][1]:
    #         result[-1][1] = max(result[-1][1],second_element)
    #     else:
    #         result.append([first_element,second_element])
    # return result        

            





# #sort and initiliaze goal
#     intervals.sort(key=lambda x: x[0])
#     result = [intervals[0]]
# #loop over values or indices
#     for start_value, end_value in intervals[1:]:
#         last_value = result[-1][1]
# #make a choice
#         if(start_value <= last_value):
#             result[-1][1] = max(last_value,end_value)
#         else:
#             result.append([start_value,last_value])
# #return the goal
#     return result                        
    


print(merge_interval([[1,3],[2,6],[8,10],[15,18]]))