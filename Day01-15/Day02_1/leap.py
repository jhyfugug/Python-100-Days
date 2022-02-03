#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/29 12:21 下午
# @Author  : jhyfugug
# @File    : leap.py

"""
输入年份 如果是闰年输出True 否则输出False
"""

year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

if is_leap == True:
    print('输入的%d年份是闰年' % year)
else:
    print('输入的%d年份不是闰年' % year)