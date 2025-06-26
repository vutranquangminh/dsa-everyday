
# 🧮 Product of Array Except Self - Medium

---

## 📌 Problem Statement

**Title**: Product of Array Except Self

**Problem Description**:  
Given an array of integers `nums`, return an array `output` such that `output[i]` is the **product of all elements** in `nums` **except** `nums[i]`.

You **cannot use division**, and the solution must run in **`O(n)` time**.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
nums = [1, 2, 4, 6]
```

**Output**:  
```python
[48, 24, 12, 8]
```

---

### Example 2  
**Input**:  
```python
nums = [-1, 0, 1, 2, 3]
```

**Output**:  
```python
[0, -6, 0, 0, 0]
```

---

## 📎 Constraints

- `2 <= nums.length <= 1000`  
- `-20 <= nums[i] <= 20`  
- The product is guaranteed to fit in a 32-bit integer

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(n)` (excluding output)

---

## 💡 Hints

- **Hint 1**:  
  Brute force (`O(n²)`) would compute product for every index by excluding it. Too slow!

- **Hint 2**:  
  Store repeated work using **prefix** and **suffix** arrays.

- **Hint 3**:  
  - Left pass: Store **prefix products** (product of all elements before index `i`)
  - Right pass: Store **suffix products** (product of all elements after index `i`)

- **Hint 4**:  
  Final output: `output[i] = prefix[i] * suffix[i]`

---

## 📅 Date Done

**Date**: *02/06/2025*  
**Time Taken**: *30 minutes*

---
