# 🧮 Taum and B'day – Easy

---

## 📌 Problem Statement

Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum:

- 🖤 **Black gifts**
- 🤍 **White gifts**

To make her happy, Taum has to buy `b` black gifts and `w` white gifts.

Each gift has the following costs:
- Cost of each black gift: `bc`
- Cost of each white gift: `wc`
- Cost to convert one gift color to the other (black ⇄ white): `z`

🎯 **Goal:** Determine the **minimum cost** to purchase the required gifts.

---

## 💡 Examples

### 🔹 Example 1

**Input:**
```
5
10 10
1 1 1
5 9
2 3 4
3 6
9 1 1
7 7
4 2 1
3 3
1 9 2
```

**Output:**
```
20
37
12
35
12
```

**Explanation:**

- **Test Case 1:**
  ```
  b = 10, w = 10
  bc = 1, wc = 1, z = 1
  Since bc == wc, no need to convert.
  Total = 10*1 + 10*1 = 20
  ```

- **Test Case 2:**
  ```
  b = 5, w = 9
  bc = 2, wc = 3, z = 4
  No cheaper conversion → Total = 5*2 + 9*3 = 10 + 27 = 37
  ```

- **Test Case 3:**
  ```
  b = 3, w = 6
  bc = 9, wc = 1, z = 1
  Convert white to black → cost per black = 1+1 = 2 < 9
  Total = 3*(1+1) + 6*1 = 6 + 6 = 12
  ```

- **Test Case 4:**
  ```
  b = 7, w = 7
  bc = 4, wc = 2, z = 1
  Convert white to black → cost per black = 2+1 = 3 < 4
  Total = 7*(2+1) + 7*2 = 21 + 14 = 35
  ```

- **Test Case 5:**
  ```
  b = 3, w = 3
  bc = 1, wc = 9, z = 2
  Convert black to white → cost per white = 1+2 = 3 < 9
  Total = 3*1 + 3*(1+2) = 3 + 9 = 12
  ```

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** O(1) per test case  
- **Space Complexity:** O(1)

---

## 📎 Constraints

- `1 ≤ t ≤ 10` – Number of test cases  
- `1 ≤ b, w ≤ 10^9` – Number of black and white gifts  
- `1 ≤ bc, wc, z ≤ 10^9` – Cost parameters

---

## 💡 Hints

- Always compute:
  - `min(bc, wc + z)` → best way to buy black
  - `min(wc, bc + z)` → best way to buy white
- Multiply each by `b` or `w` respectively and sum to get the total cost.
- Be mindful of integer overflows with large values!

---

## 📅 Date Done

**Date:** *12/07/2025*  
**Time Taken:** *12 minutes*

---