# Array Implementation
class Array:
    def __init__(self):
        self.array = []
    
    def insert(self, index, value):
        self.array.insert(index, value)  # Inserting value at index
    
    def delete(self, index):
        if index < len(self.array):
            self.array.pop(index)  # Deleting value at index
        else:
            raise IndexError("Index out of bounds")
    
    def access(self, index):
        if index < len(self.array):
            return self.array[index]  # Accessing value at index
        else:
            raise IndexError("Index out of bounds")

# Matrix Implementation
class Matrix:
    def __init__(self, rows, cols):
        self.matrix = [[0] * cols for _ in range(rows)]  # Initializing a matrix with zeroes
    
    def access(self, row, col):
        return self.matrix[row][col]  # Accessing value at (row, col)
    
    def update(self, row, col, value):
        self.matrix[row][col] = value  # Updating value at (row, col)

# Example Usage:
array = Array()
array.insert(0, 10)
array.insert(1, 20)
array.delete(0)
print(array.access(0))  # Output: 20

matrix = Matrix(3, 3)
matrix.update(1, 1, 5)
print(matrix.access(1, 1))  # Output: 5
