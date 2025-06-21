# 🧮 Minimum Index Sum of Two Lists - Easy

---

## 📌 Problem Statement

You are given two **lists of unique strings**, `list1` and `list2`. A **common string** is one that appears in **both lists**.

You need to find all common strings with the **least index sum** — that is, for a common string at index `i` in `list1` and `j` in `list2`, the value of `i + j` should be minimized.

Return all such common strings. The result can be in **any order**.

---

## 💡 Examples

### Example 1
**Input**:
```python
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
```

**Output**:
```python
["Shogun"]
```

**Explanation**: The only common string is `"Shogun"` with index sum `0 + 3 = 3`.

---

### Example 2
**Input**:
```python
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
```

**Output**:
```python
["Shogun"]
```

**Explanation**: `"Shogun"` has the least index sum: `0 + 1 = 1`.

---

### Example 3
**Input**:
```python
list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
```

**Output**:
```python
["sad","happy"]
```

**Explanation**:  
- `"happy"` → `0 + 1 = 1`  
- `"sad"` → `1 + 0 = 1`  
- `"good"` → `2 + 2 = 4`  
→ `"sad"` and `"happy"` share the **minimum index sum** of `1`.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n + m)`  
- **Space Complexity**: `O(n)`  

(where `n` and `m` are the lengths of `list1` and `list2`)

---

## 📎 Constraints

- `1 <= list1.length, list2.length <= 1000`  
- `1 <= list1[i].length, list2[i].length <= 30`  
- Strings contain **letters** and **spaces** only  
- All strings in `list1` and `list2` are **unique**  
- There is **at least one common string**

---

## 💡 Hints

- Use a **dictionary** to store indices of strings in `list1`
- While looping through `list2`, check if the string exists in the dictionary  
- Keep track of the **minimum index sum** found and update results accordingly

---

## 📅 Date Done

**Date**: *20/06/2025*  
**Time Taken**: *30 minutes*

---