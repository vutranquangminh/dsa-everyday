
# 🧮 Two Integer Sum II - Problem Description

This is the description of the **"Two Integer Sum II"** problem, where the goal is to find two numbers in a sorted array that add up to a given target.

---

## 📌 Problem Statement

**Title**: Two Integer Sum II

**Problem Description**:  
You are given a **sorted** array of integers `numbers` in **non-decreasing order**. Your task is to find **two distinct indices** `index1` and `index2` (1-indexed) such that:

- `numbers[index1 - 1] + numbers[index2 - 1] == target`
- `index1 < index2`

Return the pair `[index1, index2]`.  
It is guaranteed that **exactly one valid solution exists**.  
You **must not use extra space** (i.e., achieve `O(1)` space complexity).

> **Note**: Do not use the same element twice.

---

## 💡 Example 1

**Input**:  
```python
numbers = [1, 2, 3, 4]  
target = 3
```

**Output**:  
```python
[1, 2]
```

**Explanation**:  
The sum of `1` (at index 1) and `2` (at index 2) is `3`.

---

## ✅ Constraints

- `2 <= numbers.length <= 1000`  
- `-1000 <= numbers[i] <= 1000`  
- `-1000 <= target <= 1000`  

---

## ⏱️ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`  

---

## 📅 Date Done

**Date**: 07/06/2025  
**Time Taken**: 30 minutes

---