# 🧮 Modified Kaprekar Numbers – Easy

---

## 📌 Problem Statement

A **modified Kaprekar number** is a positive whole number with a special property:

> If you square it, then split the number into two parts and sum those parts, you get the original number back.

More formally:

- Let `n` be a positive whole number with `d` digits.
- Compute `n²`, then split the number into two parts: `l` (left) and `r` (right), where `r` has exactly `d` digits (add leading zeros if necessary).
- Convert both `l` and `r` back to integers.
- If `l + r == n`, then `n` is a modified Kaprekar number.

🧠 **Note:** `r` may have leading zeros, and `l` can be 0 if `n²` has exactly `d` digits.

---

## 💡 Examples

### 🔹 Example 1

**Input:**
```
1
100
```

**Output:**
```
1 9 45 55 99
```

**Explanation:**

- `1² = 1 → "0" + "1" → 0 + 1 = 1 ✅`
- `9² = 81 → "8" + "1" → 8 + 1 = 9 ✅`
- `45² = 2025 → "20" + "25" = 20 + 25 = 45 ✅`
- `55² = 3025 → "30" + "25" = 30 + 25 = 55 ✅`
- `99² = 9801 → "98" + "01" = 98 + 1 = 99 ✅`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

## 📎 Constraints

- `1 ≤ p < q ≤ 10^5`

---

## 🛠️ Function Signature

```python
def kaprekarNumbers(p: int, q: int) -> None:
    # Your code goes here
```

---

## 🎯 Goal

Print all **modified Kaprekar numbers** in the inclusive range `[p, q]`, space-separated.  
If **none exist**, print:

```
INVALID RANGE
```

---

## 💡 Hints

- Always split `n²` such that the **right part has the same number of digits as `n`**.
- The left part can be empty or 0 if `n²` has exactly `d` digits.
- Watch out for leading zeros when converting strings to integers.

---

## 📅 Date Done

**Date:** *13/07/2025*  
**Time Taken:** *~15 minutes*

---