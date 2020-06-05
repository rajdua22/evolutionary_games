#include "Strategy.h"
#include <string>
#include "Types.h"


Cooperator::Cooperator() : 
Strategy (1, 1, 1, 1, 1)
{
    strat = "copperator";
}


Defector::Defector() :
Strategy(0, 0, 0, 0, 0)
{
    strat = "defector";
}

TFT::TFT() : 
Strategy(0, 1, 0, 1, 1)
{
    strat = "tft";
}