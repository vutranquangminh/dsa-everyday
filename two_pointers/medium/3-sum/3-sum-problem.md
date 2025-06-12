
# 🧮 3Sum - Medium

---

## 📌 Problem Statement

**Title**: 3Sum

**Problem Description**:  
Given an integer array `nums`, return **all unique triplets** `[nums[i], nums[j], nums[k]]` such that:

- `nums[i] + nums[j] + nums[k] == 0`
- `i`, `j`, and `k` are **distinct**
- No **duplicate triplets** are allowed in the output

You may return the triplets in **any order**.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
nums = [-1, 0, 1, 2, -1, -4]
```

**Output**:  
```python
[[-1, -1, 2], [-1, 0, 1]]
```

**Explanation**:  
Valid combinations that sum to zero:
- `[-1, 0, 1]`
- `[-1, -1, 2]`  
Duplicates are avoided.

---

### Example 2  
**Input**:  
```python
nums = [0, 1, 1]
```

**Output**:  
```python
[]
```

---

### Example 3  
**Input**:  
```python
nums = [0, 0, 0]
```

**Output**:  
```python
[[0, 0, 0]]
```

---

## 📎 Constraints

- `3 <= nums.length <= 1000`  
- `-10⁵ <= nums[i] <= 10⁵`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n²)`  
- **Space Complexity**: `O(1)` (excluding the result list)

---

## 💡 Hints

- **Hint 1**:  
  Brute-force (`O(n³)`) is too slow. Think about sorting and reducing complexity.

- **Hint 2**:  
  Sort the array. Fix `i`, then search for pairs with a **two-pointer approach**.

- **Hint 3**:  
  Equation becomes:  
  `nums[i] + nums[j] + nums[k] == 0` →  
  `nums[j] + nums[k] == -nums[i]`  
  Use two pointers on the subarray to the right of `i`.

- **Hint 4**:  
  Move pointers based on comparison between current sum and target (`-nums[i]`).

- **Hint 5**:  
  To avoid duplicates, skip over the same values for both `i`, `j`, and `k`.

---

## 📅 Date Done

**Date**: *07/06/2025*  
**Time Taken**: *90 minutes*

---