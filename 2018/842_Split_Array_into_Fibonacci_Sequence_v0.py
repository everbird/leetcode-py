#!/usr/bin/env python
# encoding: utf-8

MAX_INT = 2**31-1


class Solution(object):

    def splitIntoFibonacci(self, S):
        len_n = len(S)
        max_split = len_n // 2
        for i in range(max_split):
            first_str = S[:i+1]
            if first_str != '0' and first_str.startswith('0'):
                return []

            result = []
            if verify(first_str, S[i+1:], result):
                return result
        return []


def verify(first_str, S, result, selected=None):
    first_int = int(first_str)
    len_n = len(S)
    max_split = len_n // 2

    def _do_verify(second_str):
        second_int = int(second_str)
        if second_str != '0' and second_str.startswith('0'):
            return False
        if first_int > MAX_INT or second_int > MAX_INT:
            return False
        next_int = first_int + second_int
        if next_int > MAX_INT:
            return False
        next_str = str(next_int)
        rest_S = S[len(second_str):]
        if rest_S == next_str:
            result.append(first_int)
            result.append(second_int)
            result.append(next_int)
            return True
        elif rest_S.startswith(next_str):
            result.append(first_int)
            if verify(second_str, rest_S, result, selected=next_str):
                return True

    if selected:
        return _do_verify(selected)

    for i in range(max_split):
        _second_str = S[:i+1]
        r = _do_verify(_second_str)
        if r is not None:
            return r

    return False


def main():
    s = Solution()
    tests = [
        (
            "123456579",
            [123,456,579]
        ),
        (
            "11235813",
            [1,1,2,3,5,8,13]
        ),
        (
            "112358130",
            []
        ),
        (
            "0123",
            []
        ),
        (
            "1101111",
            [110, 1, 111]
        ),
        (
            "11235813",
            [1,1,2,3,5,8,13]
        ),
        (
            "1011",
            [1,0,1,1]
        ),
        (
            "0000",
            [0,0,0,0]
        ),
        (
            "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511",
            []
        ),
        (
            "3611537383985343591834441270352104793375145479938855071433500231900737525076071514982402115895535257195564161509167334647108949738176284385285234123461518508746752631120827113919550237703163294909",
            []
        ),
    ]
    for input_args, expected in tests:
        r = s.splitIntoFibonacci(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)


if __name__ == '__main__':
    main()
