#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas):
            return -1

        tank = 0
        lenn = len(gas)
        start = 0
        for i in range(lenn):
            diff = gas[i] - cost[i]
            tank += diff
            if tank < 0:
                start = i+1
                tank = 0

        return start


if __name__ == '__main__':
    s = Solution()
    print s.canCompleteCircuit([2, 4, 3], [2, 3, 9])
    print s.canCompleteCircuit([2, 4, 3, 10], [2, 3, 8, 1])
    print s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
