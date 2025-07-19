# 🧮 Equalize Array - Easy

---

## 📌 Problem Statement

Given an array of integers, determine the **minimum number of elements** to delete to leave only elements of equal value.

### **Example**

**Input:**
```
5
3 3 2 1 3
```

**Output:**
```
2
```

**Explanation:**  
Delete the **1** and **2** to leave `[3, 3, 3]`. This is the minimal number of deletions.  
The only other option is to delete **3** elements to get an array of either `[1, 1]` or `[2, 2]`. Thus, the minimum number of deletions is **2**.

---

## 💡 Approach

1. **Count the occurrences** of each element in the array.
2. **Identify the most frequent element**.
3. **Delete all other elements** to leave only the most frequent one.
4. The number of deletions is equal to the total length of the array minus the number of occurrences of the most frequent element.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(n)  
- **Space Complexity**: O(n)

---

## 📎 Constraints

- **2 ≤ n ≤ 100**
- The array can contain any integers.

---

## 📅 Date Done

**Date**: *10/07/2025*  
**Time Taken**: *5 minutes*  

---