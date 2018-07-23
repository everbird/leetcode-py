#!/usr/bin/eni python
# encoding: utf-8



class Solution(object):
    def circularArrayLoop(self, nums):
        if not nums:
            return False

        n  = len(nums)
        self.locs = set(range(n))
        while self.locs:
            start_index = self.locs.pop()
            if self.check(nums, start_index):
                return True

        return False


    def check(self, nums, start_index):
        n = len(nums)
        a = (start_index + nums[start_index]) % n
        b = start_index
        if a in self.locs:
            self.locs.remove(a)
        if a == b:
            return False

        while a != b:
            _a = a
            a = (a + nums[a]) % n
            if a in self.locs:
                self.locs.remove(a)
            if a == _a:
                return False
            a = (a + nums[a]) % n
            if a in self.locs:
                self.locs.remove(a)
            b = (b + nums[b]) % n

        direction = nums[a] > 0
        a = (a + nums[a]) % n
        while a != b:
            x = nums[a]
            if (x > 0 or direction) and not (x > 0 and direction):
                return False
            a = (a + x) % n

        return True


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [2, -1, 1, 2, 2],
            True
        ),
        (
            [-1, 2],
            False
        ),
        (
            [-2, 1, -1, -2, -2],  # forward-backward loop
            False
        ),
        (
            [3,1,2],
            True
        )
    ]
    f = s.circularArrayLoop
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
