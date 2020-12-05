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
    double Dim = 0;
    random_device rd;            // non-deterministic generator.
    mt19937 genRandom(rd() );    // use mersenne twister and seed is rd.
    mt19937 genFixed(1);     // use mersenne twister and seed is fixed!

    uniform_real_distribution<double> Dist_J(nextafter(0.0, 1.0), 1.0); // probability distribution of J rand(0^+ ~ 1)
    /// loading Network file
    uni10::Network H12("../tSDRG_net/H12.net");

    /// create coupling list and MPO chain for OBC or PBC
    vector<double> J_list;
    for(int i=0; i<3; i++)
    {
        double jvar = Dist_J(genFixed);
        jvar = (1 + Dim * pow(-1,i+1)) * Distribution_Random_Variable(10, jvar, 0);
        J_list.push_back(jvar);
    }

    /// Decompose the Hamiltonian into MPO blocks
    vector<MPO> MPO_chain;
    MPO_chain = generate_MPO_chain(3, "XXZ_PBC", 1, J_list, 1, 0);

    uni10::UniTensor<double> H_last, H1, H2;
    /// 1 and 0; use special tools GetTensorPBC for getting real term
    H1 = MPO_chain[1].GetTensorPBC('l');
    H2 = MPO_chain[0].GetTensorPBC('r');
    H12.PutTensor("H1", H1);
    H12.PutTensor("H2", H2);
    H12.Launch(H_last);
    //cout << "H_last = " << H_last << endl;
    uni10::Permute(H_last, {-3, -1, -4, -2}, 2, uni10::INPLACE);
    //cout << "H_last_permute = " << H_last << endl;

    /// Contract any two site hamitonian in order to find highest gap
    uni10::UniTensor<double> H, H3, H4;             // H is hamitonian of site-1(= H1) and site-2(= H2)  
    H3 = MPO_chain[0].GetTensor('l');
    H4 = MPO_chain[1].GetTensor('r');    
    H12.PutTensor("H1", H3);
    H12.PutTensor("H2", H4);
    H12.Launch(H);
    //cout << "H = " << H << endl;

    cout << MPO_chain[0].GetTensor('l') << endl;cout << H3 << endl;

    /// diagonal local hamitonian
    uni10::Matrix<double> M, En, En2;                               // eigen energy
    uni10::Matrix<double> state, state2;                            // eigen state
    uni10::Matrix<double> H_block;
    H_block = H.GetBlock() + H_last.GetBlock();
    uni10::EigH(H_block, En, state, uni10::INPLACE);
    //cout << H_block << endl;cout << En << endl;

    /*uni10_double64 mat_elem[] = {\
    2.0, 1.0,\
    1.0, 2.0};
    M = uni10::Matrix<uni10_double64>(2, 2, mat_elem);
    uni10::EigH(M, En2, state2, uni10::INPLACE);
    cout << M << endl;cout << En2 << endl;cout << state2 << endl;*/

    /// Define the energy gap in the spectrum and truncation system
    int chi_loc = H.GetBlock().col();
    bool info = 1;  
    Truncation(En, state, 9, chi_loc, info); 
    //cout << "state = "<< state << endl;
    return 0;
}