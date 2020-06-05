#include <string>
#ifndef __strategy_h
#define __strategy_h

using namespace std;

class Strategy {

    public:
        
        Strategy (double cc, double cd, double dc, double dd, double init); 

        Strategy(const Strategy&);

        double CC;
        double CD;
        double DC;
        double DD;
        double initial;
        string strat;
};
#endif
