# -*- coding: utf-8 -*-
"""
Pricing options through Black Scholes Merton Model

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
        elif(self.option_type == "put"):
            price = self.put_price()
        else:
            return "Error: Invalid option type"
        
        return price
    
    
    def call_price(self):
           
        # Compute d1
        d1 = self.get_d1()
        # Compute d2
        d2 = self.get_d2()
        # Lookup N(d1)
        nd1 = norm.cdf(d1)
        # Lookup N(d2)
        nd2 = norm.cdf(d2)
        
        # Calc call option price
        price = (self.underlying_price * nd1) - (self.option_strike * math.exp(-self.riskfree_rate *  self.time_to_expiry) * nd2)
        
        return price
    
    
    def put_price(self):
        
       # Compute d1
        d1 = self.get_d1()
        # Compute d2
        d2 = self.get_d2()
        # Lookup N(d1)
        nd1 = norm.cdf(-d1)
        # Lookup N(d2)
        nd2 = norm.cdf(-d2)
        
        # Calc put option price
        price = (self.option_strike * math.exp(-self.riskfree_rate *  self.time_to_expiry) * nd2) - (self.underlying_price * nd1) 
        
        return price
        
    
    def get_d1(self):
        self.d1 = (math.log(self.underlying_price / self.option_strike) + ((self.riskfree_rate + (pow(self.underlying_vol, 2) / 2)) * self.time_to_expiry)) / (self.underlying_vol * math.sqrt(self.time_to_expiry))
        return self.d1
    
    
    def get_d2(self):
        
        try:
            self.d2 = self.d1 - (self.underlying_vol * math.sqrt(self.time_to_expiry))
        except AttributeError:
            self.get_d1()
            self.get_d2()
            
        return self.d2



