#!/usr/bin/eni python
# encoding: utf-8



class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        pid = get_uuid(pattern)
        return [x for x in words if get_uuid(x) == pid]


def get_uuid(w):
    uuid = []
    new_char_id = 0
    m = {}
    for i, c in enumerate(w):
        if c not in m:
            m[c] = new_char_id
            uuid.append(new_char_id)
            new_char_id += 1
        else:
            uuid.append(m[c])

    return tuple(uuid)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                ["abc","deq","mee","aqq","dkd","ccc"],
                "abb"
            ),
            ["mee", "aqq"]
        ),
    ]
    f = s.findAndReplacePattern
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
