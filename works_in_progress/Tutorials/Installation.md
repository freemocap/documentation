## QUICKSTART

1. Install software via [pip](https://pypi.org/project/freemocap/1.0.0rc0/):
```
pip install freemocap~=1.0.0rc0
```

2. Launch the GUI by entering the command:
```
freemocap
```

3. A GUI should pop up that looks something like this
![image](https://user-images.githubusercontent.com/15314521/225373100-4121af75-21cc-4256-a131-6ba242446c8e.png)

4. Follow the instructions in the [[Making your first Skelly - Single-Camera Recording]] (and/or [[Multi-Camera Calibration Guide]]) section for next steps!


## Install/run from source code (i.e. the code in this repository)

> NOTE - these are super bare-bones install instructions just to show the new entry point - these instructions will be overhauled very soon (written 2023-03-14)

Open an [Anaconda-enabled command prompt](https://www.anaconda.org) (or equivalent) and enter the following commands:

1) Create a `Python3.8+` environment 
```bash
conda create -n freemocap-env python=3.9
```

2) Activate that newly created environment
```bash
conda activate freemocap-env
```
3) Clone the repository (pip install coming very soon!)
```bash
git clone https://github.com/freemocap/freemocap
```

4) Navigate into the newly cloned/downloaded `freemocap` folder
```bash
cd freemocap
```

5) Install the package via the `pyproject.toml` file
```bash
pip install -e .
```

6) Launch the GUI (via the `freemocap.__main__.py` entry point)
```bash
python -m freemocap
```