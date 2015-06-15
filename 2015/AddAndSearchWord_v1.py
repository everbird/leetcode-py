#!/usr/bin/env python
# encoding: utf-8


from collections import defaultdict

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = defaultdict(dict)

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        p = self.root
        for c in word:
            r = p.get(c)
            if not r:
                p[c] = defaultdict(dict)
            p = p[c]

        p['$'] = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        s = 0
        lenw = len(word)
        p = self.root
        while s < lenw and p:
            c = word[s]
            if c == '.':
                keys = p.keys()
                for k in keys:
                    if k == '$':
                        continue

                    new_word = word[:s] + k + word[s+1:]
                    if self.search(new_word):
                        return True
                return False

            p = p[c]

            s += 1

        return '$' in p


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")


if __name__ == '__main__':
    wd = WordDictionary()
    #wd.addWord('there')
    #wd.addWord('their')
    ##print wd.search('there')
    ##print wd.search('therer')
    #print wd.search('the.e')
    #wd.addWord("a")
    #wd.addWord("a")
    #print wd.search(".")
    #print wd.search("a")
    #print wd.search("aa")
    #print wd.search("a")
    #print wd.search(".a")
    #print wd.search("a.")
    wd.addWord("at")
    wd.addWord("and"),
    wd.addWord("an"),
    wd.addWord("add"),
    print wd.search("a"),
    print wd.search(".at"),
    wd.addWord("bat"),
    print wd.search(".at"),
    print wd.search("an."),
    print wd.search("a.d."),
    print wd.search("b."),
    print wd.search("a.d"),
    print wd.search(".")
