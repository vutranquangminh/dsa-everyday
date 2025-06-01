# Encode and Decode Strings - Solution

This is my solution to the **"Encode and Decode Strings"** problem, which encodes a list of strings into a single string and decodes it back to the original list.

---

## 📌 Problem Statement

**Title**: Encode and Decode Strings

**Problem Description**:  
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

### Example 1:
**Input**:  
`["neet","code","love","you"]`  

**Output**:  
`["neet","code","love","you"]`

### Example 2:
**Input**:  
`["we","say",":","yes"]`  

**Output**:  
`["we","say",":","yes"]`

### Constraints:
- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` contains only UTF-8 characters

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(m)` for each `encode()` and `decode()` call, where `m` is the sum of the lengths of all strings.
- **Space Complexity**: `O(m + n)`, where `m` is the total length of all strings, and `n` is the number of strings.

---

## 📅 Date Done

**Date**: 01/06/2025  
**Time Taken**: 120 minutes

---