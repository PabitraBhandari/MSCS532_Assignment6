# Node for the linked list
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# Singly Linked List Implementation
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self.head
        self.head = new_node  # Insert at the beginning
    
    def delete(self, value):
        if self.head is None:
            raise ValueError("List is empty")
        
        if self.head.value == value:
            self.head = self.head.next  # Delete head node
            return
        
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next  # Delete the node
                return
            current = current.next
        
        raise ValueError(f"Value {value} not found in the list")
    
    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")  # End of list

# Example Usage:
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.traverse()  # Output: 20 -> 10 -> None
linked_list.delete(10)
linked_list.traverse()  # Output: 20 -> None
