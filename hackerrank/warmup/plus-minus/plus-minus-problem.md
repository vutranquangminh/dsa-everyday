
# 🧮 Plus Minus - Easy

---

## 📌 Problem Statement

**Title**: Plus Minus

**Problem Description**:  
Given an array of integers, calculate the **ratios** of its elements that are:
- positive
- negative
- zero

Print each ratio on a new line **with 6 decimal places**.

---

## 💡 Examples

### Example 1  
**Input**:
```python
arr = [-4, 3, -9, 0, 4, 1]
```

**Output**:
```
0.500000
0.333333
0.166667
```

**Explanation**:  
- 3 positive values: `3, 4, 1` → 3/6 = 0.500000  
- 2 negative values: `-4, -9` → 2/6 = 0.333333  
- 1 zero: `0` → 1/6 = 0.166667

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 ≤ n ≤ 100`  
- `-100 ≤ arr[i] ≤ 100`

---

## 💡 Hints

- Use counters for positive, negative, and zero values.
- Divide each count by the total length of the array.
- Use formatting: `print(f"{value:.6f}")` in Python.

---

## 📅 Date Done

**Date**: *02/06/2025*  
**Time Taken**: *3 minutes*

---