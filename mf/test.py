# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 13:42:09 2017

@author: ldh
"""

# test.py
from podaci.wind import get_wss,get_wsd
from podaci.tswrapper import get_universe

universe = get_universe('sz50')
start_date = '20150101'
end_date = '20170101'

market_data = get_wsd(universe,'close',
                      start_date,end_date,True,Period = 'M',
                      PriceAdj = 'F')
monthly_return = market_data.pct_change()
monthly_return = monthly_return.iloc[1:,:].dropna(axis = 1)
universe_adj = monthly_return.columns.values.tolist()
start_date_adj = monthly_return.index[0]
end_date_adj = monthly_return.index[-1]

# create training & test sample

