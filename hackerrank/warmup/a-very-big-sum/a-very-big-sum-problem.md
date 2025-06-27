
# 🧮 A Very Big Sum - Easy

---

## 📌 Problem Statement

**Title**: A Very Big Sum

**Problem Description**:  
You are given an array of integers. Some of these integers may be **very large**, exceeding the range of a standard 32-bit integer.  
Your task is to **calculate and return the sum** of the elements in the array.

---

## 💡 Examples

### Example 1  
**Input**:
```python
n = 5  
arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
```

**Output**:
```python
5000000015
```

**Explanation**:  
The sum is:  
`1000000001 + 1000000002 + 1000000003 + 1000000004 + 1000000005 = 5000000015`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 ≤ n ≤ 10`  
- `0 ≤ arr[i] ≤ 10^10`  

---

## 💡 Hints

- Use a data type capable of holding large integers (e.g., `long` in Java, default `int` in Python).
- Iterate through the array and add each element to a running total.

---

## 📅 Date Done

**Date**: *31/05/2025*  
**Time Taken**: *1 minute*

---