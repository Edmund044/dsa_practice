#https://www.youtube.com/watch?v=W6aB2iM7C8g
# https://leetcode.com/problems/maximum-height-by-stacking-cuboids/description/
def maximum_stack_boxes(boxes):
    cache  = [0] * len(boxes)
    for box in boxes:
        box.sort()

    for index in range(len(boxes)):
        for j in range(index):
            if boxes[j][1] < boxes[index][1] and boxes[j][2] < boxes[index][2]:
                cache[index] = max(cache[index],cache[j] + boxes[index][2])

    return max(cache)                     



    # cache = [0] * len(boxes)
    # for box in boxes:
    #      box.sort() 
    # for index in range(len(boxes)):
    #     cache[index] = boxes[index][2]
    #     for j in range(index):
    #         if boxes[j][1] <= boxes[index][1] and boxes[j][2] <= boxes[index][2]:
    #             cache[index] = max(cache[index],cache[j] + boxes[index][2])

    # return max(cache)


            
    
    





print(maximum_stack_boxes([[50,45,20],[95,37,53],[45,23,12]]))
print(maximum_stack_boxes([[38,25,45],[76,35,3]]))
print(maximum_stack_boxes([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]))