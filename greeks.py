# -*- coding: utf-8 -*-
"""
Compute option greeks

@Created: Wed Jul 21 00:03:19 2021
@author: Gowtham
"""

import sys

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
        
    
    
option = Greeks("put", 125.94, 125, 0.0446, 0.83, 0.0959)
delta = option.get_delta()
print(delta)
