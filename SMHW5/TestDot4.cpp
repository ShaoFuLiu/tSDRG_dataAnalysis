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
    int sigma11, sigma12, sigma21, sigma22, sigma31, sigma32, sigma41, sigma42;
    int n = 4; // n-ladder
    int state_num = pow(2,n);
    int matelm = pow(2,n)*pow(2,n);// number of matrix element is 2^n x 2^n
    double K = 1; // coupling constant * Beta
    double betaH;
    uni10_double64 mat_elem[matelm]; 
    uni10::Matrix<double> T, En, state;

    for(int i=0; i<2; i++)
    {
        switch (i)
        {
        case 0:
            sigma11 = 1;
            break;
        case 1:
            sigma11 = -1;
            break;
        }
        for(int j=0; j<2; j++)
        {
            switch (j)
            {
            case 0:
                sigma21 = 1;
                break;
            case 1:
                sigma21 = -1;
                break;
            }
            for(int k=0; k<2; k++)
            {
                switch (k)
                {
                case 0:
                    sigma31 = 1;
                    break;
                case 1:
                    sigma31 = -1;
                    break;
                }
                for(int l=0; l<2; l++)
                {
                    switch (l)
                    {
                    case 0:
                        sigma41 = 1;
                        break;
                    case 1:
                        sigma41 = -1;
                        break;
                    }
                    for(int m=0; m<2; m++)
                    {
                        switch (m)
                        {
                            case 0:
                                sigma12 = 1;
                                break;
                            case 1:
                                sigma12 = -1;
                                break;
                        }
                        for(int o=0; o<2; o++)
                        {
                            switch (o)
                            {
                                case 0:
                                    sigma22 = 1;
                                    break;
                                case 1:
                                    sigma22 = -1;
                                    break;
                            }
                            for(int p=0; p<2; p++)
                            {
                                switch (p)
                                {
                                    case 0:
                                        sigma32 = 1;
                                        break;
                                    case 1:
                                        sigma32 = -1;
                                        break;
                                }
                                for(int q=0; q<2; q++)
                                {
                                    switch (q)
                                    {
                                        case 0:
                                            sigma42 = 1;
                                            break;
                                        case 1:
                                            sigma42 = -1;
                                            break;
                                    }
                                    betaH = K * (sigma11*sigma12 + sigma21*sigma22 + sigma31*sigma32 + sigma41*sigma42 + sigma11*sigma21 + sigma21*sigma31 + sigma31*sigma41);           
                                    mat_elem[128*i+64*j+32*k+16*l+m*8+o*4+p*2+q] = exp(betaH);
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    cout << "mat_elem[0] = " << mat_elem[0] << endl;
    T = uni10::Matrix<uni10_double64>(state_num, state_num, mat_elem);
    cout << "The transfer matrix of K = 1 is : " << T << endl;
    uni10::EigH(T, En, state, uni10::INPLACE);
    cout << "The eigenvalue of transfermatrix is : " << En << endl;
    
    return 0;
}