#!/usr/bin/env python3

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        nw = len(word)
        rboard = zip(*board)
        for b in board, rboard:
            for row in b:
                words = "".join(row).split("#")
                for w in words:
                    targets = [word, word[::-1]]
                    for t in targets:
                        if nw == len(w):
                            if all(w[i] == ' ' or w[i] == t[i] for i in range(nw)):
                                return True

        return False
