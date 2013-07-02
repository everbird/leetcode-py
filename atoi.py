#!/usr/bin/env python
# -*- coding: utf-8 -*-



def atoi(s):
    sign_positive = True
    if s[0] == '-':
        sign_positive = False
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    r = 0
    length = len(s)
    for i in range(len(s)):
        if not s[i].isdigit():
            return 0

        r += int(s[i]) * pow(10, length - 1 - i)

    return r if sign_positive else -r

def run():
    a = '+1'
    r = atoi(a)
    assert r==1, 'Failed'
    print r

    a = '-123'
    r = atoi(a)
    assert r==-123, 'Failed:%s' % r
    print r

if __name__ == '__main__':
    run()
