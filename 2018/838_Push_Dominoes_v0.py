#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def pushDominoes(self, dominoes):
        _dominoes = list(dominoes)
        while self.run(_dominoes):
            # print _dominoes
            pass
        return ''.join(_dominoes)

    def run(self, dominoes):
        len_n = len(dominoes)
        i = 0
        modified = False
        pre_char = None
        while i < len_n:
            char = dominoes[i]
            if char == 'L':
                pre_char = char
                i += 1
                continue

            elif char == 'R':
                if i + 2 < len_n and dominoes[i+1] == '.' and dominoes[i+2] == 'L':
                    i += 3
                    pre_char = 'L'
                    continue

                pre_char = 'R'
                i += 1
                continue

            elif char == '.':
                if pre_char == 'R':
                    dominoes[i] = 'R'
                    modified = True
                    pre_char = char
                    i += 1
                    continue

                if i+1 < len_n and dominoes[i+1] == 'L':
                    dominoes[i] = 'L'
                    modified = True
                    pre_char = char
                    i += 1
                    continue

            pre_char = char
            i += 1

        return modified


def main():
    s = Solution()
    tests = [
        (
            ".L.R...LR..L..",
            "LL.RR.LLRRLL.."
        ),
    ]
    for input_args, expected in tests:
        r = s.pushDominoes(input_args)
        print 'Input:{}\tOutput:{}\tExpected:{}'.format(input_args, r, expected)


if __name__ == '__main__':
    main()
