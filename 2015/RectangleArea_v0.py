#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        top = min(D, H)
        bottom = max(B, F)
        left = max(A, E)
        right = min(C, G)
        overlap = (right - left) * (top - bottom) if top > bottom and right > left else 0
        a1 = (C - A) * (D - B)
        a2 = (G - E) * (H - F)
        return a1 + a2 - overlap


if __name__ == '__main__':
    s = Solution()
    print s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
    print s.computeArea(0, 0, 0, 0, -1, -1, 1, 1)
    print s.computeArea(-2, -2, 2, 2, 3, 3, 4, 4)
