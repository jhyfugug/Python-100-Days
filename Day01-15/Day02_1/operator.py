#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/29 12:30 下午
# @Author  : jhyfugug
# @File    : operator.py

"""
运算符的左右
"""

a = 5  # 给a赋值为5
b = 10  # 给b赋值为10
c = 3  # 给c赋值为3
d = 4  # 给d赋值为4
e = 5  # 给e赋值为5
a += b  # a = a + b，a = 10 + 5
a -= c  # a = a - c, a = 15 - 3 = 12
a *= d  # a = a * d, a = 12 * 4 = 48
a /= e  # a = a / e, a = 48 / 5 = 9.6
print("a = ", a)

# 判断真假

flag1 = 3 > 1   # 3 > 1 正确得真true
flag2 = 2 < 1   # 2 < 1 错误得假flase
flag3 = flag1 and flag2     # 根据flag1为真，flag2为假，得flag3为假
flag4 = flag1 or flag2      # 根据flag1为真，flag2为假，得flag4为真
flag5 = not flag1       # 根据flag1为真，得flag5为假
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)
