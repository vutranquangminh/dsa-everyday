
# 🧮 Evaluate Reverse Polish Notation - Medium

---

## 📌 Problem Statement

**Title**: Evaluate Reverse Polish Notation

**Problem Description**:  
You are given an array of strings `tokens` representing a valid **Reverse Polish Notation (RPN)** arithmetic expression.

Return the **integer result** after evaluating the expression.

> Valid operators are `+`, `-`, `*`, and `/`.  
> Division always **truncates toward zero**.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
tokens = ["1", "2", "+", "3", "*", "4", "-"]
```

**Output**:  
```python
5
```

**Explanation**:  
((1 + 2) * 3) - 4 = 5

---

## 📎 Constraints

- `1 <= tokens.length <= 1000`  
- `tokens[i]` is one of: `"+"`, `"-"`, `"*"`, `"/"` or a string representing an integer from `-100` to `100`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(n)`

---

## 💡 Hints

- **Hint 1**:  
  Brute force would scan and reduce operators → `O(n²)`. Too slow.

- **Hint 2**:  
  Use a **stack**:
  - Push numbers
  - On operator: pop 2 values, compute, then push the result

- **Hint 3**:  
  Stack keeps the **last two valid operands** close to each operator.  
  After evaluating the expression, the final result will be at the **top of the stack**.

---

## 📅 Date Done

**Date**: *13/06/2025*  
**Time Taken**: *60 minutes*

---