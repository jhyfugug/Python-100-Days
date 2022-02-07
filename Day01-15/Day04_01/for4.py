#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/2/4 5:04 下午
# @Author  : jhyfugug
# @File    : for4.py

"""
输入一个正整数判断它是不是素数
"""
num = int(input('num = '))
x = 0
for i in range(2, num + 1):
    if num % i == 0:
        x += 1
        print(i)
        print(x)
    print(i)
if x <= 1 and num != 1:
    print('当前正整数是素数！')
else:
    print('当前正整数不是素数！')
