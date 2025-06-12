
# 🧮 Container With Most Water - Medium

---

## 📌 Problem Statement

**Title**: Container With Most Water

**Problem Description**:  
You are given an array `height` where `height[i]` represents the height of the `iᵗʰ` vertical bar.  

You may choose **any two bars** to form a container.  
Return the **maximum amount of water** a container can store between them.

> The container’s water volume is calculated by:  
> `width * min(height[i], height[j])`

---

## 💡 Examples

### Example 1  
**Input**:  
```python
height = [1, 7, 2, 5, 4, 7, 3, 6]
```

**Output**:  
```python
36
```

---

### Example 2  
**Input**:  
```python
height = [2, 2, 2]
```

**Output**:  
```python
4
```

---

## 📎 Constraints

- `2 <= height.length <= 1000`  
- `0 <= height[i] <= 1000`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`

---

## 💡 Hints

- **Hint 1**:  
  Brute-force checks all pairs of lines → `O(n²)` — can be too slow.

- **Hint 2**:  
  You can use a **two-pointer** technique.

- **Hint 3**:  
  Water between two bars = `(j - i) * min(height[i], height[j])`.  
  Move the pointer with the **smaller height** to potentially find a better area.

- **Hint 4**:  
  Because the **shorter bar limits the water**, shifting it gives a chance to find a **taller one**.

---

## 📅 Date Done

**Date**: *08/06/2025*  
**Time Taken**: *30 minutes*

---