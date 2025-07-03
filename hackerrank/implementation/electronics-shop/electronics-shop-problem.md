# 🧮 Electronics Shop - Easy

---

## 📌 Problem Statement

A person wants to determine the **most expensive combination** of **one computer keyboard** and **one USB drive** that can be purchased without exceeding a given **budget**.

Given:
- A list of keyboard prices
- A list of USB drive prices
- A total budget `b`

Your task is to find the **maximum amount of money** that can be spent on **exactly one keyboard and one USB drive** without exceeding the budget.

> If it's **not possible** to buy both items, return `-1`.

---

## 💡 Examples

### Example 1

**Input:**
```
10 2 3
3 1
5 2 8
```

**Output:**
```
9
```

**Explanation:**

Options:
- 3 (keyboard) + 5 (drive) = 8  
- 3 + 2 = 5  
- 3 + 8 = 11 ❌ over budget  
- 1 + 5 = 6  
- 1 + 2 = 3  
- 1 + 8 = 9 ✅

✅ The most expensive valid combination is `1 + 8 = 9`.

---

### Example 2

**Input:**
```
5 1 1
4
5
```

**Output:**
```
-1
```

**Explanation:**

- 4 (keyboard) + 5 (drive) = 9 ❌ over budget  
No valid combination → return `-1`.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(n * m)  
- **Space Complexity**: O(1)

---

## 📎 Constraints

- 1 ≤ n, m ≤ 1000  
- 1 ≤ b ≤ 10⁶  
- 1 ≤ price ≤ 10⁶

---

## 💡 Hints

- Use nested loops to try all keyboard-drive pairs
- Track the maximum sum ≤ `b`
- Return `-1` if no valid combination is found

---

## 📅 Date Done

**Date**: *20/07/2025*  
**Time Taken**: *6 minutes*

---
