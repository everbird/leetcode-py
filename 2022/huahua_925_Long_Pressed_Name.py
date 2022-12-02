#!/usr/bin/env python3

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        sn = st = 0
        en = len(name)-1
        et = len(typed)-1
        pre = None
        while sn <= en and st <= et:
            # match and move on
            if name[sn] == typed[st]:
                pre = typed[st]

                sn += 1
                st += 1
                continue

            # not match, skip the long pressed chars
            while st <= et and typed[st] == pre:
                st += 1

            if st > et or name[sn] != typed[st]:
                return False

            pre = typed[st]
            sn += 1
            st += 1

        while st <= et and typed[st] == pre:
            st += 1

        return sn > en and st > et
