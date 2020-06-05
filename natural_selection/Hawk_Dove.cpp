#include <string>
#include <vector>
#include <utility>
#include <iostream>
#include <stdlib.h>     /* srand, rand */
#include <time.h>
#include <fstream>
#include <vector>
#include "Types.cpp"
#include <time.h> 
#include <stdlib.h>

using namespace std;

Type create_hawk ()
{
    Type fighter(0);
    fighter.set_fight_chance(0,1);
    fighter.set_fight_chance(1,1);
    return fighter;
}

Type create_dove ()
{
    Type fighter(1);
    fighter.set_fight_chance(0,0);
    fighter.set_fight_chance(1,0);
    return fighter;
}


int main(int argc, char* argv[])
{

    srand(time(NULL));
    // initial paramaters
    int world_size = 100;
    int num_hawk = 10;   // type = 0
    int num_dove = 10;  // type = 1
    
    // creating populations
    vector <Type> population;
    for (int i = 0; i < num_hawk; i ++)
    {
        population.push_back(create_hawk());
    }

    for (int i = 0; i < num_dove; i ++)
    {
        population.push_back(create_dove());
    }

    int number_of_players = population.size();
    // finish creating population


    // Creating world
    bool world[100][100][3];
    for (int i = 0; i < world_size; i++)
    {
        for (int j = 0; j < world_size; j++)
        {
            for (int k = 0; k < 3; k++)
            {
                world[i][j][k] = false;
            }
        }
    }

    while (number_of_players > 0)
    {
        int num = rand() % world_size;
        int axis = rand() % 4;
        // cout << number_of_players << " " << num << " " << axis << endl;
        if (axis == 0)
        {
            if (world[0][num][0] == false)
            {
                world[0][num][0] = true;
                population[number_of_players-1].setlocx(0);
                population[number_of_players-1].setlocy(num);
                number_of_players --;
            }
        }

        if (axis == 1)
        {
            if (world[num][0][0] == false)
            {
                world[num][0][0] = true;
                population[number_of_players-1].setlocx(num);
                population[number_of_players-1].setlocy(0);
                number_of_players --;
            }
        }

        if (axis == 2)
        {
            if (world[num][world_size-1][0] == false)
            {
                world[num][world_size-1][0] = true;
                population[number_of_players-1].setlocx(num);
                population[number_of_players-1].setlocy(world_size-1);
                number_of_players --;
            }
        }

        if (axis == 3)
        {
            if (world[world_size-1][num][0] == false)
            {
                world[world_size-1][num][0] = true;
                population[number_of_players-1].setlocx(world_size-1);
                population[number_of_players-1].setlocy(num);
                number_of_players --;
            }
        }
    }
    // done with creating world


    // printing for sanity
    for (int i = 0; i < population.size(); i++)
    {
        cout << i << ": " << population[i].getlocx() << " " << population[i].getlocy() << endl;
    }

    for (int i = 0; i < world_size; i++)
    {
        for (int j = 0; j < world_size; j++)
        {
            if (world[i][j][0] == false)
            {
                cout << "_";
            }

            else
            {
                cout << "+";
            }
        }
        cout << endl;
    }
    // done printing for sanity

    number_of_players = population.size();

    int num_moves = 1000;


    for (int i = 0; i < num_moves; i ++)
    {
        cout << endl << endl << endl;
        for (int j = 0; j < number_of_players; j ++)
        {

            world[population[j].getlocx()][population[j].getlocy()][population[j].getlevel()] = false;
            int level = population[j].move(world);
            world[population[j].getlocx()][population[j].getlocy()][level] = true;
        }

        for (int i = 0; i < world_size; i++)
        {   
            for (int j = 0; j < world_size; j++)
            {
                if (world[i][j][0] == false)
                {
                    cout << "_";
                }
                else
                {
                    cout << "+";
                }
            }
            cout << endl;
        }
    }
}