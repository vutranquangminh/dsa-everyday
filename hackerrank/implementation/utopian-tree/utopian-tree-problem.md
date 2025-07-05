# 🧮 Utopian Tree - Easy

---

## 📌 Problem Statement

The Utopian Tree goes through **two growth cycles each year**:
- 🌱 In **spring**, the tree **doubles** in height.
- ☀️ In **summer**, the tree's height **increases by 1 meter**.

A Utopian Tree sapling with a height of **1 meter** is planted at the onset of spring.  
Given an integer `n`, representing the number of growth cycles, determine the final **height** of the tree after `n` cycles.

---

## 💡 Examples

### Example 1

**Input:**
```
3
0
1
4
```

**Output:**
```
1
2
7
```

**Explanation:**

- **Test Case 1 (n = 0)**:  
  The tree hasn't grown yet → height = 1

- **Test Case 2 (n = 1)**:  
  Cycle 1 (Spring): 1 × 2 = 2

- **Test Case 3 (n = 4)**:
  ```
  Cycle 0: 1
  Cycle 1 (Spring): 1 × 2 = 2
  Cycle 2 (Summer): 2 + 1 = 3
  Cycle 3 (Spring): 3 × 2 = 6
  Cycle 4 (Summer): 6 + 1 = 7
  ```
  → Final height = **7**

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(n) per test case  
- **Space Complexity**: O(1)

---

## 📎 Constraints

- `1 ≤ T ≤ 10` – Number of test cases  
- `0 ≤ n ≤ 60` – Number of growth cycles per test case

---

## 💡 Hints

- Initialize `height = 1`
- Loop from `0` to `n - 1`:
  - If the cycle is **even** (spring), multiply by 2
  - If the cycle is **odd** (summer), add 1

---

## 📅 Date Done

**Date**: *25/06/2025*  
**Time Taken**: *5 minutes*

---