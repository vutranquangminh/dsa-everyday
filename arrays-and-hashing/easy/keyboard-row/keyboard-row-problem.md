# 🧮 Keyboard Row - Easy

---

## 📌 Problem Statement

**Title**: Keyboard Row

**Problem Description**:  
You're given an array of strings `words`. Your task is to return a list of words that can be typed using letters from **only one row** of an **American QWERTY keyboard**.

**Note**:  
- Letters are **case-insensitive**. Both uppercase and lowercase letters are treated as belonging to the same keyboard row.

---

## 💡 Examples

### Example 1
**Input**:  
```python
words = ["Hello","Alaska","Dad","Peace"]
```

**Output**:  
```python
["Alaska", "Dad"]
```

**Explanation**:  
"Alaska" and "Dad" can each be typed using letters from only the **second row** of the keyboard.

---

### Example 2
**Input**:  
```python
words = ["omk"]
```

**Output**:  
```python
[]
```

**Explanation**:  
"omk" uses letters from multiple rows.

---

### Example 3
**Input**:  
```python
words = ["adsdf","sfd"]
```

**Output**:  
```python
["adsdf","sfd"]
```

**Explanation**:  
Both words use letters from the **second row**.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n * m)` — where `n` is the number of words, and `m` is the average length of each word.  
- **Space Complexity**: `O(1)` — ignoring the space used by the output list.

---

## 📎 Constraints

- `1 <= words.length <= 20`  
- `1 <= words[i].length <= 100`  
- `words[i]` consists of **English letters** (both lowercase and uppercase)

---

## 💡 Hints

- Convert all characters to lowercase for uniform comparison.
- Use sets to represent each keyboard row.
- Check whether **all letters** in a word belong to **one** of these sets.

---

## 📅 Date Done

**Date**: *16/06/2025*  
**Time Taken**: *5 minutes*

---
