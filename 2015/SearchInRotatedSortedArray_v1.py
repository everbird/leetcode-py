#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        pivot = find_pivot(nums)

        r = binary_search(nums[:pivot], target)
        if r != -1:
            return r

        r = binary_search(nums[pivot:], target)
        return pivot + r if r != -1 else -1


# 返回最小元素的 index，注意这里不是最大元素
def find_pivot(nums):
    b = 0
    e = len(nums) - 1

    # 注意这里由于计算 mid 是取整靠近 b 的，所以为避免 mid = b
    # 造成的死循环，要mid 和 e 比较且 b 要有变化，所以比较用 e，处理用 b
    # 有变化的 nums[mid] > nums[e]
    # 而且也因此这里使用最小元素的 index 作为 pivot
    while b < e:
        mid = (b+e) // 2
        if nums[mid] > nums[e]:
            b = mid+1
        else:
            e = mid

    return b


def binary_search(nums, k):
    lenn = len(nums)
    b = 0
    e = lenn - 1
    while b <= e:
        mid = (e + b) // 2

        if k == nums[mid]:
            return mid
        elif k > nums[mid]:
            b = mid + 1
        else:
            e = mid - 1

    return -1


if __name__ == '__main__':
    s = Solution()
    a = [4,5,6,7,0,1,2,3]
    r = s.search(a, 6)
    print r

    a = [3,1]
    r = s.search(a, 1)
    #r = find_pivot(a)
    print r

    a = [1,]
    r = s.search(a, 1)
    print r

    a = [1,3]
    r = s.search(a, 3)
    print r

    a = [4,5,6,7,8,1,2,3]
    r = s.search(a, 8)
    print r
