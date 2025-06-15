
# 🧮 Valid Anagram - Easy

---

## 📌 Problem Statement

**Title**: Valid Anagram

**Problem Description**:  
Given two strings `s` and `t`, return `True` if `t` is an **anagram** of `s`, and `False` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of another.  
The characters must match **in count**, but order does not matter.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
s = "racecar"
t = "carrace"
```

**Output**:  
```python
True
```

---

### Example 2  
**Input**:  
```python
s = "jar"
t = "jam"
```

**Output**:  
```python
False
```

---

## 📎 Constraints

- Both `s` and `t` consist of **lowercase English letters**

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n + m)`  
- **Space Complexity**: `O(1)` (since only lowercase letters are used)

---

## 💡 Hints

- **Hint 1**:  
  A brute-force approach would **sort** both strings and compare.  
  Time: `O(n log n + m log m)`

- **Hint 2**:  
  Order doesn't matter, only the **character counts** do.

- **Hint 3**:  
  Use a **hash map** or an array to **count character frequencies** in `s` and `t`, then compare the counts.

---

## 📅 Date Done

**Date**: *28/05/2025*  
**Time Taken**: *40 minutes*

---
