#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/28 11:19 上午
# @Author  : jhyfugug
# @File    : hello.py
"""
seq：用来间隔多个对象，默认值是一个空格。也可以输入特定的值（符号、数字、中文都可）来间隔内容。
end：用来设定以什么结尾，默认值是换行符"\n"。也可以输入其他值来结尾。
"""

print("hello, world!")
print("你好，世界！")
print('你好', '世界！')
print('hello', 'world', sep=', ', end='!')
print('goodbye, world', end='!\n')

