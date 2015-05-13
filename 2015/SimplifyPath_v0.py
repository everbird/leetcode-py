#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        items = path.split('/')
        r = []
        for item in items:
            if item == '.' or item == '':
                pass
            elif item == '..':
                if r:
                    r.pop()
            else:
                r.append(item)

        return '/'+'/'.join(r)


if __name__ == '__main__':
    s = Solution()
    print s.simplifyPath('/home/')
    print s.simplifyPath('/a/./b/../../c/')
    print s.simplifyPath('/..')
