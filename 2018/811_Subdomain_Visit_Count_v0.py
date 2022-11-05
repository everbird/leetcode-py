#!/usr/bin/eni python
# encoding: utf-8

from collections import defaultdict

class Solution(object):

    def subdomainVisits(self, cpdomains):
        d = defaultdict(int)
        for cpdomain in cpdomains:
            cnt, domain = cpdomain.split()
            cnt = int(cnt)
            for subdomain in get_subdomains(domain):
                d[subdomain] += cnt

        return [
            '{} {}'.format(v, k)
            for k, v in d.iteritems()
        ]


def get_subdomains(domain):
    items = domain.split('.')
    return [
        '.'.join(items[i:])
        for i in xrange(len(items))
    ]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            ["9001 discuss.leetcode.com"],
            ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
        ),
        (
            ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
            ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
        ),
    ]
    f = s.subdomainVisits
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        r = sorted(r)
        expected = sorted(expected)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
