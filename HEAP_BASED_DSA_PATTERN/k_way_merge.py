#https://www.youtube.com/watch?v=cUiUCR-XTO0
#double loop
from heapq import heappush,heappop

class ListNode:
    def __int__(self,data):
        self.data = data
        self.next = None

def mergeList(lists):
    minheap = []
    dummy_node = ListNode(0)
    current_node = dummy_node

    for list in lists:
        heappush(list,minheap)


    while current_node.next:
        popped_node = heappop(minheap)
        current_node.next = popped_node
        current_node = current_node.next

        if popped_node.next:
            heappush(popped_node.next,minheap)

    return dummy_node.next



    # min_heap = []
    # dummy_node = ListNode(0)
    # current_node = dummy_node

    # for node in lists:
    #     heappush(min_heap,node)

    # while len(min_heap) > 0:
    #     popped_node = heappop(min_heap)
    #     current_node.next = popped_node
    #     current_node = current_node.next

    #     if popped_node.next:
    #         heappush(min_heap,popped_node.next)

    # return dummy_node.next            
            
        

    # min_heap = []
    # dummy_node = ListNode(0)
    # current_node = dummy_node

    # for node in lists:
    #     heappush(min_heap,node)

    # while len(min_heap) > 0:
    #     popped_node = heappop(min_heap)
    #     current_node.next = popped_node
    #     current_node = current_node.next

    #     if node.next:
    #         heappush(min_heap,node.next)

    # return dummy_node.next                       


list1  = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


list3 = ListNode(2)
list3.next = ListNode(6)

print(list1)
print(list2)
print(list3)
input = [list1,list2,list3]
print(input)
print(merge_list(input))

    # min_heap = []
    # dummy_node = ListNode(0)
    # current_node = dummy_node

    # for value in lists:
    #     heappush(min_heap,value)

    # while len(min_heap) > 0:
    #     node = heappop(min_heap)
    #     current_node.next = node
    #     current_node = current_node.next
    #     if node.next:
    #         heappush(min_heap,node.next)

    # return dummy_node.next        
