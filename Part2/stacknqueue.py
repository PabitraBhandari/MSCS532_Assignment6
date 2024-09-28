# Stack Implementation (LIFO)
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)  # Push value onto stack
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()  # Pop value from stack
    
    def is_empty(self):
        return len(self.stack) == 0  # Check if stack is empty

# Queue Implementation (FIFO)
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)  # Enqueue value to the end of the queue
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.pop(0)  # Dequeue value from the front of the queue
    
    def is_empty(self):
        return len(self.queue) == 0  # Check if queue is empty

# Example Usage:
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
print(stack.pop())  # Output: 10

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 20
