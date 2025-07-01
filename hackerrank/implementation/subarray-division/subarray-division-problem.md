
# 🧮 Birthday Chocolate - Easy

---

## 📌 Problem Statement

Lily wants to share a chocolate bar with Ron. The chocolate is divided into squares, each containing an integer.

Lily chooses a **contiguous segment** of the bar such that:
- The **number of squares** is equal to Ron’s **birth month** `m`.
- The **sum of the numbers** on those squares equals Ron’s **birth day** `d`.

Your task is to find **how many ways** Lily can choose such a segment.

---

## 💡 Examples

### Example 1

**Input:**
```python
s = [1, 2, 1, 3, 2]
d = 3
m = 2
```

**Output:**
```text
2
```

**Explanation:**

The valid segments of length `2` that sum to `3` are:
- `[1, 2]`
- `[2, 1]`

So the result is `2`.

---

### Example 2

**Input:**
```python
s = [1, 1, 1, 1, 1, 1]
d = 3
m = 2
```

**Output:**
```text
0
```

**Explanation:**

No contiguous segment of length `2` adds up to `3`.

---

### Example 3

**Input:**
```python
s = [4]
d = 4
m = 1
```

**Output:**
```text
1
```

**Explanation:**

Only one segment (the single square itself) matches the criteria.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 <= n <= 100`
- `1 <= s[i] <= 5`
- `1 <= d <= 31`
- `1 <= m <= 12`

---

## 💡 Hints

- Use a **sliding window** of size `m` to check all valid segments.
- For each segment, check if the sum equals `d`.

---

## 📅 Date Done

**Date**: *12/06/2025*  
**Time Taken**: *5 minutes*

---