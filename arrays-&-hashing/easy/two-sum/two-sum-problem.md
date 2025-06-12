
# 🧮 Two Sum - Easy

---

## 📌 Problem Statement

**Title**: Two Sum

**Problem Description**:  
Given an array of integers `nums` and an integer `target`, return **the indices `[i, j]`** such that:

- `nums[i] + nums[j] == target`  
- `i != j`  
- Return the answer with the **smaller index first**

You may assume **exactly one valid solution exists**.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
nums = [3, 4, 5, 6]
target = 7
```

**Output**:  
```python
[0, 1]
```

---

### Example 2  
**Input**:  
```python
nums = [4, 5, 6]
target = 10
```

**Output**:  
```python
[0, 2]
```

---

### Example 3  
**Input**:  
```python
nums = [5, 5]
target = 10
```

**Output**:  
```python
[0, 1]
```

---

## 📎 Constraints

- `2 <= nums.length <= 1000`  
- `-10⁷ <= nums[i] <= 10⁷`  
- `-10⁷ <= target <= 10⁷`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(n)`

---

## 💡 Hints

- **Hint 1**:  
  Brute-force tries all pairs → `O(n²)`. Not optimal.

- **Hint 2**:  
  Rearranged:  
  `nums[i] + nums[j] == target` → `target - nums[i] == nums[j]`

- **Hint 3**:  
  Use a **hashmap** to store elements and their indices.  
  While iterating, check if `target - nums[i]` exists in the hashmap.

---

## 📅 Date Done

**Date**: *29/05/2025*  
**Time Taken**: *45 minutes*

---
