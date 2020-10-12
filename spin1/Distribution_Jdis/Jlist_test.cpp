#include <iostream>
#include <fstream>
#include <sstream>
#include <random>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <algorithm>

using namespace std;

double Distribution_Random_Variable(int model, double var, double Jdis)
{
    double value;
    switch (model)
    {
        case 10:
        {
            /// power-law
            value = pow(var, Jdis);
            break;
        }
        case 20:
        {
            /// dimer-power-law
            value = exp(Jdis*var);
            break;
        }
    }
    return value;
}

int main()
{
    double Jdis = 0.1; //= delta
    double dimer = 0.5;
    int delta = Jdis * 10;
    int L = 10000;
    uniform_real_distribution<double> Dist_J(nextafter(0.0, 1.0), 1.0);
    mt19937 genFixed(1);
    vector<double> J_list; 
    
    for (int i = 0; i < L; i++)
    {
        double jvar = Dist_J(genFixed); // all values are same prob (0 to 1).
        jvar = (1 + dimer*pow(-1,i+1)) * Distribution_Random_Variable(10, jvar, Jdis);
        //jvar = jvar * (1 + dimer*pow(-1,i+1)) * Distribution_Random_Variable(20, jvar, Jdis);
        J_list.push_back(jvar);
    }

    // creat file to save J_list
    string file;
    file = "./J"+ to_string(delta) +"_list.csv";
    ofstream fout(file);              // == fout.open(file);
    if (!fout)
    {
        ostringstream err;
        err << "Error: Fail to save (maybe need mkdir " << file << ")";
        throw runtime_error(err.str());
    }
    fout << "J" << endl;
    for (int i = 0; i < J_list.size(); i++)
    {
        fout << J_list[i] << endl;
    }

    return 0;
}