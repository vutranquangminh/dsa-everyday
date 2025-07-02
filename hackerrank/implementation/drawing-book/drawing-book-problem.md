# 🧮 Drawing Book - Easy

---

## 📌 Problem Statement

A student is asked to turn to page `p` in a book with `n` total pages. They can start turning pages from the **front** or the **back** of the book. Each turn flips two pages (left and right).

Your task is to determine the **minimum number of pages** the student needs to turn to reach page `p`.

---

## 💡 Examples

### Example 1

**Input:**
```
6
2
```

**Output:**
```
1
```

**Explanation:**

- From front: 1 → 2 → ✅ (1 page turn)
- From back: 6 → 5-4 → 3-2 → ✅ (2 page turns)  
✅ Minimum = **1**

---

### Example 2

**Input:**
```
5
4
```

**Output:**
```
0
```

**Explanation:**

- From front: 1 → 2 → 3-4 ✅ (2 page turns)
- From back: 5 → 4 ✅ (0 page turns)  
✅ Minimum = **0**

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

---

## 📎 Constraints

- 1 ≤ n ≤ 10⁵  
- 1 ≤ p ≤ n

---

## 💡 Hints

- From front: Number of turns = `p // 2`
- From back: Number of turns = `(n // 2) - (p // 2)`
- Return the **minimum** of the two values.

---

## 📅 Date Done

**Date**: *18/06/2025*  
**Time Taken**: *4 minutes*

---
