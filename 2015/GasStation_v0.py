#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        lenn = len(gas)
        r = [i for i in range(lenn) if self.can_start(gas, cost, i)]
        return r or -1

    def can_start(self, gas, cost, index):
        tank = 0
        _gas = gas[index:] + gas[:index:-1]
        _cost = cost[index:] + cost[:index:-1]
        for g, c in zip(_gas, _cost):
            tank += g - c
            if tank < 0:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print s.canCompleteCircuit([2, 4, 3], [2, 3, 9])
    print s.canCompleteCircuit([2, 4, 3], [2, 3, 4])
    print s.canCompleteCircuit([2, 4, 3, 10], [2, 3, 8, 1])
