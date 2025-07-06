# 🧮 Viral Advertising – Easy

---

## 📌 Problem Statement

HackerLand Enterprise has a viral advertising strategy:

- On **Day 1**, the ad is shared with exactly `5` people.
- Each day:
  - Only **half** of the recipients like the ad (rounded down)
  - Each person who likes it **shares it with 3 new friends**
- This process continues for `n` days.

You are asked to find the **total number of people who have liked the ad by Day `n`**.

---

## 💡 Example

### 🔹 Example 1

**Input:**
```
3
```

**Output:**
```
9
```

**Explanation:**

Day-wise breakdown:

| Day | Shared | Liked | Cumulative |
|-----|--------|-------|------------|
| 1   | 5      | 2     | 2          |
| 2   | 6      | 3     | 5          |
| 3   | 9      | 4     | 9          |

So, after **Day 3**, the total number of likes is **9**.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

## 📎 Constraints

- `1 ≤ n ≤ 50`

---

## 💡 Hints

- Start with `shared = 5`
- For each day from 1 to `n`:
  - `liked = shared // 2`
  - `cumulative += liked`
  - `shared = liked * 3`

---

## 📅 Date Done

**Date:** *28/06/2025*  
**Time Taken:** *5 minutes*

---