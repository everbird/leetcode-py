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


## 230 Kth Smallest Element in a BST
1. 每次去掉最小节点，这样空间复杂度最小，时间复杂度为 O(KlogN)。
2. 用 list 在中序遍历时存下每个节点，然后返回 list 的 list[k-1].val，可以稍作裁剪，判断 len(list) == k 时返回 None，可跳过后面不必要的递归
3. 用 self.count 记录遍历节点数，中序遍历过程中 self.count+=1，当 count == k 时将节点记在 self.r 中，对于 self.count >= k 的情况直接返回 None 跳过后面不必要的递归


## EXP: Longest ZigZag subsequence

subsequence 指去掉任意元素后成为的子序列，只保留顺序，所以生成全部子序列要 O(2^N) 复杂度，因为相当于保留位置取 1，删除位置取 0，相当于 N 二进制的数量，故为  2^N

substring 指连续元素组成的子串，只需确定起始位置和终止位置，而他们的选择分别是 N 和 N-1，所以生成全部子串要 O(N^2) 复杂度

http://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
1. Brute force 要生成所有 subseq，然后验证每个 subseq 是不是 zigzag，复杂度O(N*2^N)
2. 动态规划，用两个数组分别记录 i 位置为末尾，上升和下降两种情况的最长结果，这样子问题可以如下描述：
initial: up[0] = down[0] = 1
func:
up[i] = max([down[j]+1 for j in range(i) if a[i] > a[j] ])
down[i] = max([up[j]+1 for j in range(i) if a[i] < a[j] ])

return: max(up+down)
之所以计算 up[i] 需要用到 a[i] > a[j] 是因为i为上升，若要子序列为上升且 zigzag，前一个位置 j 必定是下降且 j 处的值 a[j] < a[i]；同理对 down[i] 一样

## 231 Power of Two
判断 n 是否是 2 的 x 次方，从二进制的角度看即为最高位为1，其他位为0。而若成立，可以利用这样一条性质：n -1 会让所有位翻转。此时 n -1 与 n 按位做逻辑与，应该刚好得到 0。否则 n 并非 2 的 x 次方

## 232 Implement Queue using Stacks
直接用 stack 实现 queue 会发现若 push 为 O(1) 则 pop 和 peek 都会为 O(N)，因此使用一个倒置的 stack 作为数据结构来存 queue，这样 push 为 O(N)，每次都放到底部，而每次 pop 和 peek 直接用 stack 的 pop 和 peek 即可为 O(1)

## 233 Number of Dight One
找小于等于 n 的数字中所有的 1 的个数，可以按位来累计。从右开始逐位 i(从0开始) 取数字 cur，其左边为 left，右边为 right。统计 cur 出现 1 的个数时，有如下性质可以利用：
假设将 cur 和 right 所有位都补齐到 9：
此时比较简单，有 left+1 种情况来组成 <left>1<right>；right 也有 10**i 种情况。此时 v = (left+1)*(10**i)
但是这时是算多了的，需要减去算多的情况：
1. 当 cur 是 0 时，算多了 1<right> 的情况，而这个数量是 10**i，所以 v -= 10**i
2. 当 cur 是 1 时，算多了 1<right+> 的情况，这个数量是 (10**i - 1 - right)，所以 v-= 10**i - 1 - right
按上述方法将 v 累计起来，即为结果


## 42 Trapping Rain Water
Trapping Rain Water 的性质是从最高处开始向两侧，与该侧第二高处会形成水洼，然后递归下去。所以最高处两侧虽然方向不同但做法类似。
用辅助方法 max_i 找到某段内最高值及其 index。
1. max_i 找到整段最高处 i，两侧用 _trap 函数递归运算其储水量 return self._trap(height[:i+1], self._trap(height[i:][::-1]))，注意由于性质需要依赖之前的最高值，所以递归时要带着 i 处的值。
2. _trap 函数计算储水量，先看几种特殊 case：
1) 若节点数为 1 或 2，没有位置用来储水，所以直接返回 0；
2) 若 max_i height 得到的最大值为 0，即此处是平地，故无法储水，直接返回 0；
3) 否则开始正常计算，找出height[:-1] 的最高处 x，而之前的最高处为 height 最后一个元素 y，x左侧的部分继续带着 x 处用 _trap 递归；而剩下的部分可以计算其面积 area = (yi - xi - 1) * min(x, y)，注意 - 1 是因为边的宽度占 1，所以例如 xi = 0 yi = 2 时，只有 index 为 1处可以储水。area 还需减去除掉两边，其间的凸起处，所以遍历 height[xi+1:yi] 的每个元素 m，area -= m 即可。最后返回 self._trap(left) + area。


## 43 Multiply Strings
思路是用简单的乘法和加法，按照笔算乘法的步骤完成。
首先将乘法分解成单个数字和 string 相乘的简单乘法 _multi，和 string 相加的加法 _add，那么 multi(a, b) 函数即为 add(multi(a[:-1], b) + ‘0’, _multi(a[-1], b))，对于a or b 为 0 的可以直接返回 ‘0’，若a长度为1 则直接返回 _multi(a, b)；
剩下的就是实现 _add 和 _multi 函数，注意处理 carry

## 45 Jump Game II
题目限制是可以跳 a[i] 或少于 a[i] 步，求最少 jump 次数，因此这退化成了一个贪婪策略。即从左到右，在本次 jump 内可以计算出下一跳的最大范围，当本次最大位置与 i 重合时，说明该进行下一跳了，故count += 1 并重新标记能跳到的最大位置为 imax，每次迭代都计算imax = max(imax, i+a[i]) 以找到最大 jump 位置

## 46 Permutations
从输入 array 中 每次只 a = pop(i) 剩下的 array 继续递归，递归结果 r 的每一项都在最前面插入 a。递归终止条件是 array len 为 1，此时返回 [array]。特殊情况若 len 为 0，返回 [[]]。注意 python 中要不要修改迭代中的 array，做好做个复制

## 47 Permutations II
跟 46 Permutations 比较起来，有了重复的数字，对于重复的部分，如果按 46 Permutations 的方式，会出现重复结果，即 [1a,1b,2] 取 1a, [1b, 2]，时与 1b, [1a, 2] 时会冲突，故在a排序后，遍历过程中需比较 a[i] 和 a[i+1]，相同时 skip，不同时才加入结果。

## 48 Rotate Image
将正方形画出，然后找一个 a(x, y) 点，画出其被 clockwise rotate 90 度的情况，可以看出，若想 in-place 完成此任务，每动一个点需要连续依次移动 4 个点，用一个临时变量即可做到，重要的任务是正确写出这四个点移动的坐标：
t = m[y][x]
m[y][x] = m[n-x-1][y]
m[n-x-1][y] = m[n-y-1][n-x-1]
m[n-y-1][n-x-1]=m[x][n-y-1]
m[x][n-y-1] = t
另外需注意一点，虽然一眼看上去，遍历 1/4 的节点即可，但这是n为偶数的情况。若 n 为奇数时，其实被移动的 1/4 其实是个长方形，x 比 y 多 1（或 y 比 x 多1应该也可以），所以遍历取上界的时候，一个是 n // 2 一个是 (n+1) // 2，而中心点无需移动，不过被迭代进来也无妨
复杂度 O(N^2)

## 49 Anagrams
同字母异序，本质上是字符串各个字幕的排列问题，跟 permutation 一样。如何判断a和b是否为 anagrams？
方法一：O(N*LogN)的方法是 sort 字符串
方法二：O(N) 的方法是用 hash 记录每个字符的 count，然后逐个字符 count 比较相等与否。

该题整体思路很简单：
1. 对互为 anagram 的字符串构造相同的签名字符串
2. 用 hash 对相同签名者 append
3. 最后遍历一次 hash 中 value list 长度大于 1 的，拼接返回即可

构造签名字符串即可借助于上面两种方法：
借助方法一，排序后的字符串即可将 amagram 归到一起，O(N*M*log(M)) time, O(M*N) space
也可以用方法二，用每个字符串记录count 的 hash 构造一个签名，类似 a1b2c3 ，但构造时需要一个确定的字符排序，O(M*N) time,  O(log10(M)*N) space，注意 log10 是因为构造此签名相当于将 n 个字符压缩成了 n 的位数个字符，而默认是 10 进展，故认为压缩后字符长度为 log10(n)+1，忽略 +1

## 50 Pow(x, n)
最基本的操作当然认为是乘法，x*x 相当于 pow(x, 2))。当 n 为偶数时，设 y=Pow(x, n/2)，结果返回 y*y 即可，当n为奇数时 y*y*x 即可
Function: dp[n] = dp[n/2]*dp[n/2] if n %2 == 0 else dp[n/2]*dp[n/2]*x
Initial Status: dp[0]=1, dp[1]=2
用动态规划最终算出 dp[n] 即可
代码实现可以通过递归实现。需注意n可以为负数，需 1/pow(x, -n) 处理。O(log(N)) time，因为每次递归输入都折半。

## 51 N-Queens
n*n 棋盘放 n 个 queen，这类摆棋的题一般可用 backtrace 尝试。
若用 backtrace 需有 is_safe 方法负责探测是否可将 queen 摆放在 (x, y)，注意 is_safe 探测时只关心棋盘中已经处理过的部分，即横向是否有 Q，左上和左下斜线上是否有 Q，纵向上因为正在处理所以必然没有 Q，右侧还未处理所以不用管；用 solve 函数来递归处理第 n 列的 queen 摆放，逐列遍历用 is_safe 探测，若该位置可以放置，就更新棋盘上该位置为 Q，然后递归 solve(n+1)，其后将该位置重置回空，为后面的继续查找其他排法做了准备； solve 如果最后一列成功，说明此前的列都成功，这时记录下此种排法，然后直接返回，利用递归和被重置好的棋盘继续探测其他排法。
最后将记录下的所有排法返回即可
O(N^3) time, O(N^2) space

## 52 N-Queens II
只返回 solution 数量，#51 已能得到结果，但复杂度偏高。考虑简化 #51，棋盘可以用一维数组代替，初始为-1或None，其数据表示该 x 处放置的 Q 的y 值。solve 解决了最后一列时，只需将 count += 1。is_safe 的思路跟 #51 相差不多，但是斜向探测时可以借助两点横向和纵向距离相等来判断。backtrace 时将数组置回 -1 或 None
依然是 O(N^3) time，O(N) space

## 53 Maximum Subarray
O(N) time，遍历过程中记录最大累加值 max_v 和当前累加值 s，若累加后 s <0 就将 s = 0，否则看是否更新 max_v，最后返回 max_v 即可。注意询问空输入该如何返回。
D&Q，mid 找中间点，用 s, e 两个index，特殊情况是 s==e 时，返回 a[s]，s > e 时，返回MIN_INT。对于 mid 在最大subarray 中的情况，延 mid 分别向左右找到累加最大值，然后 max_r+a[mid]+max_l 与 divide_and_conque(a, s, mid-1), divide_and_conque(a, mid+1, e) 取 max 返回。O(N*log(N)) time

## 152 Maximum Product Subarray
用 max_v 和 min_v 记录当前连续的最大乘积和最小乘积，遍历 n in a，n > 0 时 max_v=max(n, max_v*n), min_v = min(n, min_v*n)。当 n <= 0 时，用 t 临时存 max_v 的值，有 max_v = max(n, min_v*n), min_v = min(n, t*n)，每次取 r = max(r, max_v) 更新结果，最终返回 r

比较 #53 和 #152 题目类似，但由于加法和乘法的性质不同，导致前者可以丢弃不是最大的部分，而后者要额外关注 min_v 的部分，因为负数会让 min_v*n 变成 max_v

## 54 Spiral Matrix
此类二维数组和 array 的输出变换题，如果是旋转的方式，那么根据其 direction 是横向还是纵向，确定方向前进次数，然后垂直方向的个数上限递减，从而达到旋转的效果。每次前进的方式由 direction 决定，0,1,2,3 对应 x+=1, y+=1, x-=1, y-=1，每次将该位置的值记录在 r 列表中，当 lenw >0 and lenh > 0 一直 while 循环。需注意x初始值为 -1，以使“前进-记录”的方式行得通。

## 54.1 Spiral Matrix 反过来出，即给定顺序数组1~n，用旋转的方式排列进一个 M*N的矩阵中
思路跟 #54 很相似，只是将v初始成1，m[y][x] = v，然后 v+= 1，其他没什么不同


## 55 Jump Game
注意题意，每个位置表示该位置 max jump count，所以唯一跳不到终点的情况是中间有 0 且之前的 jump 跳不过这个 0，当然如果出现在终点位置的 0 是可以忽略的，loop 时排除终点 index 即可。循环中记录此前能调到的最大位置 max_v，当前位置能跳到得最大位置为 a[i]+i。如果循环顺利结束，返回 True

## 56 Merge Intervals
每个元素是 Interval 对象，按 start 对输入排序后，可以确保 loop 时每个拿到元素的 start 不比当前合并到的范围的 start 小，所以 loop 时只需判断两种情况，一种是当前元素 t 和当前合并 m 有重叠，此时扩展当前合并 m.end 到 t.end；另一种是没有重合，故记录下 m 并m 重置为 t的范围。注意 loop 结束要将最后一个 m 加入记录，然后再返回

## 57 Insert Interval
用bool 变量标志 flag 是否要插入，然后 loop 每个 interval 与 new_interval 比较，此时有几种情况：
1. 某个 interval 覆盖了 new_interval，无需插入直接返回原 intervals 即可；
2. interval.end < new_interval.start，将 interval 记录到 r；
3. interval.start > new_interval.end，如果此时还没插入过，将 new_interval 先记录到 r，更新 flag 到无需插入，然后再将 interval 记录到 r；
4. interval 与 new_interval.start 部分重叠，将 new_interval.start 扩展到 interval.start；
5. interval 与 new_interval.end 部分重叠，将 new_interval.end 扩展到 interval.end；
最后若 loop 结束，检查 flag 若还需插入，表示需将 new_interval 插入到最末尾

## 58 Length of Last Word
返回最后一个 word 的长度，需注意忽略末尾的空格，用 e 记录最末非空字符 index，用 b 记录e向左遍历到的第一空格的 index，返回 e - s。若遍历结束返回 e + 1。

## 59 Spiral Matrix II
类似 #54.1 ，N，M 均为 n，v一直累加即可

## 60 Permutation Sequence
1. 利用 Next Permutation，从第一个开始做 k-1 次即可
2. 逐位来确定该字符串，候选数字列表c，因为全部 permutation 是顺序的，故每个字符开头的依次出现 x = !(n-1) 次，y = （k-1） // x 即 index，c[index]为首位数，然后 k = k % x，c 中剔除 c[index]，x /= (n-1-i)，循环n-1 次因为有最后一个字符串直接拼在末尾即可。若其间发现 k == 0，说明要取当前前缀下的最后一个序列，后续字符串直接取 c 的逆序拼接即可。将拼好的字符串结果返回

注意，可以用阶乘算出上界，过 k 超出，直接返回 None

## 61 Rotate List
找到分隔点重新组织链表即可。找分割点由于是从右向左算的，而且注意k可能大于链表长度，所以最好先遍历依次得到链表长度 l，然后 k %= l 得到需移动的步数，然后 l - k - 1 看需要从头移动几次，找到分割点后重新组织链表很简单

## 189 Rotate Array
简单题，有多重方法
1. 三次 in-place reverse
2. 计算 offset 后，连续 swap，使每个数字都在正确的位置上，被替换出的数字继续向下寻找
3. 新建一个 list 然后按加 offset 取模后的 index 赋值

## 62 Unique Paths
机器人走棋盘，只能右或下，问有多少种路径，简单 DP 题，设二维数组
Function: dp[y][x] = dp[y][x-1] + dp[y-1][x]
Initial Status: dp[0~n][0] = 1, dp[0][0~m] = 1
返回 dp[-1][-1] 即可

## 63 Unique Paths II
对比 # 62 棋盘上多了障碍，仍然 DP
Function: dp[y][x] = dp[y][x-1] + dp[y-1][x] if b[y][x] == 0 else 0
Initial Status: dp[0~n][0] 在遇到障碍前为 1，遇到障碍后为 0，dp[0][0~m] 同，用 break 即可
最后返回 dp[-1][-1]

## 64 Minimum Path Sum
DP 解决
Function: dp[y][x] = min(dp[y][x-1], dp[y-1][x])+a[y][x]
Initial Status: dp[0][0~n] 和 dp[0~m][0] 累加计算好
最后返回 dp[-1][-1]

## 174 Dungeon Game
勇士救公主，求勇士初始最小生命值，DP，二维数组表示勇士到达 (x, y) 所需最小生命值，由题可知必须 >= 1
Function: dp[y][x] = min(max(1, dp[y][x-1] - a[y][x]), max(1, dp[y-1][x] - a[y][x]))
Initial Status: dp[0][0~n] 和 dp[0~m][0] 按照 dp[0][i] = max(1, dp[0][i-1] - a[0][i]) 得到
其实 dp 可以多一行和一列，这样 dp[0][0] = 0 不过没关系反正不会用到，dp[0][0~n] 和 dp[0~m][0] 均为 0，后面的计算照旧。
最后返回 dp[-1][-1]

## 65 Valid Number
通过 4 个 flag bool 来逐字符判断
dotflag
eflag
has_sign
has_digit
初始均为 False
分五种 case：
1. 当前字符为数字，将 has_sign = True, has_digit = True
2. 当前字符为 + - 符号，判断若已有 has_sign = True，说明出现了多个符号，返回 False；否则 has_sign = True
3. 当前字符为 ‘e’ 或 ‘E’，判断若已有 eflag = True，说明出现多个 e，返回 False，也要判断 has_digit = True 不然没数字直接出现 e 也是不允许的；否则 eflag = True，dotflag = True 因为e 后面部分不允许小数，has_sign 和 has_digit 置回 False 因为这部分可以带符号
4. 当前字符为 ‘.’，判断若已有 dotflag = True ，说明出现多个点，返回 False；否则 dotflag = True，has_sign = True 点开头说明一定是正数
5. 其他字符非法，返回 False

最后注意由于一定要有数字才行，所以 return has_digit

## 66 Plus One
digit 数组表示一个 number，对其+1，返回结果
carry 默认为1，从右向左遍历，v = d[i] + carry 然后 d[i] = v % 10，carry = v // 10。
最后若 carry 存在，将 carry 拼在结果最左边 [carry] + d，否则返回 d

## 67 Add Binary
字符串来作二进制加法
carry = 0，取最长长度 loop，从右向左遍历 i，将字符转为 int 做加法+carry，然后 result += str(r % 2)，carry = r // 2，最后 carry 存在也要 result += str(carry)，最后返回 result[::-1]

## 68 Text Justification
思路分两步，第一步先分段，找出那些 words 在一行；第二步是对于一行的 words 如何将空格平均的放在间隔里。
第一步中，注意可将初始长度设为 -1，这样先算上个空格再算word 长度，会比较容易
第二步是难点，我们能知道限制长度 L，知道 words count w，对于一般情况，word 最好排列得两边顶头，故空白的位置有 w-1 个，total_spaces = L - map(len, words) 是总空格数，所以平均每个位置放置 cnt = total_spaces // (w - 1)。但是不平均时，左边要比右边多，所以用 total_spaces % (w-1) 能得到 index m 小于等于 m 的是需要 +1 spaces 的。最后将首个 word 先初始到 li 中，按 m 和 cnt 填入空格，直到排满 L 长度。
需要注意若出现一个 word 一行的情况，必然直接 word + ‘ ‘ 作为新行即可。

## 69 Sqrt(x)
可以使用的基本运算是乘法，相当于用 y*y 去试与 x 的关系，另外需注意题目要求只是整数
二叉搜索来做，对于 x>1 的情况，从 x // 2 处尝试即可，因为 2**2 =4, 3**2 = 9 ，其必然大于平方根
s = 0, e = x, mid = (s+e) // 2，如果 mid*mid == x 就返回 mid；如果 mid*mid > x 说明大了，收缩上界 e = mid - 1；否则收缩下界 b = mid + 1。
在最后返回时，需注意要返回 mid*mid < x 的最大整数，故 mid if mid*mid < x else mid - 1


## 70 Climbing Stairs
每次1 或 2 步，有多少种方法爬到 top，DP
Function: dp[i] = dp[i-1]+dp[i-2]
Initial Status: dp[0] = 1, dp[1]=2
最后返回 dp[-1]

## 71 Simplify Path
unix path 简化，先按 ‘/‘ 做 split，然后逐个 item 遍历，对于 空或者 ‘.’，直接 continue；对于 ‘..’，忽略其同时要 r.pop() 去掉当前最后一级目录；对于其他，append 到 r。最后 ‘/‘ + ‘/‘.join(r) 即可

## 72 Edit Distance
字符串 a 到 b 的最短修改距离，DP
Function: dp[y][x] = min(dp[y][x-1]+1, dp[y-1][x]+1, t)，t= dp[y-1][x-1] if a[y] == b[x] else dp[y-1][x-1] + 1
Initial Status: dp[0][0~m], dp[0~n][0] 均为对应 index 值，注意 dp 最好多一行一列，0表示长度为0的字符串
最后返回 dp[-1][-1] 即可

## 73 Set Matrix Zeroes
注意用临时标记代替 0，因为如果直接用 0，结果的0和待处理的0会混淆，增加处理次数。
分三步：
1. 先遍历 matrix 将遇到的 0 改为 None
2. 然后逐个遍历，遇到 None 的横纵列 in-place 置 0，但是 None 的依然保留
3. 最后一次遍历，将 None 改回到 0

## 74 Search a 2D Matrix
数组特征是每行升序，且下一行开头大于上一行结尾。判断 x 是否在 matrix 中。
思路：先二叉搜索判断找哪行，再在该行二叉搜索该数组是否存在
第一次二叉查找其实是要找到小于等于 x 的最大者所在 index，故二叉搜索时需要额外一个判断，即若 a[mid] < x and a[mid+1][0] > x，即可返回 mid，因为这就是要找的。剩下从一行中看元素是否存在就很容易了，简单二叉搜索即可。

## 75 Sort Colors
1. 直观的方式 two-pass，一遍记数量，一遍按数量逐个填充。
2. one-pass 的方式，相当于 左右端各有一个指针，rp指向最左侧第一个非 0 和bp 指向最右侧第一个非 2 的 index，保证左指针左边都是 0，右指针右边都是 2。i 遍历其间的各个数字，若为0 就 swap 到左指针，然后左指针右移一位，右侧同。注意存在同一位置 i 多次swap 的情况，所以 i 处需要 while nums[i] in (0, 2) 且 rp<=i<=bp，i <= bp 的每次外循环后 i+= 1

## 234 Palindrome Linked List
简单思路，list 存顺序遍历数字，然后比较 list[::-1] == list，相当于把链表简化为 list，O(N) time O(N) space
推荐用 two pointer 找到尾部开始点，对其 reverse 后，逐个节点比较 head 和reverse 后的rhead 中各个点，若不同即终止循环，此时若 rhead 已经为 None 说明是回文，否则不是。
reverse linked list 可以这样做：
pre, pre.next, head = head, pre, head.next
记住 python 这种 swap 的赋值语句 ，右侧在执行此行前已经确定，左侧才会从左到右随着赋值变化而变换。

## 235 Lowest Common Ancestor of a Binary Search Tree
其实就是从 root 开始找到第一个大小位于 p 和 q 之间的节点，如果 p q 都比节点大就向右查找，p q 都比节点小就向左查找。注意结果可以是 p 或 q。O(log(N)) time 
