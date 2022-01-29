#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/29 11:20 上午
# @Author  : jhyfugug
# @File    : centigrade.py

"""
将华氏温度转换为摄氏温度
F = 1.8C + 32
"""

f = float(input('请输入华氏温度： '))
c = (f - 32) / 1.8
print('%.1f华氏温度 = %.1f摄氏温度' % (f, c))
