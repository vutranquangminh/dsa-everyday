
# 🧮 Diagonal Difference - Easy

---

## 📌 Problem Statement

**Title**: Diagonal Difference

**Problem Description**:  
Given a square matrix, calculate the **absolute difference** between the sums of its two diagonals:

- **Primary diagonal**: Top-left to bottom-right  
- **Secondary diagonal**: Top-right to bottom-left  

Return the absolute value of the difference between the two sums.

---

## 💡 Examples

### Example 1  
**Input**:
```python
arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]
```

**Output**:
```python
15
```

**Explanation**:  
Primary diagonal: `11 + 5 + (-12) = 4`  
Secondary diagonal: `4 + 5 + 10 = 19`  
Absolute difference: `|4 - 19| = 15`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 ≤ n ≤ 10`  
- `-100 ≤ arr[i][j] ≤ 100`

---

## 💡 Hints

- Loop once from 0 to n-1.
- Use `arr[i][i]` for the primary diagonal.
- Use `arr[i][n - 1 - i]` for the secondary diagonal.
- Compute `abs(primary - secondary)`.

---

## 📅 Date Done

**Date**: *27/06/2025*  
**Time Taken**: *3 minutes*
