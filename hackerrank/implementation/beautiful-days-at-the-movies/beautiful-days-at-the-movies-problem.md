# 🧮 Beautiful Days at the Movies – Easy

---

## 📌 Problem Statement

Lily loves playing with numbers. She invented a game where, for a given number `x`, she:
- Reverses the digits of `x` → `reverse(x)`
- Calculates the absolute difference `|x - reverse(x)|`
- If this difference is **divisible by `k`**, the day is considered **beautiful**.

Given a range of days from `i` to `j` (inclusive), return the number of **beautiful days**.

---

## 💡 Examples

### 🔹 Example 1

**Input:**
```
20 23 6
```

**Output:**
```
2
```

**Explanation:**

We check each day from `20` to `23`:

- Day 20 → Reverse: 02 → `|20 - 2| = 18` → `18 % 6 == 0` ✅ → Beautiful  
- Day 21 → Reverse: 12 → `|21 - 12| = 9` → `9 % 6 == 3` ❌  
- Day 22 → Reverse: 22 → `|22 - 22| = 0` → `0 % 6 == 0` ✅ → Beautiful  
- Day 23 → Reverse: 32 → `|23 - 32| = 9` → `9 % 6 == 3` ❌  

➡️ Total beautiful days = **2**

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** O(n) where `n = j - i + 1`  
- **Space Complexity:** O(1)

---

## 📎 Constraints

- `1 ≤ i ≤ j ≤ 2 × 10^6`  
- `1 ≤ k ≤ 2 × 10^9`

---

## 💡 Hints

- Write a helper function to **reverse the digits** of a number
- Loop through all days from `i` to `j`, and for each:
  - Compute the reversed number
  - Check if `abs(day - reverse(day)) % k == 0`

---

## 📅 Date Done

**Date:** *27/06/2025*  
**Time Taken:** *7 minutes*

---