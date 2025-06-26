
# 🧮 Minimum Stack - Medium

---

## 📌 Problem Statement

**Title**: Minimum Stack

**Problem Description**:  
Design a stack class with the following operations — all in **`O(1)` time**:

- `MinStack()` — Initializes the stack object.  
- `push(int val)` — Pushes the element `val` onto the stack.  
- `pop()` — Removes the element on the top of the stack.  
- `top()` — Returns the top element.  
- `getMin()` — Retrieves the **minimum element** in the stack.

---

## 💡 Example

### Example 1  
**Input**:  
```python
["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
```

**Output**:  
```python
[None, None, None, None, 0, None, 2, 1]
```

**Explanation**:
```python
MinStack minStack = new MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
minStack.getMin() -> 0
minStack.pop()
minStack.top()    -> 2
minStack.getMin() -> 1
```

---

## 📎 Constraints

- `-2^31 <= val <= 2^31 - 1`  
- `pop()`, `top()`, and `getMin()` are only called on **non-empty stacks**

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(1)` for all operations  
- **Space Complexity**: `O(n)` where `n` is the number of pushed elements

---

## 💡 Hints

- **Hint 1**:  
  A brute-force `getMin()` would scan the stack each time → `O(n)` — not ideal.

- **Hint 2**:  
  Maintain **two stacks**:  
  1️⃣ Main stack for all values  
  2️⃣ Auxiliary stack that tracks **current min** at each step

- **Hint 3**:  
  When pushing, push the `min(val, current_min)` to the **min stack**.  
  When popping, pop from **both stacks** to maintain sync.

---

## 📅 Date Done

**Date**: *12/06/2025*  
**Time Taken**: *30 minutes*

---