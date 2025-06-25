
# 🧮 Summary Ranges - Easy

---

## 📌 Problem Statement

You are given a **sorted** and **unique** integer array `nums`.

A **range** `[a, b]` represents all the integers from `a` to `b` (inclusive).  
Your task is to return the **smallest sorted list of ranges** that **exactly covers** all numbers in `nums`.

Each range should be returned as:

- `"a->b"` if `a != b`  
- `"a"` if `a == b`

No number should be left out or duplicated across ranges.

---

## 💡 Examples

### Example 1

**Input**:
```python
nums = [0, 1, 2, 4, 5, 7]
```

**Output**:
```python
["0->2", "4->5", "7"]
```

**Explanation**:  
- [0,2] → `"0->2"`  
- [4,5] → `"4->5"`  
- [7] → `"7"`

---

### Example 2

**Input**:
```python
nums = [0, 2, 3, 4, 6, 8, 9]
```

**Output**:
```python
["0", "2->4", "6", "8->9"]
```

**Explanation**:  
- [0] → `"0"`  
- [2,4] → `"2->4"`  
- [6] → `"6"`  
- [8,9] → `"8->9"`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)` (excluding output)

---

## 📎 Constraints

- `0 <= nums.length <= 20`
- `-2³¹ <= nums[i] <= 2³¹ - 1`
- All elements are **unique**
- `nums` is **sorted** in ascending order

---

## 💡 Hints

- Use two pointers or a single scan to track the start and end of each range.
- Watch for when a range ends by checking if the current number is not consecutive.

---

## 📅 Date Done

**Date**: *24/06/2025*  
**Time Taken**: *40 minutes*

---