#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# BigO: O(n)
# @lc code=start
from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return (self.q1.popleft())

    def top(self):
        return self.q1[0]

    def empty(self):
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

