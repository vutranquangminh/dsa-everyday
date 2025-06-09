# 🧮 Trapping Rain Water - Hard

This is the description of the **"Trapping Rain Water"** problem, where the goal is to calculate the total amount of water that can be trapped between elevation bars after raining.

---

## 📌 Problem Statement

**Title**: Trapping Rain Water

**Problem Description**:
You are given an array of non-negative integers `height`, where each element represents the height of a bar in an elevation map.
The width of each bar is 1. Rainwater can be trapped between these bars.

Return the **total amount of water** that can be trapped after it rains.

---

## 💡 Example 1

**Input**:

```python
height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
```

**Output**:

```python
9
```

**Explanation**:
The water is trapped between the bars as follows:

* Between index 1 and 3 → 2 units
* Between index 3 and 7 → 4 units
* Between index 7 and 9 → 3 units
  Total = 2 + 4 + 3 = 9 units

---

## ✅ Constraints

* `1 <= height.length <= 1000`
* `0 <= height[i] <= 1000`

---

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity**: `O(n)`
* **Space Complexity**: `O(n)` *(with prefix/suffix arrays)* or `O(1)` *(with two-pointer optimization)*

---

## 📅 Date Done

**Date**: *10/06/2025*
**Time Taken**: *150 minutes*

---
