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
    int spin = 1;    
    int N = 3;

    uni10::UniTensor<double> H, Sx, Sy, Sz;
    uni10::Matrix<double> M, M2, En, state, state2, s, h, h12, h23, h34, h45, h56;
    uni10::Matrix<double> sx = matSx(spin);    
    uni10::Matrix<double> sy = matiSy(spin);
    uni10::Matrix<double> sz = matSz(spin);
    uni10::Matrix<double> Id(sx.row(), sx.col(), true);
    uni10::Matrix<uni10_complex128> expS, ZL, ZL2;
    vector<uni10::Matrix<uni10_complex128>> S, mpo;
    S.assign(N*3, Id);
    mpo.assign(N, Id);
    Id.Identity();

    for(int i=0;i<3;i++)
    {
        switch(i) 
        {
            default:
                    s = sx;
                    break;
            case 1:
                    s = sy;
                    break;
            case 2:
                    s = sz;
                    break;
        }
        S[i*N+0] =  uni10::Otimes(uni10::Otimes(s, Id), Id);
        S[i*N+1] =  uni10::Otimes(uni10::Otimes(Id, s), Id);
        S[i*N+2] =  uni10::Otimes(uni10::Otimes(Id, Id), s);
    }
    h = uni10::Dot(S[0], S[1]) + (-1)*uni10::Dot(S[N], S[N+1]) + uni10::Dot(S[2*N], S[2*N+1]);
    for(int i=1;i<N-1;i++)
    {
        h += uni10::Dot(S[i], S[i+1]) + (-1)*uni10::Dot(S[i+N], S[i+N+1]) + uni10::Dot(S[i+2*N], S[i+2*N+1]);
    }

    uni10::EigH(h, En, state, uni10::INPLACE);
    uni10::Resize(state, 1, pow(3,N), uni10::INPLACE);
    state2 = uni10::Transpose(state);

    for (int i=0; i<N; i++)
    {
        int l = i+1;
        uni10_complex128 t(0, 2*M_PI*l/ N);
        expS = uni10::ExpH(t, S[N*2+i]);   //exp((2*pi*i/L)*l*Sz) 
        mpo[i] = expS;
    }

    ZL = state2;
    for(int i=N-1; i>-1; i--)
    {
        ZL = uni10::Dot(mpo[i], ZL);
    }
    ZL = uni10::Dot(state, ZL);
    //ZL2 = uni10::Dot((-1)*state,uni10::Dot(mpo[N-4],uni10::Dot(mpo[N-3],uni10::Dot(mpo[N-2],uni10::Dot(mpo[N-1], (-1)*state2)))));
    cout << ZL << endl;

    return 0;
}