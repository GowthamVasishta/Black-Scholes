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
        
        
        
        
    def callOption(self, underlyingPrice, strike, rate, underlyingVol, timeToExpiry):
        
        # Compute d1
        d1 = (math.log(underlyingPrice / strike) + (((rate + pow(underlyingVol, 2))/2) * timeToExpiry)) / (underlyingVol * math.sqrt(timeToExpiry)) 
        
        # Compute d2
        d2 = d1 - (underlyingVol * math.sqrt(timeToExpiry))
        
        # Lookup N(d1)
        nd1 = norm.cdf(d1)
        
        # Lookup N(d2)
        nd2 = norm.cdf(d2)
        
        # Calc call option price
        price = (underlyingPrice * nd1) - (strike * math.exp(-rate *  timeToExpiry) * nd2)
        
        return price
        
    
    
    def putOption():
        print("put option")