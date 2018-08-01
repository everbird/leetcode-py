class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i, n in enumerate(nums):
            while n != nums[n-1]:
                x = nums[n-1]
                nums[n-1] = n
                nums[i] = x
                n = x

        r = []
        for i, n in enumerate(nums, 1):
            if n != i:
                r.append(i)

        return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [4,3,2,7,8,2,3,1],
            [5, 6]
        ),
    ]
    f = s.findDisappearedNumbers
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
