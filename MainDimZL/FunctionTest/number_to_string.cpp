#include <iostream>
#include <fstream>
#include <sstream>
#include <random>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <uni10.hpp>
#include "../MPO/mpo.h"
#include "../tSDRG_tools/tSDRG_tools.h"
#include "../tSDRG_tools/measure.h"

using namespace std; /// create folder in order to save data

void errMsg(char *arg) 
{
    cerr << "Usage: " << arg << " [options]" << endl;
    cerr << "Need 9-parameter:" << endl;
    cerr << "./job.exe <system size> <keep state of RG procedure> <Prob distribution> <disorder> <dimerization> <algo> <seed1> <seed2>\n" << endl;
    cerr << "Example:" << endl;
    cerr << "./job.exe 32 8 10 0.1 0.1 PBC 1 1\n" << endl;
}

int main(int argc, char *argv[])
{    
    int L;                      // system size
    int chi;                    // keep state of isometry
    string BC;                  // boundary condition
    int Pdis;                   // model of random variable disturbution
    double Jdis;                // J-coupling disorder strength
    double Dim;			        // Dimerization constant
    int seed1;                  // random seed number in order to repeat data
    int seed2;                  // random seed number in order to repeat data
    double S      = 1.0;        // spin dimension
    double Jz     = 1.0;        // XXZ model
    double h      = 0.0;        // XXZ model

    if (argc == 9)
    {
        stringstream(argv[1]) >> L;
        stringstream(argv[2]) >> chi;
        stringstream(argv[3]) >> Pdis;
        stringstream(argv[4]) >> Jdis;
	    stringstream(argv[5]) >> Dim;
        BC = argv[6];
        stringstream(argv[7]) >> seed1;
        stringstream(argv[8]) >> seed2;
    }
    else
    {
        errMsg(argv[0]);
        return 1;
    }

    string dis, dim;
    if (Jdis < 1.0)
        dis = "0" + to_string( (int)(round(Jdis*100)) );
    else if (Jdis >= 1.0)
        dis = to_string( (int)(round(Jdis*100)) ); 
    if (Dim < 1.0)
        dim = "0" + to_string( (int)(round(Dim*100)) );
    else if (Dim >= 1.0)
        dim = to_string( (int)(round(Dim*100)) );
    cout << "dis = " << dis << endl;
    cout << "dim = " << dim << endl;
    return 0;
}