#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/2/3 1:40 下午
# @Author  : jhyfugug
# @File    : rolldice.py
from random import randint

face = randint(1, 6)

if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '坐俯卧撑'
elif face == 5:
    result = '学绕口令'
else:
    result = '讲冷笑话'

print(result)