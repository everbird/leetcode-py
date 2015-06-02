#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        ops = []
        for i in range(len(ratings)-1):
            a = ratings[i]
            b = ratings[i+1]
            if a > b:
                ops.append(-1)
            elif a < b:
                ops.append(1)
            else:
                ops.append(0)

        r = [1] * len(ratings)
        for i in range(len(ratings)):
            if r[i] == 1:
                j = i
                while j > 0:
                    if ops[j-1] == -1:
                        r[j-1] = max(r[j] + 1, r[j-1])
                    else:
                        break

                    j -= 1

                k = i
                while k < (len(ratings) - 1):
                    if ops[k] == 1:
                        r[k+1] = max(r[k] + 1, r[k+1])
                    else:
                        break

                    k += 1

        return sum(r)


if __name__ == '__main__':
    s = Solution()
    print s.candy([1,2,3,4])
    print s.candy([1,2,3,4,4])
    print s.candy([2,4,1])
