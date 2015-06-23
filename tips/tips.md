## Two Sum
1. sort + two pointer
2. target - 当前，得出预期存入dic or set，下次拿到当前值时检验 dict or set


## Add Two Numbers
链表，记录 carry，不要忘记最后一步加上 carry


## Longest Substring Without Repeating Characters
初始 start=0，遍历字符串，dict 记录每个字符的 index，若遇相同字符 start 置为 pos+1，否则计算当前 i- start + 1 长度看是否最大，记录最大值


## Median of Two Sorted Arrays
merge sort 思路，two pointer 累计执行 n // 2 + 1 次，需记录 pre 元素，若n为奇数则只返回当前元素，若为偶数则返回当前元素和 pre 元素的平均值


## Longest Palindromic Substring
用 `#` 补齐每个字符间隙，以规避奇数回文和偶数回文的计算差异；初始当前右边界最靠右侧的回文中心index C 和该回文右边界 R 为0，遍历补齐后的字 符串，P[i] 记录当前 index 的回文最大半径； index 关于当前中心 C 对称的位置 _i，在只考虑以 C 为中心，R 为右边界的回文字符串内，P[_i]和 P[i]是相等的，但 P[_i] 处实际的回文半径可能超出了 C-R 构成的回文字符串，而超出的情况下，P[_i] 不适合作为 P[i] 的初始值，但此时可确保 _i 处回文半径至少达到 C-R 构成的回文边界，如此作为镜像的 i 处，自然也可以将 R-i 作为 P[i] 的初始回文半径；但是如果 i 并不在 C-R 覆盖之内时，P[i]没法借助 C-R ，只能从 0 开始了；然后通过 while 向最后多一位置做测试得到最大值；其间若 i+P[i] 计算出的新的右边界如果超出了 R ，则更新 C 和 R ；遍历后从 P 中找到最大半径及其 index，即可算出子字符串


## ZigZag Conversion
初始化有 nRows 个列表的列表r，用 i 来记当前 row 的index，flag 为 1或-1 记方向，当 i == nRows-1 或 0 时反转 flag。最后逐行遍历 r，输出字符串



