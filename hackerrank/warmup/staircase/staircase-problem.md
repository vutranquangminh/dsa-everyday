# 🧮 Staircase - Easy

---

## 📌 Problem Statement

**Title**: Staircase

**Problem Description**:  
You are given an integer `n` representing the **height and base width** of a staircase.  
Print a **right-aligned staircase** composed of `#` symbols and spaces.  
Each line `i` (where `1 ≤ i ≤ n`) should contain `n - i` spaces followed by `i` hash symbols.

---

## 💡 Examples

### Example 1  
**Input**:
```python
n = 6
```

**Output**:
```text
     #
    ##
   ###
  ####
 #####
######
```

**Explanation**:  
The staircase has 6 levels.  
Each line has `n - i` spaces and `i` `#` characters.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 ≤ n ≤ 100`

---

## 💡 Hints

- Use a loop to print `n` lines.
- For each line `i`, print `(n - i)` spaces followed by `i` hashes.
- Use string multiplication to simplify printing.

---

## ✅ Python Implementation

```python
def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)
```

---

## 📅 Date Done

**Date**: *03/06/2025*  
**Time Taken**: *1 minutes*

---
