# 🧮 Sequence Equation - Easy

---

## 📌 Problem Statement

You're given a **permutation** of the first `n` positive integers as an array `p`, where each element is **distinct** and satisfies `1 ≤ p[i] ≤ n`.

Your task is to find, for every `x` from `1` to `n`, the value `y` such that:
```
p[p[y]] == x
```

👉 Then return the list of all such `y` values.

---

## 💡 Examples

### Example 1

**Input:**
```python
p = [2, 3, 1]
```

**Output:**
```python
2
3
1
```

**Explanation:**

Let’s break it down:
- For `x = 1`: `p[3] = 1` → `y = 3`
- For `x = 2`: `p[1] = 2` → `y = 1`
- For `x = 3`: `p[2] = 3` → `y = 2`

Then `p[p[3]] = x`, so print `2`, `3`, `1`.

---

### Example 2

**Input:**
```python
p = [4, 3, 5, 1, 2]
```

**Output:**
```python
1
3
5
4
2
```

**Explanation:**

Find `y` such that `p[p[y]] = x` for each `x` in `1` to `n = 5`.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** `O(n)`  
- **Space Complexity:** `O(n)`

---

## 📎 Constraints

- `1 ≤ n ≤ 50`
- All values in `p` are distinct
- Each `p[i]` is within the range `1 ≤ p[i] ≤ n`

---

## 💡 Hints

- Use a **dictionary or array** to reverse lookup positions.
- Build a map: `val -> index`
- Then for each `x`:  
  ```python
  y = position[position[x]]
  ```

---

## 📅 Date Done

**Date:** *01/07/2025*  
**Time Taken:** *5 minutes*

---