#minheap append ,heapify,pop,append
import heapq
def closestKelement(points,k):
    minheap = []
    results = []
    for x,y in points:
        distance = x**2 + y**2
        minheap.append([distance,x,y])

    heapq.heapify(minheap)
    sorted_items = heapq.nsmallest(k,minheap)

    for index in range(sorted_items):
        results.append([sorted_items[index][1],sorted_items[index][2]]) 
        if len(results) == k:
            return results 


    # minheap = []
    # results = []

    # for x,y in points:
    #     distance = x**2 + y**2
    #     minheap.append([distance,x,y])

    # heapq.heapify(minheap)
    # sorted_points =heapq.nsmallest(k,minheap)

    # for index in range(len(sorted_points)):
    #     results.append([sorted_points[index][1],sorted_points[index][2]]) 
    #     if len(results) == k:
    #         return results   

  

# #initialize
#     minheap, results = [], [] 
#     for x_value, y_value in points:
#         distance = (x_value**2) + (y_value**2)
#         minheap.append([distance,x_value,y_value])    

# #append
        
# #heapify
#     heapq.heapify(minheap)
#     print(minheap)
# #nsmallest
#     for index in range(len(heapq.nsmallest(k,minheap))):
#         results.append([minheap[index][1],minheap[index][2]])
#         if len(results) == k:
#             return results
         
#loop by index
#return when depth is reached
                   


    #heappify
    #loop over top elements
    # return results
    # min_heap, results = [], []
    # for value_x,value_y in points:
    #     distance = (value_x**2) + (value_y**2)
    #     min_heap.append([distance,value_x,value_y])

    # heapq.heapify(min_heap)
    # for index in range(len(heapq.nsmallest(k,min_heap))):
    #     results.append([min_heap[index][1],min_heap[index][2]])
    #     if len(results) == k:
    #         return results

    # min_heap, res = [],[]

    # for x,y in points:
    #     distance = (x**2) + (y**2)
    #     min_heap.append([distance,x,y])
    # heapq.heapify(min_heap)
    # list_ = heapq.nsmallest(k, min_heap)
    # for index in range(len(list_)):
    #     res.append([min_heap[index][1],min_heap[index][2]])
    #     if len(res) == k:
    #         return res


        # res.append(min_heap[index][1][2])
        # if len(res) == k:
        #     return res
    # return [result[0][1],result[0][2]]

print("qwe",closestKelement([[1,3],[-2,2]],2))
print("qwe",closestKelement([[3,3],[5,-1],[-2,4]],2))