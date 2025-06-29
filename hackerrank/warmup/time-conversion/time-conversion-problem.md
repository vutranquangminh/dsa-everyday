# 🧮 Time Conversion - Easy

---

## 📌 Problem Statement

**Title**: Time Conversion

**Problem Description**:  
Given a time in **12-hour AM/PM format**, convert it to **24-hour military time**.

---

## 💡 Examples

### Example 1  
**Input**:
```python
s = "07:05:45PM"
```

**Output**:
```text
19:05:45
```

### Example 2  
**Input**:
```python
s = "12:01:00PM"
```

**Output**:
```text
12:01:00
```

### Example 3  
**Input**:
```python
s = "12:01:00AM"
```

**Output**:
```text
00:01:00
```

**Explanation**:
- `12:00:00AM` is `00:00:00` in 24-hour time.  
- `12:00:00PM` remains `12:00:00`.  
- For all other PM hours, add `12` to the hour.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(1)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- Input string `s` is always a valid time in 12-hour format (`hh:mm:ssAM` or `hh:mm:ssPM`).

---

## 💡 Hints

- Use string slicing to extract hour, minute, second, and AM/PM parts.
- Convert to int and adjust based on AM/PM rules.
- Return the new formatted time with zero-padding if needed.

---

## ✅ Python Implementation

```python
def timeConversion(s):
    period = s[-2:]
    hh, mm, ss = map(int, s[:-2].split(':'))

    if period == "AM":
        if hh == 12:
            hh = 0
    else:  # PM
        if hh != 12:
            hh += 12

    return f"{hh:02}:{mm:02}:{ss:02}"
```

---

## 📅 Date Done

**Date**: *06/06/2025*  
**Time Taken**: *3 minutes*

---
