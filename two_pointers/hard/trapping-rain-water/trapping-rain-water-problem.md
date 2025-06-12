
# 🧮 Trapping Rain Water - Hard

---

## 📌 Problem Statement

**Title**: Trapping Rain Water

**Problem Description**:  
You are given an array of non-negative integers `height`, where each `height[i]` represents the height of a bar in an elevation map (width of each bar is 1 unit).

Return the **maximum amount of water** that can be **trapped** between the bars after raining.

---

## 💡 Example

### Example 1  
**Input**:  
```python
height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
```

**Output**:  
```python
9
```

---

## 📎 Constraints

- `1 <= height.length <= 1000`  
- `0 <= height[i] <= 1000`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(n)` or better

---

## 💡 Hints

- **Hint 1**:  
  How much water can be stored **at each position**? Visualize water above bars.

- **Hint 2**:  
  Water trapped at index `i`:  
  `min(max_left, max_right) - height[i]`

- **Hint 3**:  
  Brute-force approach is `O(n²)` by scanning left and right for every `i`.

- **Hint 4**:  
  Precompute:
  - `prefix_max[i]` = max height from the **left** up to `i`  
  - `suffix_max[i]` = max height from the **right** up to `i`  
  Then apply:
  ```python
  water_at_i = min(prefix_max[i], suffix_max[i]) - height[i]
  ```

---

## 📅 Date Done

**Date**: *10/06/2025*
**Time Taken**: *150 minutes*

---