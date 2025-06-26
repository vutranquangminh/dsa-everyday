
# 🧮 Single Number - Easy

---

## 📌 Problem Statement

You are given a **non-empty** array of integers `nums`.  
Every element appears **twice** except for **one** element, which appears only **once**.

Your task is to **find that single number**.

You **must** implement a solution with **linear runtime complexity** and use only **constant extra space**.

---

## 💡 Examples

### Example 1
**Input**:
```python
nums = [2, 2, 1]
```

**Output**:
```python
1
```

---

### Example 2
**Input**:
```python
nums = [4, 1, 2, 1, 2]
```

**Output**:
```python
4
```

---

### Example 3
**Input**:
```python
nums = [1]
```

**Output**:
```python
1
```

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 <= nums.length <= 3 * 10⁴`  
- `-3 * 10⁴ <= nums[i] <= 3 * 10⁴`  
- Every element appears **twice** except for **one**

---

## 💡 Hints

- Think about the properties of the **bitwise XOR (`^`)** operation:
  - `a ^ a = 0`
  - `a ^ 0 = a`
- XORing all numbers together will cancel out the ones that appear twice, leaving only the single number.

---

## 📅 Date Done

**Date**: *21/06/2025*  
**Time Taken**: *10 minutes*

---