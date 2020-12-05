#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
date
./job.exe 32 30 10 0.5 0.1 PBC 1 10
./job.exe 32 30 10 0.5 0.2 PBC 1 10
./job.exe 32 30 10 0.5 0.3 PBC 1 10
./job.exe 32 30 10 0.5 0.4 PBC 1 10
./job.exe 32 30 10 0.5 0.5 PBC 1 10
./job.exe 32 30 10 0.5 0.6 PBC 1 10
./job.exe 32 30 10 0.5 0.7 PBC 1 10
./job.exe 32 30 10 0.5 0.8 PBC 1 10
./job.exe 32 30 10 0.5 0.9 PBC 1 10
./job.exe 32 30 10 0.5 1 PBC 1 10
date