#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def toGoatLatin(self, S):
        words = S.split()
        r = []
        for i, w in enumerate(words, 1):
            if w[0].lower() in ('a', 'e', 'i', 'o', 'u'):
                w += 'ma'
            else:
                if len(w) > 1:
                    w = w[1:] + w[0]
                w += 'ma'
            w += 'a'*i

            r.append(w)

        return ' '.join(r)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            "I speak Goat Latin",
            "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
        ),
        (
            "The quick brown fox jumped over the lazy dog",
            "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
        ),
    ]
    f = s.toGoatLatin
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
