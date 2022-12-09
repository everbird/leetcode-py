#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = -float("inf")
        held = -float("inf")
        cooldown = 0

        for p in prices:
            pre_cd = cooldown
            cooldown = max(cooldown, sold)
            sold = held + p
            held = max(held, pre_cd-p)

        return max(sold, cooldown)


# State Machine
