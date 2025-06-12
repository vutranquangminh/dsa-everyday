
# 🧮 Valid Palindrome - Easy

---

## 📌 Problem Statement

**Title**: Valid Palindrome

**Problem Description**:  
Given a string `s`, return `True` if it is a **palindrome**, and `False` otherwise.

A palindrome is a string that reads the **same forward and backward**, **ignoring case** and **non-alphanumeric** characters.

> **Note**: Alphanumeric characters consist of letters (`A-Z`, `a-z`) and digits (`0-9`).

---

## 💡 Examples

### Example 1  
**Input**:  
```python
s = "Was it a car or a cat I saw?"
```
**Output**:  
```python
True
```

**Explanation**:  
After removing non-alphanumeric characters and lowering case, the string becomes `"wasitacaroracatisaw"`, which **is a palindrome**.

---

### Example 2  
**Input**:  
```python
s = "tab a cat"
```
**Output**:  
```python
False
```

**Explanation**:  
Filtered string becomes `"tabacat"`, which is **not** a palindrome.

---

## 📎 Constraints

- `1 <= s.length <= 1000`  
- `s` contains only printable ASCII characters

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)` (if done with two pointers)

---

## 💡 Hints

- **Hint 1**:  
  Reversing the string and checking equality works — but uses `O(n)` space.

- **Hint 2**:  
  A string is a palindrome if the first character equals the last, second equals second last, etc.

- **Hint 3**:  
  Use **two pointers**: one from the start, one from the end. Skip non-alphanumeric characters and compare characters while moving toward the center.

---

## 📅 Date Done

**Date**: *05/06/2025*  
**Time Taken**: *15 minutes*

---