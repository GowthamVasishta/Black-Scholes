# -*- coding: utf-8 -*-
"""
Compute option greeks

@Created: Wed Jul 21 00:03:19 2021
@author: Gowtham
"""

import sys
import math
from scipy.stats import norm

sys.path.append(".")

from option import Option

class Greeks(Option):
    
    def get_delta(self):
        
        if(self.option_type == "call"):
            delta = self.get_d1()
        elif(self.option_type == "put"):
            delta = (self.get_d1() - 1)
        else:
            return "Error: Invalid option type"
        
        return delta
        
    
    def get_vega(self):
        
        d1 = self.get_d1()
        vega = (self.underlying_price * math.sqrt(self.time_to_expiry) * math.exp(- pow(d1, 2) / 2)) / (math.sqrt(2 * math.pi))
        
        return vega
    
    
    def get_gamma(self):
        
        d1 = self.get_d1()
        gamma = math.exp(- pow(d1, 2) / 2) / (self.underlying_price * self.underlying_vol * math.sqrt(2 * math.pi * self.time_to_expiry))
        
        return gamma
    
    
    def get_rho(self):
        
        d2 = self.get_d2()
        nd2 = norm.cdf(d2)
        
        if(self.option_type == "call"):
            rho = self.time_to_expiry * self.option_strike *  math.exp(-self.riskfree_rate *  self.time_to_expiry) * nd2
        elif(self.option_type == "put"):
            rho = - (self.time_to_expiry * self.option_strike *  math.exp(-self.riskfree_rate *  self.time_to_expiry) * (1- nd2))
        else:
            return "Error: Invalid option type"
        
        return rho
    
    
    def get_theta(self):
        
        d1 = self.get_d1()
        d2 = self.get_d2()
        nd2 = norm.cdf(d2)
        
        a = -(self.underlying_price * self.underlying_vol * math.exp(- pow(d1, 2) / 2)) / (2 * math.sqrt(2 * math.pi * self.time_to_expiry))
    
        if(self.option_type == "call"):
            theta = a - (self.riskfree_rate * self.option_strike *  math.exp(-self.riskfree_rate *  self.time_to_expiry) * nd2)
        elif(self.option_type == "put"):
            theta = a + (self.riskfree_rate * self.option_strike *  math.exp(-self.riskfree_rate *  self.time_to_expiry) * (1- nd2))
        else:
            return "Error: Invalid option type"
        
        return theta
    
    
    
    
option = Greeks("call", 125.94, 125, 0.0446, 0.83, 0.0959)
gamma = option.get_gamma()
print(gamma)
