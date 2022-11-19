#!/usr/bin/env python3

class Solution(object):
    def countSmaller(self, nums):
        lenn = len(nums)
        num_to_index = [(v, i) for i, v in enumerate(nums)]
        rs = [0] * lenn

        def merge_sort(s, e):
            if s + 1 >= e:
                return

            m = (s - e) // 2 + e
            merge_sort(s, m)
            merge_sort(m, e)
            merge(s, e, m)

        def merge(s, e, m):
            l = s
            r = m
            tmp = []
            while l < m and r < e:
                if num_to_index[l][0] <= num_to_index[r][0]:
                    rs[num_to_index[l][1]] += r - m
                    tmp.append(num_to_index[l])
                    l += 1
                else:
                    tmp.append(num_to_index[r])
                    r += 1

            while l < m:
                rs[num_to_index[l][1]] += r - m
                tmp.append(num_to_index[l])
                l += 1

            while r < e:
                tmp.append(num_to_index[r])
                r += 1

            for i in range(s, e):
                num_to_index[i] = tmp[i - s]

        merge_sort(0, lenn)

        return rs
