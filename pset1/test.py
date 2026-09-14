# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:13:31 2026

@author: Admin
"""

def test(memo = {}, start = 10):
    if start == 1:
        return 1
    else:
        test(memo = memo, start = start - 1)
        memo[start] = 'hello'
    print(memo)
test()