# 🧮 Angry Professor – Easy

---

## 📌 Problem Statement

A Discrete Mathematics professor is frustrated by students' tardiness. The professor **cancels class** if **fewer than `k` students** are present on time.

Each student has an arrival time:
- `≤ 0` means the student **arrived on time or early**
- `> 0` means the student **arrived late**

You're given multiple test cases. For each, determine whether the class is cancelled or not.

Return:
- `"YES"` if class is **cancelled**
- `"NO"` if class is **not cancelled**

---

## 💡 Examples

### 🔹 Example 1

**Input:**
```
2
4 3
-1 -3 4 2
4 2
0 -1 2 1
```

**Output:**
```
YES
NO
```

**Explanation:**

- **Test Case 1:**
  ```
  Total students = 4
  Threshold (k) = 3
  Arrival times = [-1, -3, 4, 2]
  On-time students = 2  → Not enough
  => Class is CANCELLED → "YES"
  ```

- **Test Case 2:**
  ```
  Total students = 4
  Threshold (k) = 2
  Arrival times = [0, -1, 2, 1]
  On-time students = 2 → Enough
  => Class is NOT cancelled → "NO"
  ```

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** O(n) per test case  
- **Space Complexity:** O(1)

---

## 📎 Constraints

- `1 ≤ T ≤ 10` – Number of test cases  
- `1 ≤ n ≤ 1000` – Number of students per test case  
- `-100 ≤ a[i] ≤ 100` – Arrival time of each student  
- `1 ≤ k ≤ n` – Minimum number of on-time students required

---

## 💡 Hints

- Count how many students have `arrival time ≤ 0`
- If this number < `k`, return `"YES"` (class cancelled)
- Otherwise, return `"NO"`

---

## 📅 Date Done

**Date:** *11/07/2025*  
**Time Taken:** *10 minutes*

---