# 🧮 Top K Frequent Elements - Medium

This is my solution to the **"Top K Frequent Elements"** problem, which returns the `k` most frequent elements from a given integer array.

---

## 📌 Problem Statement

**Title**: Top K Frequent Elements

**Problem Description**:  
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements in the array.

The test cases are generated such that the answer is always unique.

### Example 1:
**Input**:  
`nums = [1,2,2,3,3,3], k = 2`

**Output**:  
`[2, 3]`

### Example 2:
**Input**:  
`nums = [7,7], k = 1`

**Output**:  
`[7]`

### Constraints:
- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`
- `1 <= k <= number of distinct elements in nums`

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity**: `O(n)`, where `n` is the size of the input array. This accounts for counting frequencies and sorting the elements.
- **Space Complexity**: `O(n)`, where `n` is the size of the input array. Space is used for storing frequency counts.

---

## 📅 Date Done

**Date**: *31/05/2025*  
**Time Taken**: *180 minutes*
