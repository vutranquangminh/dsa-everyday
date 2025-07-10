# 🧮 Find Digits - Easy

---

## 📌 Problem Statement

Given an integer `n`, count how many of its digits are **divisors** of `n`.

- A digit `d` is a **divisor** of `n` if `n % d == 0`.
- Skip any digit equal to `0` (since division by 0 is undefined).
- You will be given `t` test cases. Return the count for each.

---

## 💡 Examples

### Example 1

**Input:**
```plaintext
2
12
1012
```

**Output:**
```plaintext
2
3
```

**Explanation:**

1. For `n = 12` → Digits: `1`, `2`  
   Both `12 % 1 == 0` and `12 % 2 == 0` → ✅ Count = `2`

2. For `n = 1012` → Digits: `1`, `0`, `1`, `2`  
   - `1012 % 1 == 0` → ✅  
   - `0` → ❌ Skip (division by zero)  
   - `1012 % 1 == 0` → ✅  
   - `1012 % 2 == 0` → ✅  
   → ✅ Count = `3`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** `O(d)` per test case (where `d` is number of digits in `n`)
- **Space Complexity:** `O(1)`

---

## 📎 Constraints

- `1 ≤ t ≤ 15`
- `0 < n < 10⁹`

---

## 💡 Hints

- Convert the number to a string to iterate over digits easily.
- Watch out for `0` digits (don’t divide by zero).

---

## 📅 Date Done

**Date:** *03/07/2025*  
**Time Taken:** *5 minutes*

---