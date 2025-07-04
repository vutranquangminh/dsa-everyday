# 🧮 Designer PDF Viewer - Easy

---

## 📌 Problem Statement

When a contiguous block of text is selected in a PDF viewer, the selection is highlighted using **independent blue rectangles** for each character.

Each letter of the alphabet has a specific **height**.  
Given a string (word), determine the **highlighted area** when the word is selected.

👉 Each character has a **width of 1 unit**, and the **height depends** on the tallest letter in the word.

---

## 💡 Examples

### Example 1

**Input:**
```
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc
```

**Output:**
```
9
```

**Explanation:**
- Heights of `a`, `b`, `c` → [1, 3, 1]
- Tallest letter is `b` → height = 3  
- Word length = 3 → area = 3 × 3 = **9**

---

### Example 2

**Input:**
```
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba
```

**Output:**
```
28
```

**Explanation:**
- Heights of `z`, `a`, `b`, `a` → [7, 1, 3, 1]
- Tallest letter is `z` → height = 7  
- Word length = 4 → area = 7 × 4 = **28**

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(n), where n is the length of the word  
- **Space Complexity**: O(1)

---

## 📎 Constraints

- `h.length = 26` (one height per lowercase letter)
- `1 ≤ h[i] ≤ 7`
- `1 ≤ len(word) ≤ 10`  
- `word` only contains lowercase English letters

---

## 💡 Hints

- Use `ord(char) - ord('a')` to map a character to its corresponding height index.
- Find the **maximum height** in the word and multiply it by **word length**.

---

## 📅 Date Done

**Date**: *24/06/2025*  
**Time Taken**: *5 minutes*

---