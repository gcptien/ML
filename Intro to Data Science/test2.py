#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:04:15 2018

@author: gcptien
"""
import pandas as pd
import numpy as np
sport = {'Basketball':'USA',
         'Soccer':'Brazil',
         'Rugby':'England',
         'Baseball':'Taiwan',
         'Archery':None};
a = pd.Series(sport)

sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)

y = pd.Series([100.00, 120.00, 101.00, 3.00])

sum = np.sum(y)
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()