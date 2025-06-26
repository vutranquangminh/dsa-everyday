# 🧮 Compare the Triplets - Easy

---

## 📌 Problem Statement

**Title**: Compare the Triplets

**Problem Description**:  
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories:  
- Problem clarity  
- Originality  
- Difficulty  

The rating for Alice's challenge is the triplet `a = (a[0], a[1], a[2])`, and for Bob's challenge it's `b = (b[0], b[1], b[2])`.

The task is to calculate their comparison points by comparing each category:

- If `a[i] > b[i]`, Alice gets 1 point.  
- If `a[i] < b[i]`, Bob gets 1 point.  
- If `a[i] == b[i]`, no points are awarded.  

Return an array of two integers: the first for Alice’s score, the second for Bob’s.

---

## 💡 Examples

### Example 1  
**Input**:  
```python
a = [5, 6, 7]  
b = [3, 6, 10]
```

**Output**:  
```python
[1, 1]
```

**Explanation**:  
- `a[0] > b[0]` → Alice gets 1 point  
- `a[1] == b[1]` → No points  
- `a[2] < b[2]` → Bob gets 1 point  
So the result is `[1, 1]`.

---

### Example 2  
**Input**:  
```python
a = [17, 28, 30]  
b = [99, 16, 8]
```

**Output**:  
```python
[2, 1]
```

**Explanation**:  
- `a[0] < b[0]` → Bob gets 1 point  
- `a[1] > b[1]` and `a[2] > b[2]` → Alice gets 2 points  
So the result is `[2, 1]`.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(1)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 ≤ a[i] ≤ 100`  
- `1 ≤ b[i] ≤ 100`

---

## 💡 Hints

- Use a loop to compare values at each index.  
- Keep two counters: one for Alice and one for Bob.

---

## 📅 Date Done

**Date**: *30/05/2025*  
**Time Taken**: *3 minutes*

---