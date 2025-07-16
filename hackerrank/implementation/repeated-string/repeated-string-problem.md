# 🧮 Repeated String - Easy

---

## 📌 Problem Statement

You are given a string `s` made up of **lowercase English letters**, which is **repeated infinitely**.  
Given an integer `n`, determine how many times the letter **`a`** appears in the **first `n` characters** of the infinite repetition of `s`.

---

## 💡 Examples

### Example 1

**Input:**
```
aba
10
```

**Output:**
```
7
```

**Explanation:**  
The infinitely repeated string starts as `abaabaabaa...`.  
The first 10 characters are:  
```
abaabaabaa
```
Count of `a`: **7**

---

### Example 2

**Input:**
```
a
1000000000000
```

**Output:**
```
1000000000000
```

**Explanation:**  
The string is just `"a"`, and repeating it forms a string of all `a`s.  
So the count of `a` in the first **10¹²** characters is exactly **10¹²**.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(1)  
- **Space Complexity**: O(1)

---

## 📎 Constraints

- `1 ≤ |s| ≤ 100`  
- `1 ≤ n ≤ 10¹²`

---

## 💡 Hints

- Count how many `a`s appear in the string `s`.
- Determine how many **full repeats** of `s` fit in the first `n` characters.
- Handle the **remaining** characters (if `n` is not a multiple of `len(s)`).
- Use arithmetic instead of building the full string.

---

## 📅 Date Done

**Date**: *08/07/2025*  
**Time Taken**: *5 minutes*

---