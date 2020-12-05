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

void tSDRG_XXZ(int L, int chi, int Pdis, double Jdis, string BC, double S, double Jz, double h, int Jseed)
{
    random_device rd;            // non-deterministic generator.
    mt19937 genRandom(rd() );    // use mersenne twister and seed is rd.
    mt19937 genFixed(Jseed);     // use mersenne twister and seed is fixed!

    uniform_real_distribution<double> Dist_J(nextafter(0.0, 1.0), 1.0); // probability distribution of J rand(0^+ ~ 1)
    
    double dim = 0; // dimerization 
    string dis;
    double sop;
    
    /// create coupling list and MPO chain for OBC or PBC
    vector<double> J_list;
    if (BC == "PBC")
    {
        for(int i=0; i<L; i++)
        {
            double jvar = Dist_J(genFixed);
            jvar = (1 + dim * pow(-1,i+1)) * Distribution_Random_Variable(Pdis, jvar, Jdis);
            J_list.push_back(jvar);
        }
    }    
    else if (BC == "OBC")
    {
        for(int i=0; i<L-1; i++)
        {
            double jvar = Dist_J(genFixed);
            jvar = jvar = (1 + dim * pow(-1,i+1)) * Distribution_Random_Variable(Pdis, jvar, Jdis);
            J_list.push_back(jvar);
        }

    }

    /// STEP.1: Decompose the Hamiltonian into MPO blocks
    vector<MPO> MPO_chain;
    MPO_chain = generate_MPO_chain(L, "XXZ_" + BC, S, J_list, Jz, h);


    /// return: TTN(w_up and w_loc) and energy spectrum of top tensor
    vector<uni10::UniTensor<double> > w_up;      // w_up is isometry tensor = VT
    vector<int> w_loc;                           // location of each w
    vector<double> En = J_list;                  // J_list will earse to one, and return ground energy.
    bool info = 1;                               // True; if tSDRG can not find non-zero gap, info return 0, and stop this random seed.
    bool save_RG_info = 0;                       // save gaps at RG stage 
    tSDRG(MPO_chain, En, w_up, w_loc, chi, dis, Pdis, Jseed, save_RG_info, info);

    /// create isometry of other part
    vector<uni10::UniTensor<double> > w_down;    // w_down
    uni10::UniTensor<double> kara;
    w_down.assign(L-1, kara);
    for (int i = 0; i < w_up.size(); i++)
    {
        w_down[i] = w_up[i];
        uni10::Permute(w_down[i], {-3, -1, 1}, 2, uni10::INPLACE);
    }

    /// test and watch output data
    double ZL, ZL2;
    ZL = Correlation_ZL(w_up, w_down, w_loc);
    cout << "method1 = " << ZL << endl;
    ZL2 = Correlation_ZL2(w_up, w_down, w_loc);
    cout << "method2 = " << ZL2 << endl;
}

void errMsg(char *arg) 
{
    cerr << "Usage: " << arg << " [options]" << endl;
    cerr << "Need 8-parameter:" << endl;
    cerr << "./job.exe <system size> <keep state of RG procedure> <Prob distribution> <disorder> <algo> <seed1> <seed2>\n" << endl;
    cerr << "Example:" << endl;
    cerr << "./job.exe 32 8 10 0.1 PBC 1 1\n" << endl;
}

int main(int argc, char *argv[])
{
    int L;                      // system size
    int chi;                    // keep state of isometry
    string BC;                  // boundary condition
    int Pdis;                   // model of random variable disturbution
    double Jdis;                // J-coupling disorder strength
    int seed1;                  // random seed number in order to repeat data
    int seed2;                  // random seed number in order to repeat data
    double S      = 1.0;        // spin dimension
    double Jz     = 1.0;        // XXZ model
    double h      = 0.0;        // XXZ model

    if (argc == 8)
    {
        stringstream(argv[1]) >> L;
        stringstream(argv[2]) >> chi;
        stringstream(argv[3]) >> Pdis;
        stringstream(argv[4]) >> Jdis;
        BC = argv[5];
        stringstream(argv[6]) >> seed1;
        stringstream(argv[7]) >> seed2;
    }
    else
    {
        errMsg(argv[0]);
        return 1;
    }

    for (int Jseed=seed1; Jseed<=seed2; Jseed++)
    {
        tSDRG_XXZ(L, chi, Pdis, Jdis, BC, S, Jz, h, Jseed);
    }

    return 0;
}