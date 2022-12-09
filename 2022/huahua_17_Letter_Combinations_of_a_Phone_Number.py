#!/usr/bin/env python3

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        rs = []
        for digit in digits:
            chars = d[digit]
            if not rs:
                for char in chars:
                    rs.append(char)
            else:
                _rs = []
                for r in rs:
                    for char in chars:
                        _rs.append(r + char)
                rs = _rs

        return ["".join(x) for x in rs]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        rs = []
        length = len(digits)
        if length == 0:
            return rs

        def backtrace(index, path):
            if index == length:
                rs.append("".join(path))
                return

            chars = d[digits[index]]
            for char in chars:
                path.append(char)
                backtrace(index+1, path)
                path.pop()

        backtrace(0, [])
        return rs

# backtrace / DFS
