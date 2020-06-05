CXX=g++
CXXFLAGS=-g -Wall -std=c++11
# Uncomment for parser DEBUG
#DEFS=-DDEBUG

OBJS=main.o MoranProcess.o Strategy.o Types.o

all: main

main: $(OBJS)
	$(CXX) $(CXXFLAGS) $(DEFS) -o $@ $(OBJS)

main.o: main.cpp MoranProcess.h Strategy.h Types.h 
	$(CXX) $(CXXFLAGS) $(DEFS) -o $@ -c main.cpp
MoranProcess.o: MoranProcess.cpp MoranProcess.h Strategy.h Types.h
	$(CXX) $(CXXFLAGS) $(DEFS) -o $@ -c MoranProcess.cpp
Strategy.o: Strategy.cpp Strategy.h Types.h
	$(CXX) $(CXXFLAGS) $(DEFS) -o $@ -c Strategy.cpp
Types.o: Types.cpp Types.h 
	$(CXX) $(CXXFLAGS) $(DEFS) -o $@ -c Types.cpp

clean:
	rm -f *.o main