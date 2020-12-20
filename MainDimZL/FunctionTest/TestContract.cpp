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

using namespace std;

int main()
{
    uni10::UniTensor<double> temp;
    uni10::Bond bdi = spin_bond(1, uni10::BD_IN);
    uni10::Bond bdo = spin_bond(1, uni10::BD_OUT);
    vector<uni10::Bond> bonds = {bdi, bdo};
    uni10::UniTensor<double> tempL(bonds);
    uni10::UniTensor<double> tempR(bonds);
    tempL.PutBlock(matSz(1));
    tempR.PutBlock(matiSy(1));
    tempL.SetLabel({1, 2});   
    tempR.SetLabel({2, 3});  
    temp = uni10::Contract(tempL, tempR);
    cout << "Sz-Sy=" << temp << endl;
    return 0;
}