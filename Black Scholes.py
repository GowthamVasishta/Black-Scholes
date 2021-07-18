# -*- coding: utf-8 -*-
"""
Black Scholes Formula

@Created: Sat Jul 17 20:07:21 2021
@author: Gowtham
"""

import math
from scipy.stats import norm

class Option:
    
    def __init__(self, optionType, underlyingPrice, strike, rate, underlyingVol, timeToExpiry):
        
        # Instance attributes
        self.optionType = optionType
        self.underlyingPrice = underlyingPrice
        self.strike = strike
        self.rate = rate
        self.underlyingVol = underlyingVol
        self.timeToExpiry = timeToExpiry
        
        
        # # Call price calculation methods as per option type
        # if(optionType == "call"):
        #     self.price = self.callPrice()
        # elif(optionType == "put"):
        #     self.price = self.putPrice()
        # else:
        #     print("Invalid Option Type")
        
        
        
        
    def Price(self):
        
        if(self.optionType == "call"):
            
            # Compute d1
            d1 = (math.log(self.underlyingPrice / self.strike) + (((self.rate + pow(self.underlyingVol, 2))/2) * self.timeToExpiry)) / (self.underlyingVol * math.sqrt(self.timeToExpiry)) 
            
            # Compute d2
            d2 = d1 - (self.underlyingVol * math.sqrt(self.timeToExpiry))
            
            # Lookup N(d1)
            nd1 = norm.cdf(d1)
            
            # Lookup N(d2)
            nd2 = norm.cdf(d2)
            
            # Calc call option price
            price = (self.underlyingPrice * nd1) - (self.strike * math.exp(-self.rate *  self.timeToExpiry) * nd2)
            
            return price
        
        elif(self.optionType == "Put"):
            
            return 0
        
        else:
            return False
        
    
    def putOption():
        print("put option")
        
        
option = Option("call", 125.94, 125, 0.0446, 0.83, 0.0959)
price = option.Price()
print(price)
