# 🧮 Counting Valleys - Easy

---

## 📌 Problem Statement

An avid hiker keeps meticulous records of their hikes. During a recent hike that took exactly `steps` number of steps, each step was recorded as either:

- `'U'` for **uphill** (step up by 1 unit)
- `'D'` for **downhill** (step down by 1 unit)

A hike **starts and ends at sea level (altitude 0)**.  
Your task is to count how many **valleys** the hiker walked through.

> A **valley** is a sequence of steps below sea level, starting with a `'D'` step from sea level and ending with a `'U'` step back to sea level.

---

## 💡 Examples

### Example 1

**Input:**
```
8
UDDDUDUU
```

**Output:**
```
1
```

**Explanation:**

Visual representation:
```
_/\      _
   \    /
    \/\/
```

- The hiker first goes down below sea level and comes back up → ✅ **1 valley**

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(n)  
- **Space Complexity**: O(1)

---

## 📎 Constraints

- 2 ≤ steps ≤ 10⁶  
- path.length == steps  
- path[i] ∈ {'U', 'D'}

---

## 💡 Hints

- Track current elevation using a variable (e.g., `elevation = 0`)
- If `elevation == 0` **right after** a `'U'` step → exited a valley → increment count

---

## 📅 Date Done

**Date**: *19/06/2025*  
**Time Taken**: *7 minutes*

---
