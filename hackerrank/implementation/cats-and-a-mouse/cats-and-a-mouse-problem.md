# 🧮 Cat and Mouse - Easy

---

## 📌 Problem Statement

Two cats (Cat A and Cat B) and one mouse (Mouse C) are placed at different positions on a number line.

Your task is to determine **which cat reaches the mouse first**, assuming:
- The mouse **does not move**
- Both cats move at the **same speed**

### Rules:
- If **Cat A** is closer to the mouse → return `'Cat A'`
- If **Cat B** is closer to the mouse → return `'Cat B'`
- If **both cats are equally distant**, the mouse escapes while they fight → return `'Mouse C'`

---

## 💡 Examples

### Example 1

**Input:**
```
2
1 2 3
1 3 2
```

**Output:**
```
Cat B
Mouse C
```

**Explanation:**

- **Query 1**:
  - Cat A at 1, Cat B at 2, Mouse C at 3
  - Distance(A → C): |1 - 3| = 2  
  - Distance(B → C): |2 - 3| = 1  
  ✅ Cat B is closer → return `Cat B`

- **Query 2**:
  - Cat A at 1, Cat B at 3, Mouse C at 2
  - Distance(A → C): |1 - 2| = 1  
  - Distance(B → C): |3 - 2| = 1  
  ✅ Equal distance → return `Mouse C`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(q)  
- **Space Complexity**: O(1)

---

## 📎 Constraints

- 1 ≤ q ≤ 100  
- 1 ≤ x, y, z ≤ 100

---

## 💡 Hints

- Use `abs(x - z)` and `abs(y - z)` to calculate distances.
- Compare the values to decide the result.

---

## 📅 Date Done

**Date**: *21/06/2025*  
**Time Taken**: *5 minutes*

---
