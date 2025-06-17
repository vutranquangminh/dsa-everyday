# 🧮 Remove Duplicates from Sorted Array - Easy

---

## 📌 Problem Statement

You're given an integer array `nums` sorted in **non-decreasing** order.  
Your task is to **remove duplicates in-place** such that each unique element appears only once.  
Return the number of unique elements `k`, and **modify** `nums` in-place such that the **first `k` elements** contain the unique values in original order.

> The remaining elements of `nums` beyond index `k-1` do **not matter**.

A custom judge will validate your solution using:
```java
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

---

## 💡 Examples

### Example 1
**Input**:  
```python
nums = [1,1,2]
```

**Output**:  
```python
2, nums = [1,2,_]
```

**Explanation**:  
The function should return `k = 2`, with the first two elements being `[1, 2]`.  
The values beyond `k` are ignored.

---

### Example 2
**Input**:  
```python
nums = [0,0,1,1,1,2,2,3,3,4]
```

**Output**:  
```python
5, nums = [0,1,2,3,4,_,_,_,_,_]
```

**Explanation**:  
The function should return `k = 5`, and the first 5 elements of `nums` should be `[0,1,2,3,4]`.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

---

## 📎 Constraints

- `1 <= nums.length <= 30,000`  
- `-100 <= nums[i] <= 100`  
- `nums` is sorted in **non-decreasing** order.

---

## 💡 Hints

- Use a **two-pointer** technique to overwrite duplicates.
- Compare each element with the previous unique one.

---

## 📅 Date Done

**Date**: *17/06/2025*  
**Time Taken**: *15 minutes*

---
