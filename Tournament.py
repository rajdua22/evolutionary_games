#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:13:11 2019

@author: rajdua
"""


import axelrod as axl
players = [s() for s in axl.basic_strategies]
tournament = axl.Tournament(players)
results = tournament.play()
summary = results.summarise()
import pprint
pprint.pprint(summary)

results.write_summary('summary.csv')
import csv
with open('summary.csv', 'r') as outfile:
     csvreader = csv.reader(outfile)
     for row in csvreader:
         print(row)
         
         
plot = axl.Plot(results)
p = plot.boxplot()
p.show()

results.ranked_names


results.wins

pprint.pprint(results.payoffs)  



players = (axl.Cooperator(), axl.Defector(),axl.Cooperator(), axl.Cooperator(),axl.Cooperator(), axl.Cooperator(), 
           axl.Cooperator(), axl.Cooperator(), axl.Cooperator(), axl.Cooperator())
w = 1
tournament = axl.Tournament(players, turns = 10)
results = tournament.play()
summary = results.summarise()
import pprint
pprint.pprint(summary)

plot = axl.Plot(results)
p = plot.boxplot()
p.show()

results.ranked_names