
# Assignment 6: Medians and Order Statistics

## Part 1: Implementation and Analysis of Selection Algorithms

### Overview
This part of the assignment focuses on the implementation, analysis, and empirical testing of two selection algorithms: 
- **Deterministic Selection (Median of Medians)** with worst-case linear time complexity.
- **Randomized Selection (Quickselect)** with expected linear time complexity.

### 1. Implementation

#### Deterministic Selection (Median of Medians)
The deterministic selection algorithm works by:
1. Dividing the array into groups of 5 elements.
2. Finding the median of each group and recursively selecting the median of medians.
3. Partitioning the array around the median and selecting recursively within the appropriate partition.
   
This ensures worst-case linear time complexity, \(O(n)\), by ensuring a good pivot for partitioning.

#### Randomized Selection (Quickselect)
The randomized Quickselect algorithm works similarly to Quicksort:
1. Selects a pivot element at random.
2. Partitions the array around the pivot.
3. Recursively selects from the appropriate partition.
   
The expected time complexity is \(O(n)\), but the worst-case can degrade to \(O(n^2)\) in rare cases if poor pivots are selected repeatedly.

### 2. Performance Analysis

#### Time Complexity
- **Deterministic Algorithm (Median of Medians)**:
  - **Worst-case Time Complexity**: \(O(n)\).
  - **Space Complexity**: \(O(n)\), mainly due to recursive calls and partitioning.
  - The algorithm guarantees linear time by ensuring that at least 30% of the elements are removed from further consideration in each recursive call.

- **Randomized Algorithm (Quickselect)**:
  - **Expected Time Complexity**: \(O(n)\).
  - **Worst-case Time Complexity**: \(O(n^2)\), but this happens with very low probability.
  - **Space Complexity**: \(O(n)\), primarily due to recursive partitioning.
  - On average, the randomized approach quickly reduces the size of the problem by partitioning based on a randomly chosen pivot.

### 3. Empirical Results

The empirical results of both algorithms were measured across different input sizes (1000, 5000, and 10,000) and array distributions (random, sorted, and reverse-sorted). Below is the summarized table of results:

```
----------------------------------------------------------------------
| Input Size | Algorithm       | Distribution | Time Taken (seconds) |
----------------------------------------------------------------------
| 1000       | Deterministic   | Random       | 0.000388             |
| 1000       | Deterministic   | Sorted       | 0.000260             |
| 1000       | Deterministic   | Reversed     | 0.000269             |
| 1000       | Randomized      | Random       | 0.000164             |
| 1000       | Randomized      | Sorted       | 0.000112             |
| 1000       | Randomized      | Reversed     | 0.000120             |
----------------------------------------------------------------------
| 5000       | Deterministic   | Random       | 0.002470             |
| 5000       | Deterministic   | Sorted       | 0.001420             |
| 5000       | Deterministic   | Reversed     | 0.001271             |
| 5000       | Randomized      | Random       | 0.000689             |
| 5000       | Randomized      | Sorted       | 0.000644             |
| 5000       | Randomized      | Reversed     | 0.000646             |
----------------------------------------------------------------------
| 10000      | Deterministic   | Random       | 0.003393             |
| 10000      | Deterministic   | Sorted       | 0.002733             |
| 10000      | Deterministic   | Reversed     | 0.002548             |
| 10000      | Randomized      | Random       | 0.001040             |
| 10000      | Randomized      | Sorted       | 0.000871             |
| 10000      | Randomized      | Reversed     | 0.001012             |
----------------------------------------------------------------------
```

### Observations
- **Randomized Selection (Quickselect)** outperforms the **Deterministic Selection (Median of Medians)** in terms of execution time for all input sizes and distributions. 
- For random input, the randomized algorithm is about twice as fast as the deterministic one for larger input sizes.
- **Deterministic Selection** performs consistently across sorted and reverse-sorted arrays, as it guarantees \(O(n)\) worst-case performance.
- **Randomized Selection** shows variability, but in practice, it remains highly efficient even for sorted or reverse-sorted arrays.

### 4. Conclusion

Both the deterministic and randomized selection algorithms have their strengths:
- The **deterministic algorithm** guarantees worst-case performance but tends to be slower due to its more careful pivot selection process.
- The **randomized algorithm** is faster on average, especially for random input, but can degrade to quadratic time in rare worst-case scenarios.

In real-world applications where performance consistency is critical, the deterministic algorithm would be preferred. However, for general use, the randomized Quickselect is faster and sufficient in most cases.

### References
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
