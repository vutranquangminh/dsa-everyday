
# 🧮 Group Anagrams - Medium

---

## 📌 Problem Statement

**Title**: Group Anagrams

**Problem Description**:  
Given an array of strings `strs`, group all **anagrams** together into sublists.  
Return the grouped anagrams in **any order**.

An **anagram** is a word or phrase formed by rearranging the letters of another — the **same characters** in **any order**.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
```

**Output**:  
```python
[["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
```

---

### Example 2  
**Input**:  
```python
strs = ["x"]
```

**Output**:  
```python
[["x"]]
```

---

### Example 3  
**Input**:  
```python
strs = [""]
```

**Output**:  
```python
[[""]]
```

---

## 📎 Constraints

- `1 <= strs.length <= 1000`  
- `0 <= strs[i].length <= 100`  
- `strs[i]` consists of **lowercase English letters**

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(m * n)`  
  where `m = len(strs)` and `n = length of the longest string`  
- **Space Complexity**: `O(m)`

---

## 💡 Hints

- **Hint 1**:  
  A basic solution is to sort each string and use the sorted result as a **hashmap key**.  
  Time: `O(m * n log n)`

- **Hint 2**:  
  You only care about **character frequency**, not order.

- **Hint 3**:  
  Use a **26-element tuple** (frequency of each letter) as the hash key for fast grouping.

---

## 📅 Date Done

**Date**: *30/05/2025*  
**Time Taken**: *150 minutes*

---