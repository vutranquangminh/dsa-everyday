
# 🧮 Valid Parentheses - Easy

---

## 📌 Problem Statement

**Title**: Valid Parentheses

**Problem Description**:  
You are given a string `s` consisting only of the characters:  
`'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`.

The string is **valid** if:

- Every open bracket has a corresponding **same type** close bracket.
- Brackets are **closed in the correct order**.
- Every closing bracket has a corresponding **opening bracket** of the same type.

**Return `true` if `s` is valid, otherwise return `false`.**

---

## 💡 Examples

### Example 1  
**Input**:  
```python
s = "[]"
```
**Output**:  
```python
True
```

### Example 2  
**Input**:  
```python
s = "([{}])"
```
**Output**:  
```python
True
```

### Example 3  
**Input**:  
```python
s = "[(])"
```
**Output**:  
```python
False
```

**Explanation**: The brackets are not closed in the correct order.

---

## 📎 Constraints

- `1 <= s.length <= 1000`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(n)`

---

## 💡 Hints

- **Hint 1**:  
  A brute-force solution could try removing pairs of brackets repeatedly, but that results in `O(n^2)`. Can we do better?

- **Hint 2**:  
  A **stack** is ideal. Push opening brackets; pop and check for closing brackets.

- **Hint 3**:  
  If the stack is **empty at the end**, and every closing matched an opening – the string is valid.

---

## 📅 Date Done

**Date**: *11/06/2025*  
**Time Taken**: *60 minutes*

---