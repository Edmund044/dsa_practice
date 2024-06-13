# https://youtu.be/_CkYbxKzkF8?si=xZxoyt6pRl4HvthQ
class ListNode:
    def __init__(self,data,next):
        self.data = data
        self.next = next

def reverseLinkedList(head: ListNode):
    previous_node,current_node = None,head

    while current_node.next:
        temporary_next = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = temporary_next

    return previous_node    
        
    

       

    # previous_node, current_node = None, head

    # while current_node:
    #     temporary_next = current_node.next
    #     current_node.next = previous_node
    #     previous_node = current_node
    #     current_node = temporary_next
    # return previous_node    


    

       

            



# class ListNode:
#     def __init__(self,data,nxt) -> None:
#         self.data = data
#         self.nxt = nxt

# def reverseLinkedList(head: ListNode):
#     previous,current = None,head

#     while current:
#         nxt = current.next
#         current.next = previous
#         previous = current
#         current = nxt
#     return previous
            