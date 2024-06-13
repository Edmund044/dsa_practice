class ListNode:
    def __int__(self,data,next):
        self.data = data
        self.next = next

def has_cycle(head: ListNode):
    slow_pointer,fast_pointer = head,head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True

    return False    

    # #initialize
    # slow_pointer, fast_pointer = head,head
    # #contraint and choice
    # while fast_pointer and fast_pointer.next:
    #     slow_pointer = slow_pointer.next
    #     fast_pointer = fast_pointer.next.next
    #     if slow_pointer == fast_pointer:
    #         return True
    # #goal
    # return False        








# class ListNode:
#     def __init__(self,data,next):
#         self.data = data
#         self.next = next

# def reverseLinkedlist(head: ListNode):
#     slow, fast = head, head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             return True

#     return False    

