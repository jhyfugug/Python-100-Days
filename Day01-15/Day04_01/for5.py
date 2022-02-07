#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/2/4 5:44 下午
# @Author  : jhyfugug
# @File    : for5.py
"""
输入两个正整数计算最大公约数和最小公倍数
"""

a = int(input('a = '))
b = int(input('b = '))

if a > b:
    (a, b) = (b, a)

for x in range(a, 0, -1):
    if a % x == 0 and b % x == 0:
        print('%d和%d的最大公约数是%d' % (a, b, x))
        print('%d和%d的最小公倍数是%d' % (a, b, a * b / x))     # 两个正整数的乘积等于最大公约数乘以最小公倍数
        break


