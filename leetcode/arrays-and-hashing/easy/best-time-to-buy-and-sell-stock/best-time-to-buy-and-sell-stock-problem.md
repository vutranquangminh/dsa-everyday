
# 🧮 Best Time to Buy and Sell Stock - Easy

---

## 📌 Problem Statement

You are given an integer array `prices` where `prices[i]` represents the price of a given stock on the `i`th day.

Your goal is to **maximize your profit** by choosing a **single day to buy** one stock and a **different day in the future to sell** that stock.

Return the **maximum profit** you can achieve from this transaction.  
If no profit can be made, return `0`.

---

## 💡 Examples

### Example 1

**Input**:
```python
prices = [7,1,5,3,6,4]
```

**Output**:
```python
5
```

**Explanation**:  
Buy on day 2 (`price = 1`) and sell on day 5 (`price = 6`) → `profit = 6 - 1 = 5`

---

### Example 2

**Input**:
```python
prices = [7,6,4,3,1]
```

**Output**:
```python
0
```

**Explanation**:  
No profitable transaction is possible, so return `0`.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 <= prices.length <= 10⁵`
- `0 <= prices[i] <= 10⁴`

---

## 💡 Hints

- Keep track of the **minimum price** encountered so far while iterating.
- At each step, calculate the **potential profit** if selling today.
- Update the maximum profit accordingly.

---

## 📅 Date Done

**Date**: *25/06/2025*  
**Time Taken**: *30 minutes*

---