'''
Problem Statement:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
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
 
Constraints:
Methods pop, top and getMin operations will always be called on non-empty stacks.
'''
# Solution:
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.item = []
        self.length = 0
        self.minimum = []
        self.minlen =0
        

    def push(self, x: int) -> None:
        self.item.append(x)
        self.length += 1
        if self.minlen == 0:
            self.minimum.append(x)
            self.minlen += 1
        else:
            if self.minimum[self.minlen -1] >= x:
                self.minimum.append(x)
                self.minlen += 1
        

    def pop(self) -> None:
        temp = self.item.pop()
        self.length -= 1
        if self.minimum[self.minlen - 1] == temp:
            self.minimum.pop()
            self.minlen -= 1
        

    def top(self) -> int:
        return self.item[self.length -1]
        
        
    def getMin(self) -> int:
        return self.minimum[self.minlen -1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
