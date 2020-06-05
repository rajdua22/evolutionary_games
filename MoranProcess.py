#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:26:21 2019

@author: rajdua
"""

import axelrod as axl
# axl.seed(0)  # for reproducible example
players = [axl.Cooperator(), axl.Defector(),
           axl.TitForTat(), axl.Grudger()]
mp = axl.MoranProcess(players)
populations = mp.play()
mp.winning_strategy_name
len(mp)


import pprint
pprint.pprint(populations)  
for row in mp.score_history:
    print([round(element, 1) for element in row])
    
    
    
import random
import matplotlib.pyplot as plt
# axl.seed(15)  # for reproducible example
players = [axl.Defector(), axl.Defector(), axl.Defector(),
        axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
        axl.TitForTat(), axl.TitForTat(), axl.TitForTat(),
        axl.Random()]
mp = axl.MoranProcess(players=players, turns=200)
populations = mp.play()
mp.winning_strategy_name
ax = mp.populations_plot()
plt.show()  

pprint.pprint(populations)  
for row in mp.score_history:
    print([round(element, 1) for element in row])
    
    
players = [axl.Cooperator(), axl.Defector(),
            axl.TitForTat(), axl.Grudger()]
mp = axl.MoranProcess(players, mutation_rate=0.1)
for _ in mp:
    if len(mp.population_distribution()) == 1:
        break
mp.population_distribution()




players = (axl.Cooperator(), axl.Defector(), axl.Defector(), axl.Defector(), axl.TitForTat())
w = 0.05
fitness_transformation = lambda score: 1 - w + w * score
mp = axl.MoranProcess(players, turns=10, fitness_transformation=fitness_transformation)
populations = mp.play()
ax = mp.populations_plot()
mp.winning_strategy_name


players = [s() for s in axl.basic_strategies]

for i in range(0,3):
    Newplayers = [s() for s in axl.basic_strategies]
    players.extend(Newplayers)
    

w = 0.05
fitness_transformation = lambda score: 1 - w + w * score
mp = axl.MoranProcess(players, turns=10, fitness_transformation=fitness_transformation)
populations = mp.play()
ax = mp.populations_plot()
mp.winning_strategy_name


players = (axl.Cooperator(), axl.Defector(), axl.Cooperator(), axl.Cooperator(),axl.Cooperator(), axl.Cooperator(), 
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator())
w = 0.05
fitness_transformation = lambda score: 1 - w + w * score
mp = axl.MoranProcess(players, turns=10, fitness_transformation=fitness_transformation)
populations = mp.play()
ax = mp.populations_plot()
mp.winning_strategy_name

for row in mp.score_history:
     print([round(element, 1) for element in row])


player_Coop = [axl.Cooperator()]
players.extend(player_Coop)

