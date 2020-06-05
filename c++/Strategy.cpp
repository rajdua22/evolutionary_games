#include "Strategy.h"

using namespace std;

Strategy::Strategy (double cc, double cd, double dc, double dd, double init)
{
    CC = cc;
    CD = cd;
    DC = dc;
    DD = dd;
    initial = init;
}

Strategy::Strategy (const Strategy& old_strat)
{
    CC = old_strat.CC;
    CD = old_strat.CD;
    DC = old_strat.DC;
    DD = old_strat.DD;
    initial = old_strat.initial;
    strat = old_strat.strat;
}

