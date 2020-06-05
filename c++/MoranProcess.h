#include <string>
#include "Strategy.h"
#include <vector>

#ifndef __moranprocess_h
#define __moranprocess_h

using namespace std;

class MoranProcess {
 public:

  MoranProcess(vector <Strategy> types);

  MoranProcess(vector <Strategy> types, int rounds_input, double w_input, int m);

  ~MoranProcess();

  void play();
    
  void game (Strategy type1, Strategy type2, int* scores);

  bool checkDone(vector <Strategy> strat_int);

  void playGame(vector <Strategy> strat_int, int* scorer);

  int ChooseBaby(int* resultants, int height);

  vector <Strategy> getResults();

  void print();


 private:
    int rounds;
    vector <Strategy> strategies;
    int w;
    int mutation;
};
#endif
