
# 🧮 Longest Consecutive Sequence - Medium

---

## 📌 Problem Statement

**Title**: Longest Consecutive Sequence

**Problem Description**:  
Given an array of integers `nums`, return the **length** of the **longest consecutive sequence** of elements that can be formed.

A **consecutive sequence** is defined as a sequence where each number is exactly **1 greater** than the previous number.  
👉 The elements **do not need to be adjacent** in the original array.

Your algorithm must run in **`O(n)`** time.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
nums = [2, 20, 4, 10, 3, 4, 5]
```

**Output**:  
```python
4
```

**Explanation**:  
The longest sequence is `[2, 3, 4, 5]`.

---

### Example 2  
**Input**:  
```python
nums = [0, 3, 2, 5, 4, 6, 1, 1]
```

**Output**:  
```python
7
```

**Explanation**:  
The sequence is `[0, 1, 2, 3, 4, 5, 6]`.

---

## 📎 Constraints

- `0 <= nums.length <= 1000`  
- `-10⁹ <= nums[i] <= 10⁹`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(n)`

---

## 💡 Hints

- **Hint 1**:  
  Brute-force: Start sequence at every element → `O(n²)`. Too slow!

- **Hint 2**:  
  A number is a **start of a sequence** if `num - 1` is **not in the array**.

- **Hint 3**:  
  Use a **hash set** for O(1) lookups.  
  Only build sequences from **starting points**.

---

## 📅 Date Done

**Date**: *03/06/2025*  
**Time Taken**: *30 minutes*

---