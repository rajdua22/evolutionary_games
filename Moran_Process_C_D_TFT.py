#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 03:09:39 2019

@author: rajdua
"""


import axelrod as axl
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt



# 1 Defector, 19 cooperators, varying w

players = (axl.Cooperator(), axl.Defector(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), 
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator())

winner_rows = []
ranger = np.linspace(0,1,50,endpoint=True)
for w in ranger:
    winner = []
    for i in range(1,51):
        fitness_transformation = lambda score: 1 - w + w * score
        mp = axl.MoranProcess(players, turns=1, fitness_transformation=fitness_transformation)
        populations = mp.play()
        a = mp.winning_strategy_name
        winner.append(a)
    c = Counter(winner)
    count  = c['Defector']
    percent = count /  50
    winner_rows.append(percent)
    print (w)

plt.plot(ranger, winner_rows)
plt.xlabel("w")
plt.ylabel("fixation probability")


players = (axl.Cooperator(), axl.TitForTat(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), 
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator())

w = 0.05
fitness_transformation = lambda score: 1 - w + w * score
mp = axl.MoranProcess(players, turns=10, fitness_transformation=fitness_transformation)
populations = mp.play()
ax = mp.populations_plot()

winner_rows = []
ranger = np.linspace(0,1,20,endpoint=True)
for w in ranger:
    winner = []
    for i in range(1,10):
        fitness_transformation = lambda score: 1 - w + w * score
        mp = axl.MoranProcess(players, turns=50, fitness_transformation=fitness_transformation)
        populations = mp.play()
        a = mp.winning_strategy_name
        winner.append(a)
    c = Counter(winner)
    count  = c['TitForTat']
    percent = count /  10
    winner_rows.append(percent)
    print (w)

plt.plot(ranger, winner_rows)
plt.xlabel("w")
plt.ylabel("fixation probability")





players = (axl.Cooperator(), axl.TitForTat(), axl.TitForTat(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), 
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator())

winner_rows = []
ranger = np.linspace(0,1,20,endpoint=True)
for w in ranger:
    winner = []
    for i in range(1,10):
        fitness_transformation = lambda score: 1 - w + w * score
        mp = axl.MoranProcess(players, turns=50, fitness_transformation=fitness_transformation)
        populations = mp.play()
        a = mp.winning_strategy_name
        winner.append(a)
    c = Counter(winner)
    count  = c['Tit For Tat']
    percent = count /  10
    winner_rows.append(percent)
    print (w)

plt.plot(ranger, winner_rows)
plt.xlabel("w")
plt.ylabel("fixation probability")





players = (axl.Cooperator(), axl.TitForTat(), axl.TitForTat(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), 
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Defector(), axl.Defector(), axl.Cooperator())

winner_rows = []
winner2_rows = []
ranger = np.linspace(0,1,20,endpoint=True)
for w in ranger:
    winner = []
    for i in range(1,10):
        fitness_transformation = lambda score: 1 - w + w * score
        mp = axl.MoranProcess(players, turns=50, fitness_transformation=fitness_transformation)
        populations = mp.play()
        a = mp.winning_strategy_name
        winner.append(a)
    c = Counter(winner)
    count  = c['Tit For Tat']
    count2 = c['Defector']
    percent = count /  10
    percent2 = count2 / 10
    winner_rows.append(percent)
    winner2_rows.append(percent2)
    print (w)

plt.plot(ranger, winner_rows)
plt.xlabel("w")
plt.ylabel("fixation probability")





players = (axl.Cooperator(), axl.TitForTat(), axl.TitForTat(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), 
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Defector(), axl.Defector(),  axl.Cooperator())

winner_rows = []
winner2_rows = []
w = 0.05
fitness_transformation = lambda score: 1 - w + w * score
for m in range(1,21):
    winner = []
    for i in range(1,20):
        mp = axl.MoranProcess(players, turns=m, fitness_transformation=fitness_transformation)
        populations = mp.play()
        a = mp.winning_strategy_name
        winner.append(a)
    c = Counter(winner)
    count  = c['Tit For Tat']
    count2 = c['Defector']
    percent = count /  20
    percent2 = count2 / 20
    winner_rows.append(percent)
    winner2_rows.append(percent2)
    print (m)

winner3 = [1 - i - j for (i,j) in zip(winner_rows, winner2_rows)]
plt.plot(range(1,21), winner_rows)
plt.plot(range(1,21), winner2_rows)
plt.plot(range(1,21), winner3)
plt.xlabel("m")
plt.ylabel("Winning probability")





players = (axl.Cooperator(), axl.TitForTat(), axl.TitForTat(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), 
           axl.Cooperator(), axl.TitForTat(), axl.TitForTat(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Defector(), axl.Defector(), axl.Cooperator(), axl.Cooperator(),
           axl.Cooperator(), axl.Defector(), axl.Defector(),  axl.Cooperator())

winner_rows = []
winner2_rows = []
ranger = np.linspace(0,1,20,endpoint=True)
for w in ranger:
    winner = []
    for i in range(1,20):
        fitness_transformation = lambda score: 1 - w + w * score
        mp = axl.MoranProcess(players, turns=50, fitness_transformation=fitness_transformation)
        populations = mp.play()
        a = mp.winning_strategy_name
        winner.append(a)
    c = Counter(winner)
    count  = c['Tit For Tat']
    count2 = c['Defector']
    percent = count /  20
    percent2 = count2 / 20
    winner_rows.append(percent)
    winner2_rows.append(percent2)
    print (w)

winner3 = [1 - i - j for (i,j) in zip(winner_rows, winner2_rows)]
plt.plot(ranger, winner_rows)
plt.plot(ranger, winner2_rows)
plt.plot(ranger, winner3)
plt.xlabel("w")
plt.ylabel("fixation probability")






players = (axl.TitForTat(), axl.Defector(), axl.Defector(), axl.Defector(), axl.Defector(),
            axl.Defector(), axl.Defector(), axl.Defector(), axl.Defector(), axl.Defector())

winner_rows = []
winner2_rows = []
w = 0.05
fitness_transformation = lambda score: 1 - w + w * score
for m in range(1,51):
    winner = []
    for i in range(1,50):
        mp = axl.MoranProcess(players, turns=m, fitness_transformation=fitness_transformation)
        populations = mp.play()
        a = mp.winning_strategy_name
        winner.append(a)
    c = Counter(winner)
    count  = c['Tit For Tat']
    count2 = c['Defector']
    percent = count /  50
    percent2 = count2 / 50
    winner_rows.append(percent)
    winner2_rows.append(percent2)
    print (m)

plt.plot(range(1,51), winner_rows)
plt.plot(range(1,51), winner2_rows)
plt.xlabel("m")
plt.ylabel("Winning probability")





players = (axl.TitForTat(), axl.TitForTat(), axl.TitForTat(), axl.TitForTat(), axl.TitForTat(), axl.Defector(),
           axl.TitForTat(), axl.TitForTat(), axl.TitForTat(), axl.TitForTat())

winner_rows = []
winner2_rows = []
w = 0.05
fitness_transformation = lambda score: 1 - w + w * score
for m in range(1,51):
    winner = []
    for i in range(1,50):
        mp = axl.MoranProcess(players, turns=m, fitness_transformation=fitness_transformation)
        populations = mp.play()
        a = mp.winning_strategy_name
        winner.append(a)
    c = Counter(winner)
    count  = c['Tit For Tat']
    count2 = c['Defector']
    percent = count /  50
    percent2 = count2 / 50
    winner_rows.append(percent)
    winner2_rows.append(percent2)
    print (m)

plt.plot(range(1,51), winner_rows)
plt.plot(range(1,51), winner2_rows)
plt.xlabel("m")
plt.ylabel("Winning probability")





players = (axl.TitForTat(), axl.TitForTat(), axl.TitForTat(), axl.TitForTat(), axl.TitForTat(), axl.Defector(),
           axl.TitForTat(), axl.TitForTat(), axl.TitForTat(), axl.TitForTat())

winner_rows = []
winner2_rows = []
ranger = np.linspace(0,1,20,endpoint=True)
for w in ranger:
    winner = []
    for i in range(1,51):
        fitness_transformation = lambda score: 1 - w + w * score
        mp = axl.MoranProcess(players, turns=50, fitness_transformation=fitness_transformation)
        populations = mp.play()
        a = mp.winning_strategy_name
        winner.append(a)
    c = Counter(winner)
    count  = c['Tit For Tat']
    count2 = c['Defector']
    percent = count /  50
    percent2 = count2 / 50
    winner_rows.append(percent)
    winner2_rows.append(percent2)
    print (w)

plt.plot(ranger, winner_rows)
plt.plot(ranger, winner2_rows)
plt.xlabel("w")
plt.ylabel("Winning probability")





players = (axl.TitForTat(), axl.Defector(), axl.Defector(), axl.Defector(), axl.Defector(),
            axl.Defector(), axl.Defector(), axl.Defector(), axl.Defector(), axl.Defector())

winner_rows = []
winner2_rows = []
ranger = np.linspace(0,1,20,endpoint=True)
for w in ranger:
    winner = []
    for i in range(1,51):
        fitness_transformation = lambda score: 1 - w + w * score
        mp = axl.MoranProcess(players, turns=50, fitness_transformation=fitness_transformation)
        populations = mp.play()
        a = mp.winning_strategy_name
        winner.append(a)
    c = Counter(winner)
    count  = c['Tit For Tat']
    count2 = c['Defector']
    percent = count /  50
    percent2 = count2 / 50
    winner_rows.append(percent)
    winner2_rows.append(percent2)
    print (w)

plt.plot(ranger, winner_rows)
plt.plot(ranger, winner2_rows)
plt.xlabel("w")
plt.ylabel("Winning probability")




