# 🧮 Missing Number - Easy

---

## 📌 Problem Statement

You are given an array `nums` containing `n` **distinct numbers** in the range `[0, n]`.

Return the **only number** in the range that is **missing** from the array.

---

## 💡 Examples

### Example 1
**Input**:
```python
nums = [3, 0, 1]
```

**Output**:
```python
2
```

**Explanation**:  
The array has `n = 3`, so the range is `[0, 3]`.  
All numbers are present except `2`.

---

### Example 2
**Input**:
```python
nums = [0, 1]
```

**Output**:
```python
2
```

**Explanation**:  
The array has `n = 2`, so the range is `[0, 2]`.  
The missing number is `2`.

---

### Example 3
**Input**:
```python
nums = [9,6,4,2,3,5,7,0,1]
```

**Output**:
```python
8
```

**Explanation**:  
The array has `n = 9`, so the range is `[0, 9]`.  
The missing number is `8`.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)` (if done in-place or using math)

---

## 📎 Constraints

- `n == nums.length`
- `1 <= n <= 10⁴`
- `0 <= nums[i] <= n`
- All numbers in `nums` are **unique**

---

## 💡 Hints

- Can you use the **sum formula** for the first `n` natural numbers?  
- Try using XOR for a constant-space solution.

---

## 📅 Date Done

**Date**: *23/06/2025*  
**Time Taken**: *15 minutes*

---