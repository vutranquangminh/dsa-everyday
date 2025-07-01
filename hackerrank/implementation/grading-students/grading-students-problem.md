# 🧮 Grading Students - Easy

---

## 📌 Problem Statement

**Title**: Grading Students  

**Problem Description**:  
HackerLand University has the following grading policy:

- Every student receives a grade in the range `0` to `100`.
- Any grade less than `40` is considered failing.
- Sam, a professor, rounds grades based on these rules:
  - If the difference between the grade and the next multiple of 5 is less than 3, round **up** to the next multiple of 5.
  - If the grade is less than 38, **no rounding occurs** (as it would still be a failing grade).

Your task is to implement a function that takes a list of student grades and applies the rounding policy.

---

## 💡 Examples

### Example 1
**Input**:
```python
grades = [73, 67, 38, 33]
```

**Output**:
```text
75
67
40
33
```

**Explanation**:
- `73` → next multiple of 5 is `75`, difference is `2` → round up.
- `67` → next multiple of 5 is `70`, difference is `3` → do not round.
- `38` → next multiple of 5 is `40`, difference is `2` → round up.
- `33` < `38` → do not round.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(n)` (to store the final list)

---

## 📎 Constraints

- `1 <= n <= 60`
- `0 <= grade <= 100`

---

## 💡 Hints

- Use the modulo operator `%` to check how far the grade is from the next multiple of 5.
- Only apply rounding if the grade is ≥ 38.

---

## 📅 Date Done

**Date**: *07/06/2025*  
**Time Taken**: *3 minutes*

---
