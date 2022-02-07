#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/2/4 4:57 下午
# @Author  : jhyfugug
# @File    : for3.py

"""
输入非负整数n计算n!
"""
n = int(input('n = '))
result = 1

if n > 0:
    for x in range(1, n + 1):
        result *= x
    print('%d! = %d' % (n, result))
else:
    print('你输入的数字非正整数!')

