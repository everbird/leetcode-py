#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        lenw = len(words)
        lens = map(len, words)
        if maxWidth < max(lens):
            return []

        p = 0
        pre = 0
        r = []
        while p <= lenw - 1:

            cnt = -1
            while cnt + lens[p] + 1 <= maxWidth:
                cnt += 1
                cnt += lens[p]
                p += 1
                if p >= lenw:
                    break

            line = words[pre:min(p, lenw)]
            pos = len(line) - 1
            spaces = maxWidth - sum(map(len, line))
            new_line = ''

            if p >= lenw:
                for w in line:
                    new_line += w
                    if spaces:
                        new_line += ' '
                        spaces -= 1

                if spaces:
                    new_line += ' ' * spaces
            else:
                threshold = spaces % pos if pos else 0
                s_cnt = spaces // pos if pos else spaces

                for i, w in enumerate(line):
                    new_line += w
                    if spaces:
                        t = min(spaces, s_cnt)
                        new_line += ' ' * t
                        spaces -= t

                    if i < threshold and spaces:
                        new_line += ' '
                        spaces -= 1

            r.append(new_line)

            pre = p

        return r


if __name__ == '__main__':
    s = Solution()
    print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    #print s.fullJustify(["a","b","c","d","e"], 3)
    #print s.fullJustify(["What","must","be","shall","be."], 12)
