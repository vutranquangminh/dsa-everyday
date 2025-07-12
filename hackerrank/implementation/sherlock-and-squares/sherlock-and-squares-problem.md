# 🧮 Sherlock and Squares – Easy

---

## 📌 Problem Statement

Watson gives Sherlock a range of integers defined by two endpoints `a` and `b`. Sherlock must figure out **how many square integers** exist in that inclusive range.

A **square integer** is an integer that is the square of another integer, like:  
`1 (1^2), 4 (2^2), 9 (3^2), 16 (4^2)...`

Your task is to **return the number of perfect square integers** between `a` and `b` (inclusive).

---

## 💡 Examples with Explanation

### Example 1
**Input:**
```plaintext
3 9
```

**Output:**
```plaintext
2
```

**Explanation:**
- Square integers in this range: `4 (2^2), 9 (3^2)`
- ✅ Answer = 2

---

### Example 2
**Input:**
```plaintext
17 24
```

**Output:**
```plaintext
0
```

**Explanation:**
- No square numbers between 17 and 24
- ❌ So return 0

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

---

## 📎 Constraints

- `1 ≤ a ≤ b ≤ 10^9`
- `1 ≤ number of test cases ≤ 100`

---

## 💡 Hints

- Use `math.ceil(sqrt(a))` to find the first perfect square root ≥ `a`.
- Use `math.floor(sqrt(b))` to find the last perfect square root ≤ `b`.
- The total count is: `floor(sqrt(b)) - ceil(sqrt(a)) + 1`

---

## 📅 Date Done

**Date:** *05/07/2025*  
**Time Taken:** *5 minutes*

---