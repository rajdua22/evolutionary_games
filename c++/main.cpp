#include "MoranProcess.h"
#include <string>
#include <vector>
#include <utility>
#include <iostream>
#include "Strategy.h"
#include <string>
#include "Strategy.h"
#include "Types.h"
#include <stdlib.h>     /* srand, rand */
#include <time.h>



using namespace std;

int main(int argc, char* argv[])
{
    
    srand (time(NULL));
    int rounds = 30;
    int cooperators = 20;
    int defectors = 1;
    int tit_for_tats = 80;
    vector <Strategy> strats;
    double w = 1;

    // NEEd to fix w.
    
    // NEED TO IMPLEMENT MUTATION
    int mutation = 0;

    for (int i = 0; i < cooperators; i ++)
    {
        Cooperator type1;
        strats.push_back(type1);
    }

    for (int i = 0; i < defectors; i ++)
    {
        Defector type1;
        strats.push_back(type1);
    }

    for (int i = 0; i < tit_for_tats; i ++)
    {
        TFT type1;
        strats.push_back(type1);
    }

    MoranProcess money = MoranProcess(strats, rounds, w, mutation);
    money.play();
    vector <Strategy> winners = money.getResults();

}

