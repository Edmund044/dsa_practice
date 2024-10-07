class LinkedListNode():
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next


class LinkedListOperations():
    def insert_at_the_begining(self,head,value):
        new_node = LinkedListNode(value)
        current_node = new_node
        current_node.next = head
        return new_node
    
    def insert_at_the_end(self,head,value):
        new_node = LinkedListNode()
        current_node = head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        return head
    
    def insert_after_a_node(self,previous_node,value):
        new_node =LinkedListNode(value)
        new_node.next = previous_node.next
        previous_node.next = new_node
    
    def traverse_linked_list(self,head):
        current_node = head
        while current_node.next is not None:
            print(current_node.value)
            current_node = current_node.next

    def search_traverse_linked_list(self,head,value):
        current_node = head
        while current_node.next is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False         

    def delete_at_the_begining(self,head):
        current_node = head
        return head.next
    
    def delete_at_the_end(self,head):
        if head is None:
            return None
        
        if head.next is None:
            return None
        
        while head.next.next is not None:
            current_node =current_node.next

        current_node.next = None
        return head
    
    def delete_node_by_value(head, value):
        if head is None:
            return None  # List is empty
        if head.value == value:
            return head.next  # Head needs to be removed
        current = head
        while current.next is not None and current.next.value != value:
            current = current.next
        if current.next is not None:
            current.next = current.next.next
        return head




head = LinkedListNode(1)
LinkedListOperations = LinkedListOperations()
# Insert operations
head = LinkedListOperations.insert_at_the_begining(head, 0)
head = LinkedListOperations.insert_at_the_end(head, 2)
LinkedListOperations.insert_after_a_node(head.next, 1.5)  # Inserting 1.5 after 1

# Traverse the list
print("List after insertions:")
LinkedListOperations.traverse_linked_list(head)


# Delete operations
head = LinkedListOperations.delete_at_the_begining(head)
head = LinkedListOperations.delete_at_the_end(head)
head = LinkedListOperations.delete_node_by_value(head, 1.5)

# Traverse the list
print("List after deletions:")
LinkedListOperations.traverse_linked_list(head)

# Search operation
print("Searching for 1 in the list:", LinkedListOperations.search_traverse_linked_list(head, 1))
print("Searching for 3 in the list:", LinkedListOperations.search_traverse_linked_list(head, 3))