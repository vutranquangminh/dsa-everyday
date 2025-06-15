
# 🧮 Plus One - Easy

---

## 📌 Problem Statement

**Title**: Plus One

**Problem Description**:  
You are given a large integer represented as an array `digits`, where each `digits[i]` is the *i-th digit* of the integer.  
Digits are ordered from **most significant to least significant** (left to right).  
There are **no leading zeros** in the input array.

Increment the large integer by one and return the resulting array of digits.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
digits = [1, 2, 3]
```

**Output**:  
```python
[1, 2, 4]
```

**Explanation**:  
123 + 1 = 124

---

### Example 2  
**Input**:  
```python
digits = [4, 3, 2, 1]
```

**Output**:  
```python
[4, 3, 2, 2]
```

**Explanation**:  
4321 + 1 = 4322

---

### Example 3  
**Input**:  
```python
digits = [9]
```

**Output**:  
```python
[1, 0]
```

**Explanation**:  
9 + 1 = 10

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)` (excluding output list)

---

## 📎 Constraints

- `1 <= digits.length <= 100`  
- `0 <= digits[i] <= 9`  
- No leading zeros

---

## 💡 Hints

- Think about the **carry-over** situation, especially when the digit is `9`.
- Start **from the last digit** and move backward.
- If you encounter a `9`, set it to `0` and continue. If not, just add `1` and return early.

---

## 📅 Date Done

**Date**: *15/06/2025*  
**Time Taken**: *5 minutes*

---
