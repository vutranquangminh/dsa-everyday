# 🧮 Kangaroo - Easy

---

## 📌 Problem Statement

**Title**: Kangaroo

**Problem Description**:  
You are choreographing a circus act involving two kangaroos on a number line. Each kangaroo jumps in the positive direction:

- Kangaroo 1 starts at position `x1` and jumps `v1` meters per jump.
- Kangaroo 2 starts at position `x2` and jumps `v2` meters per jump.

Determine whether the two kangaroos will land on the **same position at the same time** after the **same number of jumps**.

Return `"YES"` if they can meet. Otherwise, return `"NO"`.

---

## 💡 Examples

### Example 1

**Input**:
```python
x1 = 0
v1 = 3
x2 = 4
v2 = 2
```

**Output**:
```text
YES
```

**Explanation**:
After 4 jumps:
- Kangaroo 1: 0 → 3 → 6 → 9 → 12  
- Kangaroo 2: 4 → 6 → 8 → 10 → 12  
They meet at position `12`.

---

### Example 2

**Input**:
```python
x1 = 0
v1 = 2
x2 = 5
v2 = 3
```

**Output**:
```text
NO
```

**Explanation**:
Kangaroo 2 is ahead and faster, so Kangaroo 1 can never catch up.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(1)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `0 <= x1 < x2 <= 10^4`
- `1 <= v1, v2 <= 10^4`

---

## 💡 Hints

- Set their positions equal:  
  `x1 + n*v1 = x2 + n*v2`  
  Solve for `n`:  
  `n = (x2 - x1) / (v1 - v2)`
- They can meet if:
  - `v1 > v2` (Kangaroo 1 is behind but faster)
  - The difference `(x2 - x1)` is divisible by `(v1 - v2)`

---

## 📅 Date Done

**Date**: *09/06/2025*  
**Time Taken**: *5 minutes*

---
