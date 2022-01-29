#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/29 11:25 上午
# @Author  : jhyfugug
# @File    : circle.py

import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长= %.2f' % perimeter)
print('面积= %.2f' % area)
