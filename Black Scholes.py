# -*- coding: utf-8 -*-
"""
Black Scholes Formula

@Created: Sat Jul 17 20:07:21 2021
@author: Gowtham
"""

import math
from scipy.stats import norm

class option:
    
    def __int__(self, optionType, underlyingPrice, strike, rate, underlyingVol, timeToExpiry):
        
        self.optionType = optionType
        self.underlyingPrice = underlyingPrice
        self.strike - strike
        self.rate = rate
        self.underlyingVol = underlyingVol
        self.timeToExpiry = timeToExpiry
        
        # Call price calculation methods as per option type
        if(optionType == "call"):
            self.price = self.callOption(underlyingPrice, strike, rate, underlyingVol, timeToExpiry)
        elif(optionType == "put"):
            self.price = self.putOption(underlyingPrice, strike, rate, underlyingVol, timeToExpiry)
        else:
            print("Invalid Option Type")
        
    def callOption():
        print("Call Option")
        
    def putOption():
        print("put option")