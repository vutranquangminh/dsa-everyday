# 🧮 Circular Array Rotation - Easy

---

## 📌 Problem Statement

John Watson teaches Sherlock an operation called **right circular rotation** on an array.  
A **single right rotation** means:
- The **last element** moves to the **front**, and
- All other elements shift **one position to the right**.

You're given:
- An array of integers `a`
- A number of rotations `k`
- An array of query indices `queries`

🔍 Your task:
- Perform the **`k` right rotations** on array `a`
- Return the value at each index given in `queries` after the rotations

---

## 💡 Examples

### Example 1

**Input:**
```python
a = [1, 2, 3]
k = 2
queries = [0, 1, 2]
```

**Output:**
```python
2
3
1
```

**Explanation:**  
Perform 2 right circular rotations:
- After 1st rotation: [3, 1, 2]  
- After 2nd rotation: [2, 3, 1]

Now answer the queries:
- `a[0]` → 2  
- `a[1]` → 3  
- `a[2]` → 1

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** `O(q)`  
- **Space Complexity:** `O(1)` (ignoring input/output storage)

---

## 📎 Constraints

- `1 <= n <= 10⁵` – Size of the array  
- `1 <= k <= 10⁵` – Number of rotations  
- `1 <= q <= 500` – Number of queries  
- `0 <= queries[i] < n` – Valid indices  

---

## 💡 Hints

- You don’t need to rotate the array literally.
- Think **modulo math**: use index mapping.
- Final index of an element originally at `i` is:  
  ```python
  (i + k) % n
  ```
- So, to find value at `query_index`, reverse the mapping:
  ```python
  rotated_index = (query_index - k + n) % n
  ```

---

## 📅 Date Done

**Date:** *30/06/2025*  
**Time Taken:** *5 minutes*

---