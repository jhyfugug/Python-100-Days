#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/2/4 4:53 下午
# @Author  : jhyfugug
# @File    : for2.py

"""
用for循环实现1~100之间的偶数求和
"""

Sum = 0

for x in range(2, 101, 2):
    print(x)
    if x % 2 == 0:
        Sum += x

print(Sum)
