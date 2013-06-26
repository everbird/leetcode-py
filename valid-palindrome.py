#!/usr/bin/env python
#-*- coding:utf-8 -*-


def valid_palindrome(s):
    items = [item.lower() for item in s if item.isalnum()]
    i = 0
    j = len(items) - 1
    while i < j:
        if items[i] != items[j]:
            return False
        i += 1
        j -= 1

    return True


def run():
    a = 'A man, a plan, a canal: Panama'
    r = valid_palindrome(a)
    assert r==True

    a = 'race a car'
    r = valid_palindrome(a)
    assert r==False


if __name__ == '__main__':
    run()
