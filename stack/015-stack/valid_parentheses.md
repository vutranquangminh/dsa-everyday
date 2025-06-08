# 🧮 Valid Parentheses - Easy

This is the description of the **"Valid Parentheses"** problem, which checks if a given string of brackets is valid according to standard matching rules.

---

## 📌 Problem Statement

**Title**: Valid Parentheses

**Problem Description**:  
You are given a string `s` consisting of the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`. A string is considered **valid** if it satisfies all the following conditions:

- Every **open bracket** is closed by the **same type** of bracket.  
- Open brackets are closed in the **correct order**.  
- Every **close bracket** has a corresponding **open bracket** of the same type.

Return `true` if the string is valid, otherwise return `false`.

> **Note**: An empty string is considered valid.

---

### Example 1:
**Input**:  
```python
s = "[]"
```

**Output**:  
`true`

---

### Example 2:
**Input**:  
```python
s = "([{}])"
```

**Output**:  
`true`

---

### Example 3:
**Input**:  
```python
s = "[(])"
```

**Output**:  
`false`  
**Explanation**: The brackets are not closed in the correct order.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(n)`  

---

## 📅 Date Done

**Date**: *10/06/2025*  
**Time Taken**: *180 minutes*
