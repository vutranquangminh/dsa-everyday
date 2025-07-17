# 🧮 Jumping on the Clouds - Easy

---

## 📌 Problem Statement

There is a new mobile game with a sequence of clouds numbered consecutively.  
Each cloud is either:
- **`0`**: a safe **cumulus** cloud
- **`1`**: a dangerous **thunderhead**

The player starts at the first cloud and must reach the last one by jumping:
- **1 or 2 clouds** at a time
- Only onto cumulus clouds (`0`), avoiding thunderheads (`1`)

Determine the **minimum number of jumps** required to win.  
It is always guaranteed that a path to the last cloud exists.

---

## 💡 Examples

### Example 1

**Input:**
```
7
0 0 1 0 0 1 0
```

**Output:**
```
4
```

**Explanation:**  
The player must avoid thunderheads at positions `2` and `5`.  
Possible path:  
```
Index:    0 → 1 → 3 → 4 → 6
Clouds:   0    0    0    0    0
```
Number of jumps: **4**

---

### Example 2

**Input:**
```
6
0 0 0 0 1 0
```

**Output:**
```
3
```

**Explanation:**  
Only thunderhead is at index `4`.  
Best path:  
```
Index:    0 → 2 → 3 → 5
Clouds:   0    0    0    0
```
Number of jumps: **3**

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(n)  
- **Space Complexity**: O(1)

---

## 📎 Constraints

- `2 ≤ n ≤ 100`
- `c[i] ∈ {0, 1}`
- `c[0] = c[n - 1] = 0` (always start and end on safe clouds)

---

## 💡 Hints

- Greedily jump **2 clouds** if possible; if not, jump **1 cloud**
- Use a loop to simulate the jumps and count them
- You never need to jump onto a `1`

---

## 📅 Date Done

**Date**: *09/07/2025*  
**Time Taken**: *5 minutes*

---