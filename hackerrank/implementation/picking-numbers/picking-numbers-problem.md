# 🧮 Picking Numbers - Easy

---

## 📌 Problem Statement

Given an array of integers, find the **length of the longest subarray** where the **absolute difference between any two elements is less than or equal to 1**.

You may **choose any subset of the array elements** (not necessarily contiguous), but they must all have pairwise differences ≤ 1.

---

## 💡 Examples

### Example 1

**Input:**
```
6
4 6 5 3 3 1
```

**Output:**
```
3
```

**Explanation:**
We choose the multiset: `[4, 5, 5]` or `[3, 3, 4]`.  
- The maximum subset length is 3, and all pairwise differences are ≤ 1.

---

### Example 2

**Input:**
```
6
1 2 2 3 1 2
```

**Output:**
```
5
```

**Explanation:**
We choose the multiset: `[1, 2, 2, 1, 2]`.  
- All values are either 1 or 2, so the absolute difference between any pair is ≤ 1.  
- Length = 5

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(n)  
- **Space Complexity**: O(n)

---

## 📎 Constraints

- 1 ≤ n ≤ 100  
- 0 ≤ a[i] ≤ 100  
- The answer is guaranteed to be ≥ 2

---

## 💡 Hints

- Count the frequency of each number.
- For each number `i`, check the total of `count[i] + count[i + 1]`.
- Keep track of the maximum such total.

---

## 📅 Date Done

**Date**: *22/06/2025*  
**Time Taken**: *6 minutes*

---