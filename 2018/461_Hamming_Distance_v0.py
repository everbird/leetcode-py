class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        r = x^y
        cnt = 0
        while r:
            if r % 2:
                cnt += 1
            r = r>>1
        return cnt
