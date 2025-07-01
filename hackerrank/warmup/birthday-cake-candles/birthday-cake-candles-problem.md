# 🧮 Birthday Cake Candles - Easy

---

## 📌 Problem Statement

**Title**: Birthday Cake Candles

**Problem Description**:  
You are in charge of the cake for a child’s birthday. The cake will have one candle for **each year** of their age.  
The child can only **blow out the tallest candles**.  
Your task is to **count how many candles** are the tallest.

---

## 💡 Examples

### Example 1  
**Input**:
```python
n = 4
candles = [3, 2, 1, 3]
```

**Output**:
```text
2
```

**Explanation**:  
The tallest candle height is `3`, and it appears **twice** in the list.  
So, the child can blow out `2` candles.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 ≤ n ≤ 10^5`  
- `1 ≤ candles[i] ≤ 10^7`

---

## 💡 Hints

- Use `max()` to find the tallest candle.
- Use `count()` to count how many times it appears.

---

## 📅 Date Done

**Date**: *05/06/2025*  
**Time Taken**: *3 minutes*

---
