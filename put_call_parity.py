# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:55:42 2021

@author: Gowtham
"""

import sys

sys.path.append(".")

from option import Option




option = Option("put", 125.94, 125, 0.0446, 0.83, 0.0959)
price = option.price()
print(price)