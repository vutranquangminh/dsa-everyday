
# 🧮 Top K Frequent Elements - Medium

---

## 📌 Problem Statement

**Title**: Top K Frequent Elements

**Problem Description**:  
Given an integer array `nums` and an integer `k`, return the `k` **most frequent elements** in the array.  
The answer is guaranteed to be **unique**.  
You may return the result in **any order**.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
nums = [1, 2, 2, 3, 3, 3]
k = 2
```

**Output**:  
```python
[2, 3]
```

---

### Example 2  
**Input**:  
```python
nums = [7, 7]
k = 1
```

**Output**:  
```python
[7]
```

---

## 📎 Constraints

- `1 <= nums.length <= 10⁴`  
- `-1000 <= nums[i] <= 1000`  
- `1 <= k <= number of distinct elements in nums`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(n)`  
Where `n = len(nums)`

---

## 💡 Hints

- **Hint 1**:  
  Brute-force sorts by frequency → `O(n log n)`. Can we improve?

- **Hint 2**:  
  Group elements based on their **frequency** using **bucket sort**.

- **Hint 3**:  
  Create buckets from 1 to `n` where each bucket holds numbers with that frequency.  
  Then collect from the **highest bucket** downward until you have `k` elements.

---

## 📅 Date Done

**Date**: *31/05/2025*  
**Time Taken**: *180 minutes*

---
