#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/2/4 4:39 下午
# @Author  : jhyfugug
# @File    : for1.py

Sum = 0

for x in range(1, 101):
    if x % 2 == 0:
        Sum += x

print(Sum)
