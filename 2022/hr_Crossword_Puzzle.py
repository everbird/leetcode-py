#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#

def crosswordPuzzle(crossword, words):
    # Write your code here
    N = 10

    def check(arr, word):
        rs = []
        n = len(word)

        for i in range(N - n + 1):
            if arr[i] == "+":
                continue

            if all(arr[i+x] == '-' or arr[i+x] == word[x] for x in range(n)):
                rs.append(i)

        return rs

    def get_col(i):
        return [crossword[x][i] for x in range(N)]

    def place_word(x, y, dx, dy, word):
        for ch in word:
            crossword[y][x] = ch
            y += dy
            x += dx

    def delete_word(x, y, dx, dy, word):
        n = len(word)

        for i in range(n):
            crossword[y][x] = "-"
            y += dy
            x += dx

    def solve(crosswords):
        if not words:
            return crossword

        word = words.pop()

        solutions = []

        for i, row in enumerate(crossword):
            rs = check(row, word)
            if rs:
                solutions.extend([(1, 0, x, i) for x in rs])

        for i in range(N):
            col = get_col(i)
            rs = check(col, word)
            if rs:
                solutions.extend([(0, 1, i, x) for x in rs])

        for dx, dy, x, y in solutions:
            place_word(x, y, dx, dy, word)
            if solve(crossword):
                return True
            delete_word(x, y, dx, dy, word)
        words.append(word)
        return False

    solve(crossword)
    return ["".join(row) for row in crossword]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(list(crossword_item))

    words = input()
    words = words.split(";")
    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
