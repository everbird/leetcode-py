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


## Reverse Integer
首先用 1 或 -1 记录符号，设另一个变量r，r = r * 10 + n % 10, n = n // 10，注意若溢出则返回0


## Word Break
递归比较容易想到，但时间复杂度最坏情况 O(2^n)，最好情况O(1)，效率有问题；
若用 cache 的方式，即沿用上述递归思路，但加上 cache 装饰器用于记录输入和输出，相当于一个 loop 找匹配前缀，一个 loop 递归向下找所有后缀并 cache，最多有 n 个后缀，所以复杂度是 O(n^2)
也可以用 DP 的方式，一维数组`dp[n] = dp[i] and s[i:n] in wordDict`，外层循环计算每个 dp[n]，内层循环看s[:n] 是否可以利用此公式完成分隔，最后返回 dp[-1]

## String to Integer(atoi)
通过首字符判断 symbol 是 1  或 -1，数字部分从左到右遍历，通过ascii 码减法用 r = r*10 + i 得到数字部分 r；最后带符号返回，但需注意溢出判断，整数上界 2**31-1，下界 -2**31，返回 `max(下界，min(上界, r))`


##Palindrome Number
先处理特殊 case：0 直接返回 True；0结尾或小于0 的数直接返回 False
剩下的部分如下处理：从输入 m 右侧去掉数字 i ，并将其放在 r 的左侧，即：
```
i = m % 10
m = m // 10
r = r*10 + i
```
直到 r >= m，此时若为奇数回文，中心点在r；若为偶数回文，r==m；故返回 `m == r or (r // 10) == m`


## Regular Expression Matching
先处理特殊 case：pattern 和输入为空时返回 True，否则 pattern 为空时返回 False
剩下部分从 pattern 尾部开始看最后一个字符 p
若 p 非 ‘*’，p ==  s[-1] 或 p == ‘.’ 的话，递归，用少末尾字符串的 pattern 和 s 的子字符串作为输入
若 p == ‘*’，看 p 前一位字符串 rep，
1) rep == s[-1] 或 rep == ‘.’就递归看两种情况，一种 pattern 不变，s 少末尾一个字符；另一种 pattern 少末尾两个字符，s 不变。两者取或。
2) 如非上述情况，说明统配部分并未有匹配，故直接递归，pattern 少末尾两个字符，s 不变


## Divide Two Integers
先判断 symbol，然后采用二进制位移的方式，a 为被除数，b 为除数，找出比 b << shift  <= a 的最大者 x，此处认为是二分查找，因为每次 b 翻倍。将这个倍数不断累加到结果 r 中（相当每次得到二进制的r的一位 bit），并从 a 中减去该次 x。最后返回 symbol * r 并且考 `max(下界, min(上界, symbol*r))` 处理溢出


## Container With Most Water
Two pointer 递归，每次都移动较矮的一端， b=b+1 或 e=e-1 ，返回其与当前面积的最大者，递归终止条件是 b == e 时，此时返回 0


## Integer to Roman
倒序字典 d（可用 list + tuple） 记录 1 4 5 9 开头的对应的罗马数字，这里已经包含了字母放左右的变化，简化了很多。然后循环 d 的 k v，若k <= 输入的数字 i，则将 v append到输出右侧，而后 i-k 作为下次循环的输入，知道最后输入为 0 终止返回 ''


## Roman to Integer
1. 用字典 d 记录 1 4 5 9 开头的情况，罗马数字作 key，对应数字作 value；从右向左遍历输入字符串s，当前位置记为 p，`while p>=0`，若 p 和 p左边一个字符构成的字符串在 d 中，则将对应值累计入r 并 p+= 2 ，否则取 p 所在字符对应 d 中的输入累计入 r 并 p+= 1，最后返回 r
2. 先逐个数字母累计数值，然后减去加多得量，即看 s 中是否有特殊的组合，如 CD，其值为 400，但若单独看 C=100, D=500，故 CD 比单独看时多了 200将其减去


## Longest Common Prefix
从左到右逐个比较第 i 位的字母，若全相同 i+= 1，否则返回第一个字符串的 s[:i] 即可，注意处理边界情况，`i < min(map(len, strs))`


## 3 Sum
Two Sum 的变形，但思路类似。
首先对输入进行排序，然后用一个 loop 取 a，这样退化成了找 b + c = -a 的 Two Sum 问题，用 Two pointer对剩下的 nums 部分处理即可得到，并将结果计入 r，最终返回 r 即可。注意输入可能有重复，而排序后重复部分会联系，因此在计入 r 之后，需要跳过重复的部分。


## 3 Sum Closest
3 Sum 的变形，用 Two pointer 即可，因为题中假设每个输入对应只有一个输出，让事情简化了不少。
大致思路痛 3 Sum，区别在于每次内循环需计算当前 sum 值，保留sum 与预期值差最小的，最后将其返回


## Letter Combinations of a Phone Number
1. 比较直接的思路是递归，取少一个数字的子字符串对应的结果集，在末尾追加此数字对应的各种字母，但时间复杂度是 O(K^n) K 大概是 3
2. 也可以借助 reduce 来做，reduce(lambda acc, dight: [x+y for x in acc for y in d[digit]], digits, [‘’])，注意初始值是 ['']


## 4 Sum
直接推导至 k Sum，思路跟 3 Sum 类似，先排序。
在k > 2 时，用一个 loop 遍历数组每个数字 n，剩下的部分k -= 1，target = target - n，往下递归。所得结果和 n 合并计入 r；
k == 2 时，用 Two Sum 得到符合当前 target 的 tuple 计入 r；
返回 r 即可


## Remove Nth Node From End of List 
链表不好逆向取第几个，因此可以借助 math。
1. a 指针先从头遍历至第 n 个 node，此时在头部设另一指针 b。
2. while a.next is not None，a 和 b 同时向后遍历，直至 a.next 指向 None，返回此时 b.next 即为尾部算起第 n 个 node
3. b.next = b.next.next 直接删去此 node，返回 head
注意特殊情况，即从头遍历至第 n 时刚好 a 指向 None，说明 b坐在的头部即为要去除的 node，此时直接返回 b.next 即可


## Valid Parentheses 
非法的括号嵌套有特征：即右括号的前一个字符是不同的左括号。O(N) 遍历若发现符合此特征直接返回 False，否则返回 True


## Merge Two Sorted Lists
正常的链表归并排序，谁小拿走谁，被拿走的部分头指针下移。注意处理一种一个被拿空后的情况：
`if not l2 or (l1 and l1.val < l2.val) 拿 l1 else 拿 l2`


## 227 Basic Calculator II
输入中无括号，且均为非负数，故可以直接用 split，外层 loop 低优先级的 +-，内层 loop 计算 */ 的表达式。
单独计算 */ 表达式时按照从左到右的顺序即可，具体做法可以分两步，第一步获取 numbers 和 ops 数组，第二部遍历 ops，用 numbers[i+1] 存 i 位移时的计算结果，表达式返回 numbers[-1]。