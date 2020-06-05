# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import axelrod as axl
players = (axl.Cooperator(), axl.Alternator())
match = axl.Match(players, 5)
match.play()


match = axl.Match(players=players, turns=5, noise=0.2)
match.play()  

match2 = axl.Match(players, 25)
match2.play()
print(match2.sparklines(c_symbol = '|', d_symbol = ''))  

print(match2.sparklines())  


players = [axl.Cooperator(), axl.Defector(), axl.TitForTat(), axl.Grudger()]
tournament = axl.Tournament(players)
results = tournament.play()
results.ranked_names
plot = axl.Plot(results)
p = plot.boxplot()

summary = results.summarise()
import pprint
pprint.pprint(summary)
results.write_summary('summary.csv')





players.append(axl.Random())
tournament2 = axl.Tournament(players)
results = tournament2.play()
plot = axl.Plot(results)
p = plot.boxplot()
p = plot.winplot()
p = plot.payoff()


import matplotlib.pyplot as plt
_, ax = plt.subplots()
title = ax.set_title('Payoff')
xlabel = ax.set_xlabel('Strategies')
p = plot.boxplot(ax=ax)