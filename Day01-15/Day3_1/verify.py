#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/2/4 4:15 下午
# @Author  : jhyfugug
# @File    : verify.py

"""
用户身份验证
"""

username = input('请输入用户名： ')
password = input('请输入密码： ')
if username == 'admin' and password == '123456':
    print('密码验证成功！')
else:
    print('密码验证失败！')