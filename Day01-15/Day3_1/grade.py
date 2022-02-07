#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/2/3 1:24 下午
# @Author  : jhyfugug
# @File    : grade.py

"""
百分制成绩转等级制成绩
90分以上 	 	--> A
80分~89分 	--> B
70分~79分	--> C
60分~69分	--> D
60分以下		--> E
"""

grade = float(input('请输入成绩： '))
if grade >= 90:
    grade = 'A'
elif grade >= 80:
    grade = 'B'
elif grade >= 70:
    grade = 'C'
elif grade >= 60:
    grade = 'D'
elif grade >= 0:
    grade = 'E'
else:
    grade = '无效成绩！！！'
print('成绩等级为：', grade)

"""
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
elif grade >= 0:
    print('E')
else:
    print("请输入有效成绩！！！")
"""
