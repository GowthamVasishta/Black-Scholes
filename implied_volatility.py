# -*- coding: utf-8 -*-
"""
Calculate Implied Volatility using trial-and-error search

@Created: Sat Jul 24 13:02:09 2021
@author: Gowtham
"""

import math
from pricer import Option

option_type = "call"
spot = 125.94
strike = 125
riskfree_rate = 0.0446
time_to_maturity = 0.0959
market_price = 13.5533

# Implied vol intial value
iv_estimate = 0.0001

tolerance = 0.0005

low = 0
high = math.inf


iteration = range(100)

for i in iteration:
    
    BS_option = Option(option_type, spot, strike, riskfree_rate, iv_estimate, time_to_maturity)
    
    model_price = BS_option.price()
    
    if (abs(model_price - market_price) < tolerance):
        break
    
    elif (model_price > market_price):
        high = iv_estimate
        iv_estimate = ((low + high)/2) 
        
    else:
        low = iv_estimate
        
        if(math.isinf(high)):
            high = low * 2
        
        iv_estimate = ((low + high)/2) + 2 * low
        
        
print("Implied Vol: ", iv_estimate)
print("No of iteration:", i)