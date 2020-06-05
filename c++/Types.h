#include <string>
#include "Strategy.h"
#ifndef __types_h
#define __types_h

using namespace std;

class Cooperator: public Strategy {

public:
    Cooperator();
};


class Defector: public Strategy {

public:
    Defector();
};

class TFT: public Strategy {

    public:
    TFT();
};

class Custom: public Strategy {
    public: 
    Custom();
};
#endif






        