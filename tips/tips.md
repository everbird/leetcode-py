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


## 22 Generate Parentheses
用递归并记录当前字符串及还需左右括号的数量，计入 list r 返回。要生成合法的括号组合：
1. left == 0 而 right > 0 时，全部用右括号补齐计入 r
2. `0 < left < right` 时，分别递归追加左括号和右括号，计入 r
3. left == right 且不为 0 时，只能追加左括号，计入 r
4. 其他情况不会出现，否则必然不是合法的括号组合


## 215 Kth Largest Element in an Array
排序和大顶堆的方法比较容易想到，但复杂度分别为 O(NlogN) 和 O(N+kLogN)。
借鉴 Quick Sort 的方式，每次找 pivot 做 partition，看 pivot 是否为 k，若pivot < k则 left = pivot + 1 否则 right = pivot - 1。partition 方法可以先认为尾部元素是 pivot，用 swap 实现，但最坏情况是 O(N^2)，一般情况为 O(N)。
改进可随机取 pivot，排序时间不依赖于输入是否有序，最坏情况还是 O(N^2)，认为复杂度是 O(N)


## 23 Merge k Sorted Lists
分治法，分为两半递归，然后将两者 merge sort 归并；归并部分同 Merge Two Sorted Lists。


## 24 Swap Nodes in Pairs
普通链表题，记录遍历时记录当前节点c、前节点p、后节点n，然后 while c and c.next：
```
t = n.next if n else None 记录下次 loop 的节点
c.next = t 
n.next = c
p.next = n
p = c  下次的连接点

c = t c指向下次的当前节点
```
循环结束后，要记得 p.next = c，最后返回 head.next，因为结果链表必然是 head.next 为头。特殊情况空链表或只有一个 node 的，返回 head 即可


## 25 Reverse Nodes in k-Group
is_enough 函数从当前节点向后找 k 个，若找够了 k 个，则返回 True, 当前节点h，第 k 个节点 b；否则返回 False, 当前节点h，None
reverse 用于翻转从当前节点算起的 k 个节点，无需返回
while 循环当 is_enough 能找够 k 个时，f 若为 False 就 break。先记录下次起始节点 c= b.next，用 reverse 从当前 h 处翻转 k 个，然后将上次结果的尾部 p.next = b，h.next = c 链接好新的头尾
然后 p = h，h = b.next if b else None 进入下次循环
由于最后一次 f 为 False break 出来，仍需 p.next = h 链接好剩下的部分。
为了方便获取返回的头节点，开始用 r = p = ListNode(0) 作为辅助节点，最终结果返回 r.next 即可，因为这是 p 第一次链接翻转后头部的位置


## 26 Remove Duplicates from Sorted Array
O(N) 逐项遍历，由于已经是有序的，故出现重复必然是连续某个数字重复出现，因此初始 count = 1，记录前一个数 p 和当前数 c，在 p != c 的时候，另 nums[count] = c，count += 1，即用输入 list 的前一部分存储去重结果。最后新的长度 count


## 27 Remove Element
O(N) 遍历，当前元素与 val 不相等时nums[i] = n, count += 1，count 初始为 0。最后返回 count


## 229 Majority Element II
由于要找出多于 n/3 的元素，那么可以通过计数来最终圈定这些元素的范围，因为采用策略如下：
遍历数组，若存在于 d 中或 d 元素少于 3，就向 d 中累计，否则就对 d 中得全部元素减一，对于已经为零的，踢出 d。这样对于多余 n/3 的元素，最终必然会留在 d 中。然后再次遍历数组，只累计此小范围内的元素数量，找出多余 n/3 的返回即可。
由此也可知此方法可以推广至m，m=2~n


## 31 Next Permutation
查找峰左侧一个元素 index，初始为 -1，若非找得到，该元素和右侧下坡最右一个大于峰值的元素交换；然后将右侧下坡reverse成上坡，即 reverse(nums, index+1, lenn-1)


## 32 Longest Valid Parentheses
遍历，用 stack 存遇到每个左括号的 index，遇到右括号时：
1. 若stack 为空无法 pop 则说明该右括号是不合法的，故合法index 起始位置 last 重置为此处 i
2. 不 append，而是 pop stack，因为 stack 都是左括号；。然后判断 pop 后 stack 是否为空，若为空则该处长度为 i - last；否则 stack 中仍有未匹配完的左括号，故长度为 i - stack[-1]
用 max_l 记录下最长的长度返回即可


## 33 Search in Rotated Sorted Array
O(logN) 二叉搜索找 pivot，然后再二叉搜索找 pivot 两侧的元素 index。
注意查找 pivot 时，比较index 为 0，mid，-1 的元素
1. 若 nums[0] < nums[mid] < nums[-1] 则是递增的，pivot 为最右侧元素
2. 若 nums[0] < nums[mid] > nums[-1] 则继续丢弃左边，因为其为递增，而 pivot 必然在右侧；
3. 若 nums[0] > nums[mid] < nums[-1] 则丢弃右侧，因为右侧递增，而 pivot 必然在左侧
用 O(N) 的方法可以很见到找到 pivot，若卡住可以先用 O(N) 的解法找到 pivot 先


## 34 Search for a Range 
要求 O(logN) 所以二叉搜索变种，对于 mid 初始 l = r = mid，然后 l 向左 r 向右 while 找到边界。
上述用 while 找边界在重复较多时复杂度会趋向于 O(N)，改为用二叉搜索找边界更合适。

## 35 Search Insert Position
二叉搜索，最后未找到时判断 nums[mid] 和 输入k 的关系，nums[mid] > k 返回 mid，否则返回 mid+1

## 36 Valid Sudoku
根据数独的规则，按照行、列、3*3 方格逐个验证 unique，一旦发现不符就return False，否则通过检查


## 37 Sudoku Solver
用 backtrace 思路，find_unassigned 找到未填的位置，逐个数字验证是否 is_safe，用 is_solved 方法递归，一旦 is_solved 为 True 就返回 True，否则将该次处理的位置置回 ‘.'

## 38 Count and Say
先实现单词处理函数：逐个字符遍历输入字符串，记录上一个字符为 p，若p为None重置 count = 1，否则p != c 时向结果 r 拼接 str(count) + p；p == c 时 count += 1。遍历结束后需记得将剩下的 count 和 p 拼接，r + str(count) + p
将’1’作为初始值，输出作为输入循环 n -1 次即为结果


## 39 Combination Sum
C排序，由于 C 元素可重复使用，且结果需为递增，所以直接递归f，遍历 C 中元素，递归找f(C[i:], T-n)结果 items，对 items 中每个 list 头部插入 n。


## 40 Combination Sum II
C排序，C 中每个元素只能使用一次，对于重复的，遍历时只递归第一个元素，其余重复元素跳过，这样可以避免追加结果是出现重复；递归函数多一个 start 变量，表示从 candidates 数组何处开始计算，这样避免做 slice 的 copy；当 T 小于遍历的元素时直接 break，因为所有数字为正数，这些可以丢弃。递归终止条件依旧是 T 小于 0 返回 []；T 等于0 返回 [[]]


## 44 Wildcard Matching
DP，遍历 pattern 逐个字母c，dp 数组长度为 s 长度+1，表示子 pattern为包括c之前时，s不同长度匹配与否；因此有：
1. c 为 ‘*’ 时，dp 目前为去掉此 * 的 pattern的匹配情况，若找到最靠左的一个匹配i，由于为 *，故其后一定匹配，因此将i以后的 dp 全部置为 True
2. c 为 ‘?’时，由于加上任意一个非空字符才匹配，故相当于 dp 结果全部右移，首位 dp[0] = False
3. c 为其他时，倒序遍历，若该字符相同且之前 dp[i] 为 True，则dp[i+1] = True，最后首位 dp[0] = False，因为出现这类字符的情况下，dp[0] 一定是 False


## 41 First Missing Positive
逐个数值遍历，尝试将 nums[i] 放在正确的位置上，所谓的正确位置是，所在 index+1即为该数值；用 while 循环尝试位置 i，因为每次尝试成功，原来在 i 位置的数字被放去了正确位置，而新的数字被放到了 i 位置。循环交换条件是:
1. 该 nums[i] 大小需在 lenn > nums[i] >0 之间，否则必然找不到正确位置
2. nums[i] != i+1 即当前 i 已经是正确的了，就不必再换了
3. nums[i] != nums[nums[i]-1] 即虽然当前位置不对，但目标地址的数值和这里一样，交换也没意义

遍历一遍后确保能被放置在正确位置的数字已经被放置好，再次从头遍历，一旦发现 nums[i] != i+1 的，即为第一个缺失的正数
