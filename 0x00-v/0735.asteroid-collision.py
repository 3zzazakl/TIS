#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#
# BigO = O(n)
# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for aster in asteroids:
            while stack and aster < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(aster):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(aster):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(aster)
        return stack
# @lc code=end

