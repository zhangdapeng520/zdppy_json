#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 22:59
# @Author  : 张大鹏
# @Site    : 
# @File    : z02_读写配置.py
# @Software: PyCharm
from zdppy_json import Json

j = Json()
print(j)

# 更新配置
j.update_config({"debug": False, "a": 11, "b": [22, 33]})
print(j)
