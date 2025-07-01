
# 🧮 Between Two Sets - Easy

---

## 📌 Problem Statement

You are given **two arrays** of integers:  
- Array `a`  
- Array `b`

You need to find **all integers `x`** such that:

1. Every element in `a` is a factor of `x` (i.e., `x % a[i] == 0`)
2. `x` is a factor of every element in `b` (i.e., `b[j] % x == 0`)

Your task is to determine **how many such integers `x` exist**. These integers are considered to be **between the two sets**.

---

## 💡 Examples

### Example 1

**Input:**
```python
a = [2, 4]
b = [16, 32, 96]
```

**Output:**
```text
3
```

**Explanation:**

Numbers that are multiples of `LCM(2, 4) = 4` and divide `GCD(16, 32, 96) = 16` are:
```
4, 8, 16
```
So, the result is `3`.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n log n + m log m)` (for LCM and GCD computation)  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 <= len(a), len(b) <= 10`
- `1 <= a[i], b[j] <= 100`

---

## 💡 Hints

- Use `math.lcm` or implement LCM via `lcm(x, y) = abs(x * y) // gcd(x, y)`
- Similarly, use `math.gcd` or reduce `gcd` over all elements in `b`
- Loop from `LCM of a` to `GCD of b`, incrementing by LCM step

---

## 📅 Date Done

**Date**: *10/06/2025*  
**Time Taken**: *10 minutes*

---