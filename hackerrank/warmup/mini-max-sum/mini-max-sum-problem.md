# 🧮 Mini-Max Sum - Easy

---

## 📌 Problem Statement

**Title**: Mini-Max Sum

**Problem Description**:  
Given **five positive integers**, find the **minimum and maximum values** that can be calculated by **summing exactly four** of the five integers.  
Print these two values as **space-separated integers** on one line.

---

## 💡 Examples

### Example 1  
**Input**:
```python
arr = [1, 2, 3, 4, 5]
```

**Output**:
```text
10 14
```

**Explanation**:  
The sums of all combinations of 4 out of 5 elements are:
- 2 + 3 + 4 + 5 = 14  
- 1 + 3 + 4 + 5 = 13  
- 1 + 2 + 4 + 5 = 12  
- 1 + 2 + 3 + 5 = 11  
- 1 + 2 + 3 + 4 = 10  

So the **minimum** is `10`, and the **maximum** is `14`.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- Exactly `5` integers in the array  
- Each integer is in the range: `1 ≤ arr[i] ≤ 10^9`

---

## 💡 Hints

- The total sum of the array is constant.
- The **minimum sum** is the total sum minus the **maximum number**.
- The **maximum sum** is the total sum minus the **minimum number**.
- Use 64-bit integers (`long` or `int` in Python) to prevent overflow.

---

## ✅ Python Implementation

```python
def miniMaxSum(arr):
    total = sum(arr)
    min_val = min(arr)
    max_val = max(arr)
    print(f"{total - max_val} {total - min_val}")
```

---

## 📅 Date Done

**Date**: *04/06/2025*  
**Time Taken**: *3 minutes*

---
