#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:45:49 2019

@author: rajdua
"""



import axelrod as axl
import numpy as np

# 1 Defector, 9 cooperators, no selection (w=1)

players = (axl.Cooperator(), axl.Defector(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), 
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator())
winners = []
for i in range(1,101):
    mp = axl.MoranProcess(players, turns=1)
    populations = mp.play()
    a = mp.winning_strategy_name
    winners.append(a)
    
from collections import Counter
Counter(winners)

# Add a selction parameter (w = 0.05)

winners2 = []
for i in range(1,101):
    w = 0.05
    fitness_transformation = lambda score: 1 - w + w * score
    mp = axl.MoranProcess(players, turns=1, fitness_transformation=fitness_transformation)
    populations = mp.play()
    a = mp.winning_strategy_name
    winners2.append(a)
    
from collections import Counter
Counter(winners2)





players = (axl.Cooperator(), axl.Defector(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), 
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator())
winners3 = []
for i in range(1,101):
    mp = axl.MoranProcess(players, turns=1)
    populations = mp.play()
    a = mp.winning_strategy_name
    winners3.append(a)
    
from collections import Counter
Counter(winners3)

# Add a selction parameter (w = 0.05)

winners4 = []
for i in range(1,101):
    w = 0.05
    fitness_transformation = lambda score: 1 - w + w * score
    mp = axl.MoranProcess(players, turns=1, fitness_transformation=fitness_transformation)
    populations = mp.play()
    a = mp.winning_strategy_name
    winners4.append(a)
    
from collections import Counter
Counter(winners4)







import axelrod as axl
from collections import Counter
Counter(winners4)


# 1 Defector, 9 cooperators, no selection (w=1)

players = (axl.Cooperator(), axl.Defector(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), 
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator())

winner_rows = []

ranger = np.linspace(0,1,100,endpoint=True)
for w in ranger:
    winner = []
    for i in range(1,101):
        fitness_transformation = lambda score: 1 - w + w * score
        mp = axl.MoranProcess(players, turns=1, fitness_transformation=fitness_transformation)
        populations = mp.play()
        a = mp.winning_strategy_name
        winner.append(a)
    c = Counter(winner)
    count  = c['Defector']
    percent = count /  100
    winner_rows.append(percent)
    print (w)
    
    
import matplotlib.pyplot as plt

plt.plot(ranger, winner_rows)
plt.xlabel("w")
plt.ylabel("fixation probability")
    
   


    
    

    