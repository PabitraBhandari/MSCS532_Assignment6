## Assignment 6: Medians and Order Statistics & Elementary Data Structures
## Name: Pabitra Bhandari
## Course: Algorithms and Data Structures (MSCS-532-A01)
## Date: 09/29/2024

## Overview
This assignment is divided into two parts:
1. **Part 1: Medians and Order Statistics**
   - Implementation and analysis of algorithms for selecting the \(k^{th}\) smallest element, including a deterministic algorithm (Median of Medians) and a randomized algorithm (Quickselect).
2. **Part 2: Elementary Data Structures**
   - Implementation of basic data structures: arrays, matrices, stacks, queues, linked lists, and rooted trees.

## Repository Structure
The repository is organized into two folders:
- **Part 1**: Contains Python scripts for selection algorithms and a detailed report of the findings.
- **Part 2**: Contains Python scripts for the implementation of various data structures, along with performance analysis.

## Instructions to Run the Code
#### Running on windows 
1. Open a terminal (command prompt).
2. Navigate to the folder containing the python script using:

   ```bash
   cd path/to/your/script
   ```

3. Run the python file using:

   ```bash
   python your_script_name.py
   ```

#### Running on MacOS (Linux)
1. Open a terminal
2. Navigate to the folder containing the python script using:

   ```bash
   cd path/to/your/script
   ```

3. Run the python file using:

    ```bash
   python3 your_script_name.py
   ```
### Part 1: Medians and Order Statistics
1. Navigate to the `Part 1` folder.
2. Run the Python scripts to execute the deterministic and randomized selection algorithms.
   - `main.py`: Implements the deterministic selection algorithm (Median of Medians) and randomized Quickselect algorithm.
   - `test.py`: test both algorithm.
3. Modify the test cases in the scripts to experiment with different input sizes and distributions.

### Part 2: Elementary Data Structures
1. Navigate to the `Part 2` folder.
2. Run the Python scripts for the different data structures:
   - `arraynmatrices.py`: Implements basic array and matrix operations.
   - `stacknqueue.py`: Implements stack and queue operations using arrays and linked lists.
   - `linkedlist.py`: Implements singly linked list operations.
   - `rootedtrees.py`: Implements tree nodes.
3. Modify the test cases in the scripts to test different operations on the data structures.

## Summary of Findings

### Part 1: Medians and Order Statistics
- The **deterministic algorithm** (Median of Medians) consistently provides O(n) worst-case performance but tends to be slower than the randomized approach.
- The **randomized algorithm** (Quickselect) is faster in most cases, with an expected time complexity of O(n). It works efficiently for random inputs but has a worst-case complexity of O(n^2) in rare cases.
- Both algorithms handled edge cases such as duplicates, sorted, and reverse-sorted arrays.

### Part 2: Elementary Data Structures
- **Arrays** provide efficient O(1) access times but have slower insertion and deletion operations due to the need to shift elements.
- **Linked Lists** excel in scenarios with frequent insertions and deletions, providing O(1) for these operations, but their access times are slower O(n).
- **Stacks** and **Queues** performed efficiently for LIFO and FIFO operations, with linked list-based queues offering better performance for dequeue operations compared to array-based queues.

## References
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.

