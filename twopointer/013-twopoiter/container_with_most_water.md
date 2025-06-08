
# 🧮 Container With Most Water - Problem Description

This is the description of the **"Container With Most Water"** problem, where the goal is to find two lines that together with the x-axis form a container, such that the container holds the most water.

---

## 📌 Problem Statement

**Title**: Container With Most Water

**Problem Description**:  
You are given an integer array `height` where `height[i]` represents the height of the `i`-th vertical line on the x-axis.  
You may choose any two lines to form a container. The container is formed between the two lines and the x-axis.

Return the **maximum amount of water** a container can store.

---

## 💡 Example 1

**Input**:  
```python
height = [1, 7, 2, 5, 4, 7, 3, 6]
```

**Output**:  
```python
36
```

**Explanation**:  
The lines at indices `1` and `7` (heights 7 and 6) can form a container with width `6`.  
So, `min(7, 6) * 6 = 6 * 6 = 36`.

---

## 💡 Example 2

**Input**:  
```python
height = [2, 2, 2]
```

**Output**:  
```python
4
```

**Explanation**:  
Choose the first and last lines. Width = 2, height = min(2, 2) = 2 → Area = 2 * 2 = 4.

---

## ✅ Constraints

- `2 <= height.length <= 1000`  
- `0 <= height[i] <= 1000`

---

## ⏱️ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`  

---

## 📅 Date Done

**Date**: *08/06/2025*  
**Time Taken**: *30 minutes*
