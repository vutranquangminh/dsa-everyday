# Group Anagrams - Solution

This is my solution to the **"Group Anagrams"** problem, which groups strings that are anagrams of each other into sublists.

---

## 📌 Problem Statement

**Title**: Group Anagrams

**Problem Description**:  
Given an array of strings `strs`, group all anagrams together into sublists.  
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

### Example 1:  
**Input**:  
`strs = ["act","pots","tops","cat","stop","hat"]`

**Output**:  
`[["hat"],["act", "cat"],["stop", "pots", "tops"]]`

### Example 2:  
**Input**:  
`strs = ["x"]`

**Output**:  
`[["x"]]`

### Example 3:  
**Input**:  
`strs = [""]`

**Output**:  
`[[""]]`

### Constraints:
- `1 <= strs.length <= 1000`
- `0 <= strs[i].length <= 100`
- `strs[i]` is made up of lowercase English letters.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(m * n)`, where `m` is the number of strings and `n` is the length of the longest string.
- **Space Complexity**: `O(m)`

---

## 📅 Date Done

**Date**: 30/05/2025  
**Time Taken**: 150 minutes

---
