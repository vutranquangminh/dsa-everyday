
# 🧮 Encode and Decode Strings - Medium

---

## 📌 Problem Statement

**Title**: Encode and Decode Strings

**Problem Description**:  
Design an algorithm to **encode** a list of strings into a **single string**,  
and a method to **decode** that string back into the **original list** of strings.

You must implement two functions:

```python
def encode(strs: List[str]) -> str:
    pass

def decode(s: str) -> List[str]:
    pass
```

The encoded string must be able to **perfectly reconstruct** the input list.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
["neet", "code", "love", "you"]
```

**Output**:  
```python
["neet", "code", "love", "you"]
```

---

### Example 2  
**Input**:  
```python
["we", "say", ":", "yes"]
```

**Output**:  
```python
["we", "say", ":", "yes"]
```

---

## 📎 Constraints

- `0 <= strs.length < 100`  
- `0 <= strs[i].length < 200`  
- `strs[i]` contains only UTF-8 characters

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(m)` per `encode()` and `decode()` call  
- **Space Complexity**: `O(m + n)`  
Where `m` is the total length of all strings and `n` is the number of strings

---

## 💡 Hints

- **Hint 1**:  
  Naive delimiter (e.g. comma or `~`) fails if it appears inside a string.

- **Hint 2**:  
  Instead of using a separator, encode using **string length**.

- **Hint 3**:  
  Use the format:  
  ```
  encoded = "4#neet4#code4#love3#you"
  ```  
  Then decode by reading the number until `#`, and extracting that many characters.

---

## 📅 Date Done

**Date**: *01/06/2025*  
**Time Taken**: *120 minutes*

---
