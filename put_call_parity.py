# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:55:42 2021

@author: Gowtham
"""

import sys

sys.path.append(".")

from option import Option

# Option(Type, spot, strike,rate, vol, time to maturity)
put_option = Option("put", 125.94, 125, 0.0446, 0.83, 0.0959)
call_option= Option("call", 125.94, 125, 0.0446, 0.83, 0.0959)


put_premium = put_option.price()
call_premium = call_option.price()
strike = put_option.option_strike
spot = put_option.underlying_price
riskfree_rate = put_option.riskfree_rate
time_to_maturity = put_option.time_to_expiry

# LHS of put call parity
lhs = put_premium + spot

# RHS of put call parity
rhs = call_premium + (strike / pow((1 + riskfree_rate), time_to_maturity))

## check if LHS and RHS are equal
if(round(lhs,1) == round(rhs, 1)):
    print("Equal")
else:
    print("Not equal")