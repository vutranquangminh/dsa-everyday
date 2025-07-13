# 🧮 Library Fine – Easy

---

## 📌 Problem Statement

You’re given two dates:
- **Returned date**: when the book was actually returned
- **Due date**: when the book *should* have been returned

Your task is to **calculate the fine** based on this fee structure:

- ✅ If the book is returned **on or before the due date** → **fine = 0**
- 📅 If returned **after the due day**, but **same month and year** → **fine = 15 × number of late days**
- 📆 If returned **after the due month**, but **same year** → **fine = 500 × number of late months**
- 📤 If returned **in a different year** → **fixed fine = 10000**

---

## 💡 Examples with Explanation

### Example
**Input:**
```
9 6 2015
6 6 2015
```

**Returned:** 9 June 2015  
**Due:** 6 June 2015

- Same **month** and **year**
- 3 days late → `3 × 15 = 45`

**Output:**
```
45
```

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** `O(1)` (just date comparison)
- **Space Complexity:** `O(1)`

---

## 📎 Constraints

- Valid Gregorian calendar dates
- `1 ≤ d ≤ 31`, `1 ≤ m ≤ 12`, `1 ≤ y ≤ 3000`

---

## 💡 Hints

- Compare **year** → **month** → **day**
- Use only the **least precise unit** that applies
- Use conditional logic (if/elif/else)

---

## 📅 Date Done

**Date:** *06/07/2025*  
**Time Taken:** *3 minutes*

---