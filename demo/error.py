#!usr/bin/env python3
# -*- coding:utf-8 -*-
import logging

try:
    r = 10 / int('a')
    print(r)
except Exception as e:
    raise TypeError('TypeError!')
    print(e)