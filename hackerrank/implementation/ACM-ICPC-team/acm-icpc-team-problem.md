# 🧠 ACM ICPC Team – Easy

---

## 📌 Problem Statement

There are a number of people attending the **ACM-ICPC World Finals**. Each of them may be well versed in a number of topics. Given a list of topics known by each attendee (represented as **binary strings**), determine:

1. The **maximum number of topics** a 2-person team can know.
2. The **number of 2-person teams** that know that maximum number of topics.

Each subject has a column in the binary string, and a `'1'` means the subject is known while `'0'` means it is not.

You must return an integer array of two elements:

- The **first** is the maximum number of topics known.
- The **second** is the number of teams that know that many topics.

---

## 💡 Example

### 🔹 Example 1

**Input:**
```
4 5
10101
11100
11010
00101
```

**Output:**
```
5
2
```

### 🧾 Explanation:

Here are all the 2-person teams and the topics they collectively know:

| Team  | Combined Topics | Topics Known |
|-------|------------------|--------------|
| (1,2) | 10101 OR 11100 = 11101 | 4 topics |
| (1,3) | 10101 OR 11010 = 11111 | 5 topics ✅ |
| (1,4) | 10101 OR 00101 = 10101 | 3 topics |
| (2,3) | 11100 OR 11010 = 11110 | 4 topics |
| (2,4) | 11100 OR 00101 = 11101 | 4 topics |
| (3,4) | 11010 OR 00101 = 11111 | 5 topics ✅ |

👉 **Max topics known = 5**, and there are **2 teams** that know all 5.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** O(n² * m)  
- **Space Complexity:** O(1)

---

## 📎 Constraints

- `2 ≤ n ≤ 500` — number of people  
- `1 ≤ m ≤ 500` — number of topics  
- Each topic string contains only `'0'` or `'1'`.

---

## 💡 Hints

- For each pair of people, combine their topics using bitwise **OR**
- Count how many `'1'`s are in the combined string
- Track the maximum and how many times it occurs

---

## 📅 Date Done

**Date:** *20/07/2025*  
**Time Taken:** *10 minutes*
