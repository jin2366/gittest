# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:51:03 2020

@author: 81909
"""
import pandas as pd

df_population_data = pd.read_csv('data.csv',encoding='shift-jis')

df_population_data.describe().round(0)




