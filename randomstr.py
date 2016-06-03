#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import random

def randomstr(length, enable_symbol=True):
    """
    長さlengthのランダムな文字列を返す
    enable_symbol == Trueで，記号を含めた文字列になる
    """
    string_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    if enable_symbol:
        string_list += '''!@#$%^&*()_+-=|\~`[]{};:'",<.>/?'''

    s = ''
    for i in range(length):
        s += random.choice(string_list)
    return s

if __name__ == '__main__':
    import sys

    usage = """USAGE:
    randomstr.py [LEN] ([OPTION])

    [LEN]       length of randomstrings.

    [OPTION]
    --non-symbole
                not use symbol in randomstrings.
    """
    # check arguments option
    if len(sys.argv) < 2:
        print(usage)
        exit()

    str_long = int(sys.argv[1])
    if len(sys.argv) == 3 and sys.argv[2] == "--non-symbol":
        print(randomstr(str_long, False))
    else:
        print(randomstr(str_long))
            
