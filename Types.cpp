#include <vector>
#include <iostream>

class Type {
    int type;
    std::vector<double> fight_chances;
    int locx;
    int locy;
    int level;
  public:
    Type(int typer);
    void set_type(int type_name);
    int get_type();
    void set_fight_chance (int type_passed, double fight_chance);
    double get_fight_chance (int type_passed);
    void setlocx (int locationx);
    void setlocy (int locationy);
    int getlocx ();
    int getlocy();
    int getlevel();
    void setlevel(int level);
    int move(bool world[100][100][3]);
};

Type::Type (int typer)
{
    type = typer;
    level = 0;
}

void Type::set_type(int type_name)
{
    type = type_name;
}

int Type::get_type()
{
    return type;
}

void Type::set_fight_chance (int type_passed, double fight_chance)
{
    int num_types = fight_chances.size();
    if (type_passed > num_types)
    {
        std::cout << "Error: trying to add type that doesn't exist.";
        return;
    }

    if (type_passed  == num_types)
    {
        fight_chances.push_back(fight_chance);
        return;
    }

    if (type_passed < num_types)
    {
        auto itPos = fight_chances.begin() + type;
        fight_chances.insert(itPos, fight_chance);
        return;
    }
}

double Type::get_fight_chance(int type_passed)
{
    return fight_chances[type_passed];
}

void Type::setlocx(int locationx)
{
    locx = locationx;
}

void Type::setlocy(int locationy)
{
    locy = locationy;
}

int Type::getlocx()
{
    return locx;
}

int Type::getlocy()
{
    return locy;
}

int Type::getlevel()
{
    return level;
}

void Type::setlevel(int level2)
{
    level = level2;
}

int Type::move(bool world[100][100][3])
{
    int moved = false;

    while (!moved)
    {
        int choice = rand() % 4;
        if (choice == 0)
        {
            if (locx != 0)
            {
                if (world[locx-1][locy][0] == false)
                {
                    locx--;
                    moved = true;
                    level = 0;
                    return 0;
                }

                else if (world[locx-1][locy][1] == false)
                {
                    locx--;
                    moved = true;
                    level = 1;
                    return 1;
                }
            }
        }

        if (choice == 1)
        {
            if (locx != 99)
            {
                if (world[locx+1][locy][0] == false)
                {
                    locx++;
                    moved = true;
                    level = 0;
                    return 0;
                }

                else if (world[locx+1][locy][1] == false)
                {
                    locx++;
                    moved = true;
                    level = 1;
                    return 1;
                }
            }
        }

        if (choice == 2)
        {
            if (locy!= 0)
            {
                if (world[locx][locy-1][0] == false)
                {
                    locy--;
                    moved = true;
                    level = 0;
                    return 0;
                }

                else if (world[locx][locy-1][1] == false)
                {
                    locy--;
                    moved = true;
                    level = 1;
                    return 1;
                }
            }     
        }

        if (choice == 3)
        {
            if (locy != 99)
            {
                if (world[locx][locy+1][0]  == false)
                {
                    locy++;
                    moved = true;
                    level = 0;
                    return 0;
                } 

                else if (world[locx][locy+1][1] == false)
                {
                    locy++;
                    moved = true;
                    level = 1;
                    return 1;
                }
            }
        }
    }
}
