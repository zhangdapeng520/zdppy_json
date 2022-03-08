#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 23:54
# @Author  : 张大鹏
# @Site    : 
# @File    : z01_解析decimal类型.py
# @Software: PyCharm
from zdppy_json import dumps

import decimal

d = {"a": decimal.Decimal(33.33)}
print(dumps(d))
