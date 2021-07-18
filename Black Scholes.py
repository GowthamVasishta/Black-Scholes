# -*- coding: utf-8 -*-
"""
Black Scholes Formula

@Created: Sat Jul 17 20:07:21 2021
@author: Gowtham
"""

import math
from scipy.stats import norm

class Option:
    
    def __init__(self, option_type, underlying_price, option_strike, riskfree_rate, underlying_vol, time_to_expiry):
        
        # Instance attributes
        self.option_type = option_type
        self.underlying_price = underlying_price
        self.option_strike = option_strike
        self.riskfree_rate = riskfree_rate
        self.underlying_vol = underlying_vol
        self.time_to_expiry = time_to_expiry
        
        
    def price(self):
        
        if(self.option_type == "call"):
            
           price = self.call_price()
        
        elif(self.option_type == "Put"):
            
           price = self.put_price()
        
        else:
            return "Error: Invalid option type"
        
        return price
    
    
    
    def call_price(self):
        
        # Compute d1
        d1 = (math.log(self.underlying_price / self.option_strike) + (((self.riskfree_rate + pow(self.underlying_vol, 2))/2) * self.time_to_expiry)) / (self.underlying_vol * math.sqrt(self.time_to_expiry)) 
        
        # Compute d2
        d2 = d1 - (self.underlying_vol * math.sqrt(self.time_to_expiry))
        
        # Lookup N(d1)
        nd1 = norm.cdf(d1)
        
        # Lookup N(d2)
        nd2 = norm.cdf(d2)
        
        # Calc call option price
        price = (self.underlying_price * nd1) - (self.option_strike * math.exp(-self.riskfree_rate *  self.time_to_expiry) * nd2)
        
        return price
    
    
    
    def put_price(self):
        
        # Compute d1
        d1 = (math.log(self.underlying_price / self.option_strike) + (((self.riskfree_rate + pow(self.underlying_vol, 2))/2) * self.time_to_expiry)) / (self.underlying_vol * math.sqrt(self.time_to_expiry)) 
        
        # Compute d2
        d2 = d1 - (self.underlying_vol * math.sqrt(self.time_to_expiry))
        
        # Lookup N(d1)
        nd1 = norm.cdf(d1)
        
        # Lookup N(d2)
        nd2 = norm.cdf(d2)
        
        # Calc call option price
        price = (self.underlying_price * nd1) - (self.option_strike * math.exp(-self.riskfree_rate *  self.time_to_expiry) * nd2)
        
        return price
        
        
option = Option("call", 125.94, 125, 0.0446, 0.83, 0.0959)
price = option.price()
print(price)
