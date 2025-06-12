
# 🧮 Two Integer Sum II - Medium

---

## 📌 Problem Statement

**Title**: Two Integer Sum II

**Problem Description**:  
You are given an array of integers `numbers` sorted in **non-decreasing order**.  
Find **two distinct indices** `index1` and `index2` (1-indexed) such that:

- `numbers[index1 - 1] + numbers[index2 - 1] == target`
- `index1 < index2`

You **must not** use the same element twice.  
Return the pair `[index1, index2]`.  
It is **guaranteed** that exactly one valid solution exists.  
You must solve it using **`O(1)` additional space**.

---

## 💡 Example

### Example 1  
**Input**:  
```python
numbers = [1, 2, 3, 4]
target = 3
```

**Output**:  
```python
[1, 2]
```

**Explanation**:  
The sum of `1` (index 1) and `2` (index 2) is `3`.

---

## 📎 Constraints

- `2 <= numbers.length <= 1000`  
- `-1000 <= numbers[i] <= 1000`  
- `-1000 <= target <= 1000`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`

---

## 💡 Hints

- **Hint 1**:  
  Brute-force tries all pairs → `O(n^2)` — not efficient.

- **Hint 2**:  
  Use the fact that the array is **sorted**.

- **Hint 3**:  
  Apply the **two-pointer technique**:  
  - If `left + right > target` → move `right` left  
  - If `left + right < target` → move `left` right  
  - Else → return their indices

- **Hint 4**:  
  This works because the array is sorted. You always move toward a more optimal sum.

---

## 📅 Date Done

**Date**: *06/06/2025*  
**Time Taken**: *30 minutes*

---