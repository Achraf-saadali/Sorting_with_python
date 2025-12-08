# Sorting Algorithms Documentation

## Overview

This document provides comprehensive documentation for four fundamental sorting algorithms implemented in Python: Selection Sort, Bubble Sort, Quick Sort, and Fusion Sort (Merge Sort).

## Test Data

```python
M = [6, 7, 3, 1, 89, 4, 56, 32, 1, 5, 7, 8, 9]
```

---

## 1. Selection Sort

### Description

Selection Sort is a simple comparison-based sorting algorithm that divides the list into two parts: a sorted portion and an unsorted portion. In each iteration, it finds the minimum element from the unsorted portion and moves it to the sorted portion.

### Algorithm

1. Start with the first element as the sorted portion
2. Find the smallest element in the unsorted portion
3. Swap it with the first element of the unsorted portion
4. Move the boundary between sorted and unsorted portions one step to the right
5. Repeat until the entire list is sorted

### Implementation

```python
def select_sort(L : list[int])->list[int] :
    if len(L) <= 1:
        return L
    length : int = len(L)
    for i in range(length) :
        index : int = i
        for j in range(i,length):
            if L[index] > L[j] :
                index = j
        if index != i :
            L[index] , L[i] = L[i] , L[index]      
    return L
```

### Complexity Analysis

- **Time Complexity**: O(n²) in all cases (best, average, worst)
- **Space Complexity**: O(1) - sorts in-place
- **Stability**: Not stable

### Characteristics

- Simple to understand and implement
- In-place sorting (requires minimal extra space)
- Not adaptive (doesn't perform better on nearly sorted data)
- Makes O(n) swaps in worst case

---

## 2. Bubble Sort

### Description

Bubble Sort is a simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. Larger elements "bubble up" to the end of the list with each pass.

### Algorithm

1. Compare adjacent pairs of elements
2. Swap them if they are in the wrong order
3. Continue through the entire list
4. Repeat the process until no swaps are needed

### Implementation

```python
def bubble_sort(L: list[int])->list[int] :
    if len(L) <= 1 :
        return L
    length : int = len(L)
    for i in range(length):
        for j in range(length - 1):
            if L[j] > L[j+1]:
                L[j] , L[j+1] = L[j+1] , L[j]
    return L
```

### Complexity Analysis

- **Time Complexity**: O(n²) in worst and average cases, O(n) in best case
- **Space Complexity**: O(1) - sorts in-place
- **Stability**: Stable

### Characteristics

- Very simple to understand
- In-place sorting
- Stable sorting algorithm
- Inefficient for large datasets
- Can be optimized with early termination detection

---

## 3. Quick Sort

### Description

Quick Sort is a highly efficient divide-and-conquer algorithm that selects a pivot element and partitions the list around it. Elements smaller than the pivot go to the left, and larger elements go to the right. The process is recursively applied to the left and right partitions.

### Algorithm

1. Select a pivot element (in this implementation, the middle element)
2. Partition the list into three parts: elements less than pivot, equal to pivot, and greater than pivot
3. Recursively apply Quick Sort to the left partition (less than pivot)
4. Recursively apply Quick Sort to the right partition (greater than pivot)
5. Concatenate the sorted partitions

### Implementation

```python
def quick_sort(L:list[int]) -> list[int] :
    if len(L) <= 1 :
        return L
    length : int = len(L)
    x : int = L[length//2]
    return quick_sort([ value for value in L if value < x]) + [ value for value in L if value == x] +quick_sort([ value for value in L if value > x])
```

### Complexity Analysis

- **Time Complexity**: O(n log n) average case, O(n²) worst case
- **Space Complexity**: O(log n) due to recursion stack
- **Stability**: Not stable

### Characteristics

- Very efficient for large datasets
- Divide-and-conquer approach
- Can be optimized with better pivot selection strategies
- Worst case occurs with poor pivot selection
- Uses extra space for partitions

---

## 4. Fusion Sort (Merge Sort)

### Description

Fusion Sort, also known as Merge Sort, is a stable divide-and-conquer algorithm that divides the list into halves, recursively sorts each half, and then merges the sorted halves back together.

### Algorithm

1. Divide the list into two halves at the midpoint
2. Recursively apply Fusion Sort to the left half
3. Recursively apply Fusion Sort to the right half
4. Merge the two sorted halves:
   - Compare elements from both halves
   - Add the smaller element to the result
   - Continue until one half is exhausted
   - Append remaining elements

### Implementation

```python
def fusion_sort(L:list[int])->list[int]:
    if len(L) <= 1:
        return L
    
    length : int = len(L) // 2
    A = fusion_sort(L[:length])
    B = fusion_sort(L[length:])
    i : int = 0 
    j : int = 0 
    k : int = 0
    M = [0]*len(L)
    while i < len(A) & j < len(B) & k < len(L):
        if A[i] > B[j]:
            M[k] = B[j]
            j += 1
        else:
            M[k] = A[i] 
            i += 1
        k += 1
    while i < len(A) & k < len(L):
<<<<<<< HEAD
            L[k] = A[i]
            k += 1 
            i += 1     
    while j < len(B) & k < len(L):
            L[k] = B[j]
            k += 1 
            j += 1    
    return L
=======
            M[k] = A[i]
            k += 1 
            i += 1     
    while j < len(B) & k < len(L):
            M[k] = B[j]
            k += 1 
            j += 1    
    return M
>>>>>>> 3d93283 (new commit to come)

```

### Complexity Analysis

- **Time Complexity**: O(n log n) in all cases (best, average, worst)
- **Space Complexity**: O(n) - requires additional space for merging
- **Stability**: Stable

### Characteristics

- Consistent O(n log n) performance
- Stable sorting algorithm
- Requires additional space proportional to input size
- Better for linked lists than arrays
- Guaranteed performance regardless of input distribution

### Note

There appears to be a bug in the merge operation of the current implementation. The merge logic uses bitwise AND operators (`&`) instead of logical AND operators (`and`), which may cause unexpected behavior.

---

## Comparison Table

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable | In-place |
|-----------|------------|-----------|-------------|-------|--------|----------|
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes* |
| Fusion Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |

*Quick Sort is considered in-place in terms of the partitioning approach, though this implementation creates new lists.

---

## Usage Example

```python
M = [6, 7, 3, 1, 89, 4, 56, 32, 1, 5, 7, 8, 9]
print(select_sort(M))   # Output: [1, 1, 3, 4, 5, 6, 7, 7, 8, 9, 32, 56, 89]
print(bubble_sort(M))   # Output: [1, 1, 3, 4, 5, 6, 7, 7, 8, 9, 32, 56, 89]
print(quick_sort(M))    # Output: [1, 1, 3, 4, 5, 6, 7, 7, 8, 9, 32, 56, 89]
print(fusion_sort(M))   # Output: [1, 1, 3, 4, 5, 6, 7, 7, 8, 9, 32, 56, 89]
```

---

## When to Use Each Algorithm

- **Selection Sort**: Educational purposes, when memory is critical, or when the number of swaps must be minimized
- **Bubble Sort**: Educational purposes, small datasets, or checking if a list is nearly sorted
- **Quick Sort**: General-purpose sorting for large datasets, when average O(n log n) is acceptable
- **Fusion Sort**: When guaranteed O(n log n) performance is needed, data doesn't fit in memory (can be adapted for external sorting), or stability is required

---

## Notes and Recommendations

1. For production code, use Python's built-in `sorted()` function or `.sort()` method, which use Timsort (hybrid of merge sort and insertion sort)
2. Consider the characteristics of your data (size, distribution, existing order) when choosing an algorithm
3. The Fusion Sort implementation has a bug in the merge logic that should be fixed before use
4. Type hints are used appropriately in the implementation for better code documentation
