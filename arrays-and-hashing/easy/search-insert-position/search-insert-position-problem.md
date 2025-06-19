
# 🧮 Search Insert Position - Easy

---

## 📌 Problem Statement

Given a **sorted array** of **distinct integers** and a **target** value, return the **index if the target is found**.  
If not, return the **index where it would be inserted** in order.

You must write an algorithm with **`O(log n)` runtime complexity**.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
nums = [1, 3, 5, 6], target = 5
```

**Output**:  
```python
2
```

---

### Example 2  
**Input**:  
```python
nums = [1, 3, 5, 6], target = 2
```

**Output**:  
```python
1
```

---

### Example 3  
**Input**:  
```python
nums = [1, 3, 5, 6], target = 7
```

**Output**:  
```python
4
```

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(log n)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 <= nums.length <= 10⁴`  
- `-10⁴ <= nums[i] <= 10⁴`  
- `nums` contains **distinct values** sorted in **ascending** order  
- `-10⁴ <= target <= 10⁴`

---

## 💡 Hints

- Think about how **binary search** works.
- Modify the logic to return the **insert position** when the target is not found.

---

## 📅 Date Done

**Date**: *19/06/2025*  
**Time Taken**: *5 minutes*

---