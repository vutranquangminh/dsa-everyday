# 🧮 Majority Element - Easy

---

## 📌 Problem Statement

You are given an array `nums` of size `n`.  
The **majority element** is the element that appears **more than ⌊n / 2⌋ times**.

You may assume that the **majority element always exists** in the array.

Your task is to **return the majority element**.

---

## 💡 Examples

### Example 1
**Input**:
```python
nums = [3, 2, 3]
```

**Output**:
```python
3
```

---

### Example 2
**Input**:
```python
nums = [2, 2, 1, 1, 1, 2, 2]
```

**Output**:
```python
2
```

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 <= nums.length <= 5 * 10⁴`  
- `-10⁹ <= nums[i] <= 10⁹`  
- The majority element **always exists** in the array.

---

## 💡 Hints

- Try using the **Boyer-Moore Voting Algorithm**:
  - Maintain a `count` and `candidate`.
  - Iterate and adjust the count depending on whether the current number matches the candidate.
  - This approach works in **O(n)** time and **O(1)** space.

---

## 📅 Date Done

**Date**: *22/06/2025*  
**Time Taken**: *5 minutes*  

---