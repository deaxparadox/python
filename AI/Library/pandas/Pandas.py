#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 15:13:32 2022

@author: creator
"""

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5), index=['a','b','c','d','e'])
print(s)
print(s.index)
print(pd.Series(np.random.rand(5)))