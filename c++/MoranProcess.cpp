#include "MoranProcess.h"
#include <string>
#include <vector>
#include <utility>
#include <iostream>
#include <stdlib.h>     /* srand, rand */
#include <time.h>

MoranProcess::MoranProcess(vector <Strategy> types)
{
    rounds = 1;
    strategies = types;
    w = 1;
    mutation = 0;

}

MoranProcess::MoranProcess(vector <Strategy> types, int rounds_input, double w_input, int m)
{
    rounds = rounds_input;
    strategies = types;
    w = w_input;
    mutation  = m;
}

MoranProcess::~MoranProcess() {}

void MoranProcess::play()
{
    bool done = checkDone(strategies);
    int height  = strategies.size();
    int generation = 1;
    cout << "Generation" << generation << endl;
    print();
    cout << endl;
    

    while (!done)
    {
        generation ++;
        int* scorer = new int [height];
        playGame(strategies, scorer);
        /* for (int i = 0; i < height; i ++)
        {
            cout << scorer[i] << endl;
        } */

        int chosenOne = ChooseBaby(scorer, height);
        // cout << chosenOne << endl;

        // choose death
        int death = rand() % height;
        Strategy copy = Strategy(strategies[chosenOne]);
        strategies.at(death) = copy;

        done = checkDone(strategies);
        cout << "Generation" << generation << endl;
        print();
        cout << endl;
    }

}


void MoranProcess::game(Strategy strat1, Strategy strat2, int* scores)
{

    bool p1 = (rand() % 100) < (strat1.initial * 100);
    bool p2 = (rand() % 100) < (strat2.initial * 100);

    bool state1 = p1 & p2;
    bool state2 = p1 & !p2;
    bool state3 = p2 & !p1;
    bool state4 = !p1 & !p2;


    if (state1)
    {
        scores[0] += 3;
        scores[1] += 3;
    }

    if (state2)
    {
        scores[0] += 0;
        scores[1] += 5;
    }

    if (state3)
    {
        scores[0] += 5;
        scores[1] += 0;
    }

    if (state4)
    {
        scores[0] += 1;
        scores[1] += 1;
    }

    for (int i = 2; i <= rounds; i++)
    {

        if (state1)
        {
            p1 = (rand() % 100) < (strat1.CC * 100);
            p2 = (rand() % 100) < (strat2.CC * 100);
        }

        if (state2)
        {
            p1 = (rand() % 100) < (strat1.CD * 100);
            p2 = (rand() % 100) < (strat2.DC* 100);
        }

        if (state3)
        {
            p1 = (rand() % 100) < (strat1.DC * 100);
            p2 = (rand() % 100) < (strat2.CD * 100);
        }

        if (state4)
        {
            p1 = (rand() % 100) < (strat1.DD * 100);
            p2 = (rand() % 100) < (strat2.DD * 100);
        }

        state1 = p1 & p2;
        state2 = p1 & !p2;
        state3 = p2 & !p1;
        state4 = !p1 & !p2;

        if (state1)
        {
            scores[0] += 3;
            scores[1] += 3;
        }

        if (state2)
        {
            scores[0] += 0;
            scores[1] += 5;
        }

        if (state3)
        {
            scores[0] += 5;
            scores[1] += 0;
        }

        if (state4)
        {
            scores[0] += 1;
            scores[1] += 1;
        }
    }

    scores[0] /= rounds;
    scores[1] /= rounds;
}


bool MoranProcess::checkDone(vector <Strategy> strat_int) 
{
    string word = strat_int[0].strat;

    for (auto & element : strat_int) 
    {
        if (element.strat != word)
        {
            return false;
        }
    }

    return true;
}

 void MoranProcess::playGame(vector <Strategy> strat_int, int* scorer)
 {
     for (int i = 0; i < strat_int.size(); i ++)
        {
            scorer[i] = 0;
        }

     for (int i = 0; i < strat_int.size(); i++)
     {
         for (int j = i+1; j < strat_int.size(); j++)
         {
             Strategy strat1 = strat_int[i];
             Strategy strat2 = strat_int[j];
             int* scores  = new int [2];
             scores[0] = 0;
             scores[1] = 0;
             game(strat1, strat2, scores);
             // cout << strat1.strat << ": " << scores[0] << strat2.strat << ": " << scores[1] << endl;
             scorer[i] += scores[0];
             scorer[j] += scores[1];
         }
     }

     for (int i = 0; i < strat_int.size(); i ++)
        {
            scorer[i] = (int) (1 - w + (w * scorer[i]));
        }
 }


int MoranProcess::ChooseBaby(int* resultants, int height)
{
    int total = 0;
    for (int i = 0; i < height; i++)
    {
        total += resultants[i];
    }

    int reproduce = rand() % total;

    int prevTotal = 0;
    for (int i = 0; i < height; i ++)
    {
        prevTotal += resultants[i];
        if (reproduce < prevTotal)
        {
            return i;
        }
    }

    return -1;
}

vector <Strategy> MoranProcess::getResults()
{
    return strategies;
}

void MoranProcess::print()
{
    for (auto it = strategies.begin(); it != strategies.end(); ++it)
    {
        cout << it->strat << endl;
    }

}


