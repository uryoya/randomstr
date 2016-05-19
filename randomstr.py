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

    print(randomstr(int(sys.argv[1])))
        
