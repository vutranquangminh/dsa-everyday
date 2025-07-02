# 🧮 Bill Division - Easy

---

## 📌 Problem Statement

Two friends **Anna** and **Brian** are splitting the bill for dinner. However, Anna didn’t eat one of the items. Brian is supposed to fairly split the cost by excluding the item Anna didn’t eat. Your task is to determine whether Brian correctly calculated Anna’s share.

If he overcharged Anna, you must print the amount he owes her. Otherwise, print `"Bon Appetit"`.

---

## 💡 Examples

### Example 1

**Input:**
```
4 1
3 10 2 9
12
```

**Output:**
```
5
```

**Explanation:**

Anna didn’t eat the item at index 1 (which costs 10).  
Total of shared items = 3 + 2 + 9 = 14  
Split evenly: 14 / 2 = 7  
Brian charged 12 → Overcharge = 12 - 7 = **5**

---

### Example 2

**Input:**
```
4 1
3 10 2 9
7
```

**Output:**
```
Bon Appetit
```

**Explanation:**

Total of shared items = 3 + 2 + 9 = 14  
Split evenly = 7  
Brian charged 7 → Correct split → Print `"Bon Appetit"`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

---

## 📎 Constraints

- 2 ≤ n ≤ 10⁵  
- 0 ≤ k < n  
- 0 ≤ bill[i] ≤ 10⁴  
- The amount due will always be an integer

---

## 💡 Hints

- Exclude the item Anna didn’t eat from the total sum
- Divide the rest by 2 to get her fair share
- Compare this to the amount Brian charged

---

## 📅 Date Done

**Date**: *16/06/2025*  
**Time Taken**: *5 minutes*

---
