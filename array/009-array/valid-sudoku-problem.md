# 🧮 Valid Sudoku - Medium

This is the description of the **"Valid Sudoku"** problem, which checks if a given 9x9 Sudoku board follows the standard rules of validity.

---

## 📌 Problem Statement

**Title**: Valid Sudoku

**Problem Description**:  
You are given a 9 x 9 Sudoku board `board`. A Sudoku board is valid if the following rules are followed:

- Each **row** must contain the digits `1-9` without duplicates.  
- Each **column** must contain the digits `1-9` without duplicates.  
- Each of the nine **3 x 3 sub-boxes** of the grid must contain the digits `1-9` without duplicates.  

Return `true` if the Sudoku board is valid, otherwise return `false`.

> **Note**: A board does not need to be full or be solvable to be valid.

### Example 1:
**Input**:  
```python
board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
]
```

**Output**:  
`true`

---

### Example 2:
**Input**:  
```python
board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
]
```

**Output**:  
`false`  
**Explanation**:  
There are two `1`s in the top-left 3x3 sub-box.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n^2)`  
- **Space Complexity**: `O(n^2)`

---

## 📅 Date Done

**Date**: *04/06/2025*
**Time Taken**: *180 minutes*

---