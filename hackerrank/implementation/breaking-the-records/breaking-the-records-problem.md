
# 🧮 Breaking the Records - Easy

---

## 📌 Problem Statement

Maria is a basketball player who wants to go pro. She tracks her points scored in each game during a season. Her **first game's score sets both her season high and low records**, and from there, she tracks:

- Each time she **breaks her record for most points**.
- Each time she **breaks her record for least points**.

Your task is to return the number of times she **breaks her high and low records** during the season.

---

## 💡 Examples

### Example 1

**Input:**
```python
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
```

**Output:**
```text
2 4
```

**Explanation:**
- High score broken at: game 2 (20), game 7 (25) → 2 times  
- Low score broken at: game 1 (5), game 4 (4), game 6 (2), game 8 (1) → 4 times

---

### Example 2

**Input:**
```python
scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
```

**Output:**
```text
4 0
```

**Explanation:**
- High score broken at: games 1, 2, 3, 9 → 4 times  
- Low score never broken → 0 times

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 <= n <= 1000`
- `0 <= scores[i] <= 10^8`

---

## 💡 Hints

- Track current `min_score` and `max_score` as you iterate.
- Increment counters when Maria scores a new personal best or worst.

---

## ✅ Python Implementation

```python
def breakingRecords(scores):
    min_score = max_score = scores[0]
    min_breaks = max_breaks = 0

    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_breaks += 1
        elif score < min_score:
            min_score = score
            min_breaks += 1

    return [max_breaks, min_breaks]
```

---

## 📅 Date Done

**Date**: *11/06/2025*  
**Time Taken**: *5 minutes*

---