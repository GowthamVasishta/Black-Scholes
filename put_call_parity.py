# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:55:42 2021

@author: Gowtham
"""

import sys
import math

sys.path.append(".")

from option import Option

spot = 125.94
strike = 125
riskfree_rate = 0.0446
vol = 0.83
time_to_maturity = 0.0959

put_option = Option("put", spot, strike, riskfree_rate, vol, time_to_maturity)
call_option= Option("call", spot, strike, riskfree_rate, vol, time_to_maturity)

put_premium = put_option.price()
call_premium = call_option.price()


# LHS of put call parity
lhs = put_premium + spot

# RHS of put call parity
rhs = call_premium + (strike * math.exp(- riskfree_rate * time_to_maturity))

## check if LHS and RHS are equal
if(round(lhs,3) == round(rhs, 3)):
    print("Equal")
else:
    print("Not equal")