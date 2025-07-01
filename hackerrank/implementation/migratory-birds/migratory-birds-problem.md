# 🧮 Migratory Birds - Easy

---

## 📌 Problem Statement

You are given an array of bird sightings, where each element represents a **bird type ID**. Your task is to determine the **ID of the most frequently sighted bird type**.

If there are multiple types with the same highest frequency, return the **smallest bird type ID** among them.

---

## 💡 Examples

### Example 1

**Input:**
```python
arr = [1, 4, 4, 4, 5, 3]
```

**Output:**
```
4
```

**Explanation:**

Bird sightings by type:
- Type 1: 1 bird
- Type 3: 1 bird
- Type 4: 3 birds
- Type 5: 1 bird

Type 4 has the highest frequency → return 4.

---

### Example 2

**Input:**
```python
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
```

**Output:**
```
3
```

**Explanation:**

Bird sightings by type:
- Type 1: 2 birds
- Type 2: 2 birds
- Type 3: 3 birds
- Type 4: 3 birds
- Type 5: 1 bird

Types 3 and 4 are tied with 3 sightings. Return the smaller ID → 3.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1) (bounded by number of bird types, i.e. 5)

---

## 📎 Constraints

- 5 ≤ n ≤ 2 × 10⁵
- Bird type IDs are guaranteed to be in `{1, 2, 3, 4, 5}`

---

## 💡 Hints

- Use a frequency array or dictionary to count the number of sightings per type.
- After counting, find the max frequency and its corresponding lowest ID.

---

## 📅 Date Done

**Date**: *14/06/2025*  
**Time Taken**: *5 minutes*

---