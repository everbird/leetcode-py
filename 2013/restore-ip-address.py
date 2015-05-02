#!/usr/bin/env python
# -*- coding: utf-8 -*-


result = []

def str_to_ip(s):
    global result
    yield_head(s, [], 1)
    return result


def yield_head(s, current, num):
    global result

    if not s:
        return None

    if num == 4:
        if len(s) < 4 and int(s) <= 255:
            _current_x = current[:]
            _current_x.append(str(int(s)))
            result.append(_current_x)
        return

    one_digit = s[:1]
    left = s[1:]
    _current_1 = current[:]
    _current_1.append(str(int(one_digit)))
    yield_head(left, _current_1, num+1)

    if len(s) > 1:
        two_digit = s[:2]
        if not two_digit.startswith('0'):
            left = s[2:]
            _current_2 = current[:]
            _current_2.append(str(int(two_digit)))
            yield_head(left, _current_2, num+1)

    if len(s) > 2:
        three_digit = s[:3]
        if not three_digit.startswith('0') and three_digit.startswith('00'):
            if 0 <= int(three_digit) <= 255:
                left = s[3:]
                _current_3 = current[:]
                _current_3.append(str(int(three_digit)))
                yield_head(left, _current_3, num+1)


def run():
    r = str_to_ip('010010')
    print r

if __name__ == '__main__':
    run()
