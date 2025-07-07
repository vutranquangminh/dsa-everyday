
# 🧮 Save the Prisoner! - Easy

---

## 📌 Problem Statement

A jail has `n` prisoners seated in a circle and `m` sweets to distribute. The distribution starts at prisoner in seat `s`, and continues sequentially around the table. Each prisoner receives one sweet at a time.  
However, the **last sweet is unpleasant**, and we must determine **which prisoner will receive it**.

Return the **chair number** of the prisoner who receives the bad sweet.

---

## 💡 Examples

### Example 1

**Input**:
```python
n = 5, m = 2, s = 1
```

**Output**:
```python
2
```

**Explanation**:  
Sweets go to prisoners: seat 1 → seat 2  
So prisoner at **seat 2** gets the bad sweet.

---

### Example 2

**Input**:
```python
n = 5, m = 2, s = 2
```

**Output**:
```python
3
```

**Explanation**:  
Sweets go to: seat 2 → seat 3  
So prisoner at **seat 3** gets the bad sweet.

---

### Example 3

**Input**:
```python
n = 7, m = 19, s = 2
```

**Output**:
```python
6
```

**Explanation**:  
Sweets go around multiple times. The last sweet lands at seat 6.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(1)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 <= n <= 10⁹` – Number of prisoners  
- `1 <= m <= 10⁹` – Number of sweets  
- `1 <= s <= n` – Starting chair position

---

## 💡 Hints

- Use **modulo arithmetic** to simulate the circular structure.
- Watch out for **off-by-one errors**.
- If `(s + m - 1) % n == 0`, return `n`.

---

## 🧠 Formula Used

To calculate the final position:
```python
last = (s + m - 1) % n
return last if last != 0 else n
```

---

## 🧪 Sample Code (Python)

```python
def saveThePrisoner(n, m, s):
    last = (s + m - 1) % n
    return last if last != 0 else n
```

---

## 📅 Date Done

**Date**: *29/06/2025*  
**Time Taken**: *5 minutes*

---
