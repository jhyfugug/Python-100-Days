#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/29 3:27 下午
# @Author  : jhyfugug
# @File    : string.py

"""
字符串常用操作
"""

str1 = 'hello, world!'
print("字符串的长度是：", len(str1))
print("单词首字母大写：", str1.title())
print("字符串变大写：", str1.upper())
print("字符串是不是大写：", str1.isupper())
print("字符串是不是以hello开头：", str1.startswith('hello'))
print("字符串是不是以world!结尾", str1.endswith('world!'))
print("字符串是不是以感叹号！开头", str1.startswith("!"))
print("字符串是不是以感叹号！开头", str1.endswith("!"))
str2 = '- \u738b\u52c7'
str3 = str1.title() + ' ' + str2.lower()
print(str3)


