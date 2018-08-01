from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        len_p = len(p)
        pc = Counter(p)
        sc = Counter(s[:len_p])
        r = []
        if counter_equals(sc, pc):
            r.append(0)
        for i, ch in enumerate(s[len_p:], len_p):
            sc[ch] += 1
            pre_ch = s[i-len_p]
            sc[pre_ch] -= 1
            if counter_equals(sc, pc):
                r.append(i-len_p+1)

        return r

def counter_equals(a, b):
    return all([a[k] == b[k] for k in b])


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                'cbaebabacd',
                'abc'
            ),
            [0, 6]
        ),
        (
            (
                'abab',
                'ab'
            ),
            [0, 1, 2]
        ),
    ]
    f = s.findAnagrams
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
