# 🧮 The Hurdle Race - Easy

---

## 📌 Problem Statement

A video game character is running a hurdle race. Each hurdle has a different height, and the character can jump up to a fixed maximum height `k` naturally.

However, the character can take a **magic potion** that increases their maximum jump height by **1 unit per dose**.

Your task is to calculate the **minimum number of doses** required so that the character can jump **all** the hurdles.  
If they can already jump all the hurdles, return `0`.

---

## 💡 Examples

### Example 1

**Input:**
```
5 4
1 6 3 5 2
```

**Output:**
```
2
```

**Explanation:**
- The character can jump `4` units naturally.
- The tallest hurdle is `6` → needs `6 - 4 = 2` extra units.
✅ So, the character needs **2 doses** of the potion.

---

### Example 2

**Input:**
```
5 7
2 5 4 5 2
```

**Output:**
```
0
```

**Explanation:**
- The character can jump `7` units.
- All hurdles are ≤ 7 → no potion needed.  
✅ So, the answer is **0**.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(n)  
- **Space Complexity**: O(1)

---

## 📎 Constraints

- 1 ≤ n ≤ 100  
- 1 ≤ k ≤ 100  
- 1 ≤ height[i] ≤ 100

---

## 💡 Hints

- Find the **maximum** hurdle height.
- Subtract the natural jump height `k`.
- If the result is negative, return `0`.

---

## 📅 Date Done

**Date**: *23/06/2025*  
**Time Taken**: *5 minutes*

---