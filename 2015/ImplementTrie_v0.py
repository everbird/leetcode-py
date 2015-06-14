#!/usr/bin/env python
# encoding: utf-8


class TrieNode:
    # Initialize your data structure here.
    def __init__(self, val=None):
        self.val = val
        self.children = []
        self.is_word = False

    def __repr__(self):
        return '<{}>'.format(self.val)


def printt(n):
    if n:
        print n
        for c in n.children:
            printt(c)


def makelist(word):
    h = p = TrieNode(word[0])
    for c in word[1:]:
        n = TrieNode(c)
        p.children.append(n)
        p = n

    p.is_word = True
    return h


class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        p = self.root
        s = 0

        while p:
            for n in p.children:
                if n.val == word[s]:
                    s += 1
                    p = n
                    if s == len(word):
                        p.is_word = True
                        return

                    break
            else:
                h = makelist(word[s:])
                p.children.append(h)
                break

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        if not word:
            return False

        s = 0
        p = self.root
        while p:
            for n in p.children:
                if word[s] == n.val:
                    s += 1
                    p = n
                    if s == len(word):
                        return p.is_word
                    break
            else:
                return False


    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        s = 0
        p = self.root
        while p:
            for n in p.children:
                if prefix[s] == n.val:
                    s += 1
                    p = n
                    if s == len(prefix):
                        return True
                    break
            else:
                return False


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")


if __name__ == '__main__':
    s = Trie()
    #h = makelist('hello')
    #printt(h)
    #s.insert('there')
    #s.insert('their')
    #print s.search('there')
    #print s.search('they')
    #print s.search('the')
    #print s.startsWith('the')
    s.insert("abc")
    print s.search("abc")
    print s.search("ab")
    s.insert("ab")
    print s.search("ab")
    s.insert("ab")
    print s.search("ab")
