
# 🧮 Contains Duplicate - Easy

---

## 📌 Problem Statement

**Title**: Contains Duplicate

**Problem Description**:  
Given an integer array `nums`, return `True` **if any value appears more than once**, and `False` **if every element is distinct**.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
nums = [1, 2, 3, 3]
```

**Output**:  
```python
True
```

---

### Example 2  
**Input**:  
```python
nums = [1, 2, 3, 4]
```

**Output**:  
```python
False
```

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(n)`

---

## 📎 Constraints

- `1 <= nums.length <= 10⁵`  
- `-10⁹ <= nums[i] <= 10⁹`

---

## 💡 Hints

- **Hint 1**:  
  A brute-force solution uses nested loops → `O(n²)`. Too slow!

- **Hint 2**:  
  Think about a **data structure** that allows quick existence checks.

- **Hint 3**:  
  Use a **set** to store seen values.  
  If a value is already in the set, return `True`.  
  Otherwise, insert it and continue.

---

## 📅 Date Done

**Date**: *27/05/2025*  
**Time Taken**: *10 minutes*

---