# 🧮 Divisible Sum Pairs - Easy

---

## 📌 Problem Statement

Given an array of integers and a positive integer `k`, determine how many pairs of indices `(i, j)` exist such that:
- `i < j`, and
- `ar[i] + ar[j]` is divisible by `k`.

---

## 💡 Examples

### Example 1

**Input:**
```python
n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]
```

**Output:**
```
5
```

**Explanation:**

The 5 valid pairs where the sum is divisible by 3 are:
- (0, 2) → 1 + 2 = 3
- (0, 5) → 1 + 2 = 3
- (1, 3) → 3 + 6 = 9
- (2, 4) → 2 + 1 = 3
- (4, 5) → 1 + 2 = 3

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(k)

---

## 📎 Constraints

- 2 ≤ n ≤ 100
- 1 ≤ ar[i] ≤ 100
- 1 ≤ k ≤ 100

---

## 💡 Hints

- Try using a **frequency array of remainders** to count how many numbers have a specific mod value.
- For each element, calculate its complement `(k - ar[i] % k) % k`.

---

## 📅 Date Done

**Date**: *13/06/2025*  
**Time Taken**: *5 minutes*

---