# -*- coding: utf-8 -*-
"""SB2527 Percolation 1-D, Run.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zlw9xt9XB2ML9sKUFft46sR7n6umd0x_
"""

#this cell generates data
chain_ls,chain_ps_arrays, chain_stats = Canonical_Simulation(chain_runs = 50, chain_ls = [10, 100], number_of_ps = 100) #1000, 10000