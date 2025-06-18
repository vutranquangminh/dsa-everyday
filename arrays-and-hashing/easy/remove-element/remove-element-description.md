# 🧮 Remove Element - Easy

---

## 📌 Problem Statement

You're given an integer array `nums` and an integer `val`.  
Remove **all occurrences** of `val` in-place in the array.

The **order of the remaining elements does not matter**, and the remaining part of the array beyond the new length `k` can be ignored.

You must:
1. Modify `nums` in-place so that the **first `k` elements** contain the elements not equal to `val`.
2. Return `k` — the number of elements not equal to `val`.

> The judge will test your implementation with:
```java
int[] nums = [...];
int val = ...;
int[] expectedNums = [...];

int k = removeElement(nums, val);
sort(nums, 0, k);
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

---

## 💡 Examples

### Example 1
**Input**:  
```python
nums = [3, 2, 2, 3], val = 3
```
**Output**:  
```python
2, nums = [2, 2, _, _]
```

**Explanation**:  
You return `k = 2`, and the first two elements should be `2`.  
Anything after index 1 can be ignored.

---

### Example 2
**Input**:  
```python
nums = [0,1,2,2,3,0,4,2], val = 2
```
**Output**:  
```python
5, nums = [0,1,4,0,3,_,_,_]
```

**Explanation**:  
You return `k = 5`.  
The first five elements can be in any order, but must not include `2`.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `0 <= nums.length <= 100`  
- `0 <= nums[i] <= 50`  
- `0 <= val <= 100`

---

## 💡 Hints

- Use a pointer to track the position of the next valid value.
- Overwrite the values equal to `val`.

---

## 📅 Date Done

**Date**: *18/06/2025*  
**Time Taken**: *10 minutes*
