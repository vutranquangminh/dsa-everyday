# 🧮 3 Sum - Medium

This is the description of the **"3 Sum"** problem, where the goal is to find all unique triplets in the array that sum up to zero.

---

## 📌 Problem Statement

**Title**: 3 Sum

**Problem Description**:  
Given an integer array `nums`, return all the **unique triplets** `[nums[i], nums[j], nums[k]]` such that:

- `nums[i] + nums[j] + nums[k] == 0`
- `i`, `j`, and `k` are all **distinct indices**

The solution **must not contain duplicate triplets**. You can return the triplets in **any order**.

---

## 💡 Example 1

**Input**:  
```python
nums = [-1, 0, 1, 2, -1, -4]
```

**Output**:  
```python
[[-1, -1, 2], [-1, 0, 1]]
```

**Explanation**:  
Valid triplets that sum to zero include:
- (-1) + 0 + 1
- (-1) + (-1) + 2

---

## 💡 Example 2

**Input**:  
```python
nums = [0, 1, 1]
```

**Output**:  
```python
[]
```

**Explanation**:  
No valid triplet that sums to zero.

---

## 💡 Example 3

**Input**:  
```python
nums = [0, 0, 0]
```

**Output**:  
```python
[[0, 0, 0]]
```

**Explanation**:  
A single valid triplet exists with all elements zero.

---

## ✅ Constraints

- `3 <= nums.length <= 1000`  
- `-10^5 <= nums[i] <= 10^5`  

---

## ⏱️ Recommended Time & Space Complexity

- **Time Complexity**: `O(n^2)`  
- **Space Complexity**: `O(1)` (excluding output)

---

## 📅 Date Done

**Date**: *07/06/2025*  
**Time Taken**: *90 minutes*

---