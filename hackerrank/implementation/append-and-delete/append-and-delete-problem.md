# 🧮 Append and Delete – Easy

---

## 📌 Problem Statement

You're given two strings `s` (initial) and `t` (target), and an integer `k`. You can perform exactly `k` operations to convert `s` into `t`. You have only 2 operations allowed:

1. Append a lowercase letter to the end.
2. Delete the last character (even if the string is already empty).

Return `"Yes"` if it is possible to convert `s` into `t` using exactly `k` operations. Otherwise, return `"No"`.

---

## 💡 Examples with Explanation

### Example 1
**Input:**
```plaintext
hackerhappy
hackerrank
9
```

**Output:**
```plaintext
Yes
```

**Explanation:**
- Common prefix: `hacker`
- Need to delete: `happy` → 5 deletes
- Need to append: `rank` → 4 appends
- Total: `5 + 4 = 9` → ✅ Exactly `k` operations → Yes

---

### Example 2
**Input:**
```plaintext
aba
aba
7
```

**Output:**
```plaintext
Yes
```

**Explanation:**
- Strings are already equal → no actual changes needed
- But we still have 7 operations
- We can delete from an empty string repeatedly (wasting operations)
- ✅ So `Yes`

---

### Example 3
**Input:**
```plaintext
ashley
ash
2
```

**Output:**
```plaintext
No
```

**Explanation:**
- Common prefix: `ash`
- To go from `ashley` to `ash`, we need 3 deletes
- Only 2 operations allowed → ❌ Not enough → No

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** `O(min(len(s), len(t)))`  
- **Space Complexity:** `O(1)`

---

## 📎 Constraints

- `1 ≤ len(s), len(t) ≤ 100`
- `1 ≤ k ≤ 100`

---

## 💡 Hints

- Find the longest common prefix.
- Count how many characters you need to delete and how many to append.
- If you have leftover operations, check if they can be "wasted" as delete+append pairs or extra deletes on an empty string.

---

## 📅 Date Done

**Date:** *04/07/2025*  
**Time Taken:** *10 minutes*

---