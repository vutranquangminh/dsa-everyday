# 🧮 Day of the Programmer - Easy

---

## 📌 Problem Statement

Marie invented a Time Machine and wants to visit **Russia** on the **256th day of a given year** between **1700 and 2700**, inclusive.

Russia used:
- The **Julian calendar** from **1700 to 1917**.
- The **Gregorian calendar** from **1919 onwards**.
- In **1918**, due to the calendar shift, **February 14th** was the **32nd** day of the year.

### Leap Year Rules:

- **Julian calendar**: Leap year if year % 4 == 0  
- **Gregorian calendar**: Leap year if:
  - year % 400 == 0 **or**
  - year % 4 == 0 **and** year % 100 != 0

Your task is to determine the **date of the 256th day** of the given year in the format `dd.mm.yyyy`.

---

## 💡 Examples

### Example 1

**Input:**
```
2017
```

**Output:**
```
13.09.2017
```

**Explanation:**

In a common year:
```
Jan to Aug = 243 days → 256 - 243 = 13 → 13.09.2017
```

---

### Example 2

**Input:**
```
2016
```

**Output:**
```
12.09.2016
```

**Explanation:**

In a **leap year**, February has 29 days:
```
Jan to Aug = 244 days → 256 - 244 = 12 → 12.09.2016
```

---

### Example 3

**Input:**
```
1800
```

**Output:**
```
12.09.1800
```

**Explanation:**

1800 is a leap year under the **Julian calendar** → 12.09.1800

---

### Example 4

**Input:**
```
1918
```

**Output:**
```
26.09.1918
```

**Explanation:**

In 1918, due to the calendar switch, **13 days were skipped** in February. So:
```
Jan + Feb (only 15 days) + Mar...Aug = 31 + 15 + ... = 230 days
→ 256 - 230 = 26 → 26.09.1918
```

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

---

## 📎 Constraints

- 1700 ≤ year ≤ 2700

---

## 💡 Hints

- Use conditionals to check which calendar system the year belongs to.
- Handle 1918 as a **special case**.

---

## 📅 Date Done

**Date**: *15/06/2025*  
**Time Taken**: *7 minutes*

---