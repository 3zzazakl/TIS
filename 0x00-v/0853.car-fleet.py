#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#
# BigO = O(nlogn)
# @lc code=start
class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        arrival = []

        for position, speed in cars:
            targeted_time = (target - position) / speed

            if not arrival or targeted_time > arrival[-1]:
                arrival.append(targeted_time)
                fleets += 1
        return (fleets)

# @lc code=end
