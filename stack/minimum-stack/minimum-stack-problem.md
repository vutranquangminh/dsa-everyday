🧮 Minimum Stack - Easy
Design a stack that supports retrieving the minimum element in constant time along with standard stack operations.

📌 Problem Statement
Title: Minimum Stack (MinStack)

Problem Description:
Design a class MinStack that supports all the following operations in constant time O(1):

MinStack() – Initializes the stack object.

void push(int val) – Pushes the element val onto the stack.

void pop() – Removes the element on the top of the stack.

int top() – Gets the top element of the stack.

int getMin() – Retrieves the minimum element in the stack.

Note: All operations must run in constant time. Each method should be efficient and scalable.

Example 1:
Input:

python
Copy
Edit
["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
Output:

python
Copy
Edit
[None, None, None, None, 0, None, 2, 1]
Explanation:

python
Copy
Edit
MinStack minStack = new MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
minStack.getMin() ➝ 0
minStack.pop()
minStack.top() ➝ 2
minStack.getMin() ➝ 1
✅ Recommended Time & Space Complexity
Time Complexity: O(1) for all operations

Space Complexity: O(n), where n is the maximum number of elements stored

📎 Constraints
-2^31 <= val <= 2^31 - 1

pop, top, and getMin are always called on non-empty stacks

💡 Hints
A brute-force approach would make getMin() an O(n) operation. Can we improve that?

Consider maintaining another stack to track the minimum element at each step.

When pushing, store the minimum so far in the auxiliary stack. When popping, remove from both stacks.

📅 Date Done
Date: *12/06/2025*
Time Taken: *30 minutes*