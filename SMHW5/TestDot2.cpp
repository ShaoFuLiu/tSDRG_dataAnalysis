#include <iostream>
#include <fstream>
#include <sstream>
#include <random>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <uni10.hpp>
using namespace std;

int main()
{
    int sigma11, sigma12, sigma21, sigma22;
    int n = 2; // n-ladder
    int state_num = pow(2,n);
    int matelm = pow(2,n)*pow(2,n);// number of matrix element is 2^n x 2^n
    double K = 1; // coupling constant * Beta
    double betaH;
    uni10_double64 mat_elem[matelm]; 
    uni10::Matrix<double> T, En, state;

    for(int i=0; i<pow(2,n); i++)
    { 
        switch (i)
        {
        case 0:
            sigma11 = 1;
            sigma21 = 1;
            break;
        case 1:
            sigma11 = 1;
            sigma21 = -1;
            break;
        case 2:
            sigma11 = -1;
            sigma21 = 1;
            break;
        case 3:
            sigma11 = -1;
            sigma21 = -1;
            break;                            
        }
        for(int j=0; j<pow(2,n); j++)
        {
            switch (j)
            {
            case 0:
                sigma12 = 1;
                sigma22 = 1;
                break;
            case 1:
                sigma12 = 1;
                sigma22 = -1;
                break;
            case 2:
                sigma12 = -1;
                sigma22 = 1;
                break;
            case 3:
                sigma12 = -1;
                sigma22 = -1;
                break;                            
            }
            betaH = K * (sigma11*sigma12 + sigma21*sigma22 + sigma11*sigma21);           
            mat_elem[i*state_num+j] = exp(betaH);
            if(i==2 && j==2)
            {
                cout << "mat_elem[i*state_num+j] = " << mat_elem[i*state_num+j] << endl;
            }
        }   
    }

    T = uni10::Matrix<uni10_double64>(state_num, state_num, mat_elem);
    cout << "The transfer matrix of K = 1 is : " << T << endl;
    uni10::EigH(T, En, state, uni10::INPLACE);
    cout << "The eigenvalue of transfermatrix is : " << En << endl;
    
    return 0;
}