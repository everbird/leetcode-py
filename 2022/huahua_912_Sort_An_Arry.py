#!/usr/bin/env python3

def quicksort(nums, s, e):
    if s >= e:
        return

    p = partation(nums, s, e)
    quicksort(nums, s, p-1)
    quicksort(nums, p+1, e)


def partation(nums, s, e):
    p = s
    index = p + 1
    i = index
    while i <= e:
        if nums[i] < nums[p]:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1

        i += 1

    nums[p], nums[index-1] = nums[index-1], nums[p]
    return index - 1




def quicksort_v2(nums):
    def helper(s, e):
        if s >= e:
            return

        l = s
        r = e
        p = (s - e) // 2 + e
        pivot = nums[p]
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1

            while l <= r and nums[r] > pivot:
                r -= 1

            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]

                l += 1
                r -= 1

        helper(s, r)
        helper(l, e)

    helper(0, len(nums)-1)
    return nums


def mergesort(nums):
    if len(nums) > 1:
        m = len(nums) // 2
        left = mergesort(nums[:m])
        right = mergesort(nums[m:])

        i = j = k = 0

        while i < len(left) and j < len(right) and k < len(nums):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    return nums


def heapsort(nums):
    build_max_heap(nums)
    lenn = len(nums)
    for i in range(lenn-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)

    return nums

def build_max_heap(nums):
    lenn = len(nums)
    n = lenn // 2 - 1
    for i in range(n, -1, -1):
        heapify(nums, lenn, i)


def heapify(nums, n, i):
    l = 2*i+1
    r = 2*i+2
    largest = i

    if l < n and nums[l] > nums[largest]:
        largest = l

    if r < n and nums[r] > nums[largest]:
        largest = r

    if largest != i:
        nums[largest], nums[i] = nums[i], nums[largest]

        heapify(nums, n, largest)
