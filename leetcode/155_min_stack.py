#!/usr/bin/env python
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.



Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack = [val, *self.stack]
        if not self.min_stack or self.min_stack[0] >= val:
            self.min_stack = [val, *self.min_stack]

    def pop(self) -> None:
        val = self.stack[0]
        self.stack = self.stack[1:]
        if val == self.min_stack[0]:
            self.min_stack = self.min_stack[1:]

        return val

    def top(self) -> int:
        top_val = self.stack[0]
        print(top_val)
        return top_val

    def getMin(self) -> int:
        min_val = self.min_stack[0]
        print(min_val)
        return min_val


class MinStack2:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack = [val, *self.stack]

    def pop(self) -> None:
        val = self.stack[0]
        self.stack = self.stack[1:]

        return val

    def top(self) -> int:
        top_val = self.stack[0]
        print(top_val)
        return top_val

    def getMin(self) -> int:
        print(min(self.stack))
        return min(self.stack)


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin() # return -3
    minStack.pop()
    minStack.top()    # return 0
    minStack.getMin() # return -2
