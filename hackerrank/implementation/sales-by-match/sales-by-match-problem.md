# 🧮 Sales by Match - Easy

---

## 📌 Problem Statement

There is a large pile of socks that must be **paired by color**. Given an array of integers where each integer represents a **sock's color**, determine **how many matching pairs** of socks there are.

---

## 💡 Examples

### Example 1

**Input:**
```
9
10 20 20 10 10 30 50 10 20
```

**Output:**
```
3
```

**Explanation:**

Sock color counts:
- 10 → 4 socks → 2 pairs
- 20 → 3 socks → 1 pair
- 30 → 1 sock → 0 pairs
- 50 → 1 sock → 0 pairs

Total = **3 pairs**

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(k), where k is the number of distinct colors

---

## 📎 Constraints

- 1 ≤ n ≤ 100  
- 1 ≤ ar[i] ≤ 100, where `ar[i]` is the color of the i-th sock

---

## 💡 Hints

- Use a dictionary or counter to keep track of how many socks of each color you have.
- Integer divide each count by 2 to get the number of pairs.

---

## 📅 Date Done

**Date**: *17/06/2025*  
**Time Taken**: *2 minutes*

---
