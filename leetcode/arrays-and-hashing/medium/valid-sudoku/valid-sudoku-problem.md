
# 🧮 Valid Sudoku - Medium

---

## 📌 Problem Statement

**Title**: Valid Sudoku

**Problem Description**:  
You are given a 9 × 9 `board` representing a partially filled Sudoku grid.  
A **valid** Sudoku board must satisfy the following rules:

- Each row contains the digits `1-9` without **duplicates**  
- Each column contains the digits `1-9` without **duplicates**  
- Each of the **nine 3×3 sub-boxes** must contain the digits `1-9` without **duplicates**

Return `True` if the board is **valid**, otherwise return `False`.

> ⚠️ The board **does not need to be solvable or complete** to be considered valid.

---

## 💡 Examples

### Example 1  
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
```python
True
```

---

### Example 2  
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
```python
False
```

**Explanation**:  
Duplicate `1` appears in the top-left 3×3 sub-box.

---

## 📎 Constraints

- `board.length == 9`  
- `board[i].length == 9`  
- `board[i][j]` is a digit `'1'`–`'9'` or `'.'`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n²)`  
- **Space Complexity**: `O(n²)`  
  Where `n = 9` (grid size)

---

## 💡 Hints

- **Hint 1**:  
  Use a **hash set** to detect duplicates efficiently.

- **Hint 2**:  
  Create sets for:
  - Rows  
  - Columns  
  - 3×3 Boxes

- **Hint 3**:  
  To index a sub-box, use:  
  ```python
  box_index = (row // 3) * 3 + (col // 3)
  ```

---

## 📅 Date Done

**Date**: *04/06/2025*
**Time Taken**: *180 minutes*

---
