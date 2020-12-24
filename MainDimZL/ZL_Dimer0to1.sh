#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -pe smp 12

export OMP_NUM_THREADS=12

source ${HOME}/intel/mkl/bin/mklvars.sh intel64
source ${HOME}/intel/bin/compilervars.sh intel64

date
./spin1.exe 64 30 10 0 0.5 PBC 1 1
./spin1.exe 64 30 10 0 0.52 PBC 1 1
./spin1.exe 64 30 10 0 0.54 PBC 1 1
./spin1.exe 64 30 10 0 0.56 PBC 1 1
./spin1.exe 64 30 10 0 0.58 PBC 1 1
./spin1.exe 64 30 10 0 0.6 PBC 1 1
./spin1.exe 64 30 10 0 0.62 PBC 1 1
./spin1.exe 64 30 10 0 0.64 PBC 1 1
./spin1.exe 64 30 10 0 0.66 PBC 1 1
./spin1.exe 64 30 10 0 0.68 PBC 1 1
./spin1.exe 64 30 10 0 0.7 PBC 1 1
./spin1.exe 64 30 10 0 0.72 PBC 1 1
./spin1.exe 64 30 10 0 0.74 PBC 1 1
./spin1.exe 64 30 10 0 0.76 PBC 1 1
./spin1.exe 64 30 10 0 0.78 PBC 1 1
./spin1.exe 64 30 10 0 0.84 PBC 1 1
./spin1.exe 64 30 10 0 0.82 PBC 1 1
./spin1.exe 64 30 10 0 0.84 PBC 1 1
./spin1.exe 64 30 10 0 0.86 PBC 1 1
./spin1.exe 64 30 10 0 0.88 PBC 1 1
./spin1.exe 64 30 10 0 0.9 PBC 1 1
./spin1.exe 64 30 10 0 9.2 PBC 1 1
./spin1.exe 64 30 10 0 9.4 PBC 1 1
./spin1.exe 64 30 10 0 9.6 PBC 1 1
./spin1.exe 64 30 10 0 9.8 PBC 1 1
./spin1.exe 64 30 10 0 1 PBC 1 1

date
