#!/usr/bin/env python
# encoding: utf-8


class Node(object):
    def __init__(self, v):
        self.v = v
        self.children = []
        self.is_word = False

    def __repr__(self):
        return '<{}:{}>'.format(self.v, self.is_word)


def printl(n):
    if n:
        print n
        for c in n.children:
            printl(c)


class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = Node(None)

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        p = self.root
        s = 0
        while p:
            for c in p.children:
                if word[s] == c.v:
                    p = c
                    s += 1
                    if s == len(word):
                        p.is_word = True
                        return
                    break
            else:
                h = self.makelist(word[s:])
                if h:
                    p.children.append(h)
                break


    def makelist(self, word):
        head = pre = None
        lenw = len(word)
        s = 0
        while s<lenw:
            p = Node(word[s])
            if not head:
                head = p

            if pre:
                pre.children.append(p)

            pre = p
            s += 1

        pre.is_word = True
        return head


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        s = 0
        p = self.root
        while p:
            if word[s] == '.':
                r = False
                for c in p.children:
                    r = r or self.search(word[:s]+c.v+word[s+1:])

                return r

            for c in p.children:
                if c.v == word[s]:
                    p = c
                    s += 1
                    if s == len(word):
                        return p.is_word
                    break
            else:
                return False


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
