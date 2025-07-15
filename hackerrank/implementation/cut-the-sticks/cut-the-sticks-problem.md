# 🧮 Cut the Sticks – Easy

---

## 📌 Problem Statement

You are given a number of sticks with varying lengths. Your task is to iteratively cut the sticks into smaller pieces, discarding the shortest pieces until none are left. At each iteration, you will:

1. Determine the length of the shortest stick remaining.
2. Cut that length from each of the longer sticks.
3. Discard all the pieces of the shortest length.
4. Repeat the process until only sticks of the same length remain.

You need to print the number of sticks that are left before each cut operation until there are none left.

---

## 💡 Examples with Explanation

### Example 1
**Input:**
```
6
5 4 4 2 2 8
```

**Explanation:**

- The initial sticks are `[5, 4, 4, 2, 2, 8]`. The shortest stick is of length 2.
  - **Cut:** Subtract 2 from each of the longer sticks.
  - Remaining sticks: `[3, 2, 2, 6]`
  - **Discard:** The 2-length pieces are discarded.
  - **Output:** `6`

- The next shortest stick is of length 2.
  - **Cut:** Subtract 2 from each of the longer sticks.
  - Remaining sticks: `[1, 4]`
  - **Output:** `4`

- The next shortest stick is of length 1.
  - **Cut:** Subtract 1 from the remaining stick.
  - Remaining stick: `[3]`
  - **Output:** `2`

- Finally, we are left with 1 stick.
  - **Output:** `1`

**Output:**
```
6
4
2
1
```

### Example 2
**Input:**
```
8
1 2 3 4 3 3 2 1
```

**Explanation:**

- The initial sticks are `[1, 2, 3, 4, 3, 3, 2, 1]`. The shortest stick is of length 1.
  - **Cut:** Subtract 1 from each of the longer sticks.
  - Remaining sticks: `[1, 2, 3, 3, 3, 2]`
  - **Discard:** The 1-length pieces are discarded.
  - **Output:** `8`

- The next shortest stick is of length 2.
  - **Cut:** Subtract 2 from each of the longer sticks.
  - Remaining sticks: `[1, 2, 2, 2]`
  - **Output:** `6`

- The next shortest stick is of length 1.
  - **Cut:** Subtract 1 from the remaining sticks.
  - Remaining sticks: `[1]`
  - **Output:** `4`

- Finally, we are left with 1 stick.
  - **Output:** `1`

**Output:**
```
8
6
4
1
```

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** `O(n * log n)` (due to the sorting process in each iteration)
- **Space Complexity:** `O(1)` (constant space for the operations)

---

## 📎 Constraints

- The input list contains integers representing the lengths of the sticks.
- `1 ≤ n ≤ 1000`, `1 ≤ arr[i] ≤ 1000`

---

## 💡 Hints

- Sort the array initially to make finding the shortest stick easy.
- Perform the cut by subtracting the shortest stick from all longer sticks.
- Discard the sticks of the shortest length and repeat the process until there are no sticks left.

---

## 📅 Date Done

**Date:** *07/07/2025*  
**Time Taken:** *5 minutes*

---
