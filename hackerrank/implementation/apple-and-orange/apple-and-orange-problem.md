# 🧮 Count Apples and Oranges - Easy

---

## 📌 Problem Statement

**Title**: Count Apples and Oranges

**Problem Description**:  
Sam’s house is located on a number line between points `s` and `t`. There is an **apple tree** at point `a` and an **orange tree** at point `b`. When fruit falls, it may land at a distance `d` from its tree:

- Positive `d` → fruit falls to the right.
- Negative `d` → fruit falls to the left.

You are given:
- Positions of Sam’s house (`s`, `t`)
- Tree locations (`a` for apple, `b` for orange)
- Lists of distances each apple and orange falls

**Determine how many apples and oranges fall on Sam’s house**, i.e., within `[s, t]` inclusive.

---

## 💡 Examples

### Example 1

**Input**:
```python
s = 7
t = 11
a = 5
b = 15
apples = [-2, 2, 1]
oranges = [5, -6]
```

**Output**:
```text
1
1
```

**Explanation**:
- Apples land at: `3`, `7`, `6` → only `7` is in `[7, 11]`.
- Oranges land at: `20`, `9` → only `9` is in `[7, 11]`.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n + m)` where `n` is number of apples and `m` is number of oranges  
- **Space Complexity**: `O(1)` (excluding input space)

---

## 📎 Constraints

- `1 <= s, t, a, b <= 10^5`
- `1 <= n, m <= 10^5`
- `-10^5 <= d <= 10^5`

---

## 💡 Hints

- Use list comprehension or a simple loop to compute the landing position of each fruit.
- Count how many fall in range `[s, t]`.

---

## 📅 Date Done

**Date**: *08/06/2025*  
**Time Taken**: *5 minutes*

---
