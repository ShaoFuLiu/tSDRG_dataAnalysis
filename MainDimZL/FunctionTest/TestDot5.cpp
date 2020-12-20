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
    int chi_loc = 1;
    int N = 5;
    bool info = 1;

    uni10::UniTensor<double> H, Sx, Sy, Sz;
    uni10::Matrix<uni10_complex128> expS, ZL, ZL2;
    uni10::Matrix<double> M, M2, En, state, state2, s, h, h12, h23, h34, h45, h56;
    uni10::Matrix<double> sx = matSx(spin);    
    uni10::Matrix<double> sy = matiSy(spin);
    uni10::Matrix<double> sz = matSz(spin);
    uni10::Matrix<double> Id(sx.row(), sx.col(), true);
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
        S[i*N+0] =  uni10::Otimes(uni10::Otimes(uni10::Otimes(uni10::Otimes(s, Id), Id), Id), Id);
        S[i*N+1] =  uni10::Otimes(uni10::Otimes(uni10::Otimes(uni10::Otimes(Id, s), Id), Id), Id);
        S[i*N+2] =  uni10::Otimes(uni10::Otimes(uni10::Otimes(uni10::Otimes(Id, Id), s), Id), Id);
        S[i*N+3] =  uni10::Otimes(uni10::Otimes(uni10::Otimes(uni10::Otimes(Id, Id), Id), s), Id);
        S[i*N+4] =  uni10::Otimes(uni10::Otimes(uni10::Otimes(uni10::Otimes(Id, Id), Id), Id), s);
        /*S[i*N+5] =  uni10::Otimes(uni10::Otimes(uni10::Otimes(uni10::Otimes(uni10::Otimes(Id, Id), Id), Id), Id), s);*/
    }
    
    h12 = uni10::Dot(S[0], S[1]) + (-1)*uni10::Dot(S[5], S[6]) + uni10::Dot(S[10], S[11]); //S1x.S2x + S1y.S2y + S1z.S2z 
    h23 = uni10::Dot(S[1], S[2]) + (-1)*uni10::Dot(S[6], S[7]) + uni10::Dot(S[11], S[12]); //S2x.S3x + S2y.S3y + S2z.S3z 
    h34 = uni10::Dot(S[2], S[3]) + (-1)*uni10::Dot(S[7], S[8]) + uni10::Dot(S[12], S[13]); //S3x.S4x + S3y.S4y + S3z.S4z
    h45 = uni10::Dot(S[3], S[4]) + (-1)*uni10::Dot(S[8], S[9]) + uni10::Dot(S[13], S[14]); //S4x.S5x + S4y.S5y + S4z.S5z
    /*h56 = uni10::Dot(S[4], S[5]) + (-1)*uni10::Dot(S[10], S[11]) + uni10::Dot(S[16], S[17]); //S5x.S6x + S5y.S6y + S5z.S6z*/
    
    h = h12+h23+h34+h45;

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