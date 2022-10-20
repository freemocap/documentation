# Installation

## Setting up your system to use freemocap
Open an Anaconda-enabled command prompt or powershell window and perform the following steps:

1) Create a Python3.7 Anaconda environment
``` 
conda create -n freemocap-env python=3.7
``` 

2) Activate that newly created environment
```
conda activate freemocap-env
```
3) Install freemocap  from PyPi using `pip`
```
pip install freemocap==0.0.54 #pin version at pre-alpha, to match the workflow described in this document
```
That should be it!