## QUICKSTART: Install with pip

1. Install software via [pip](https://pypi.org/project/freemocap/1.0.0rc0/):
```
pip install freemocap~=1.0.13rc0
```

2. Launch the GUI by entering the command:
```
freemocap
```

3. A GUI should pop up that looks something like this
![image](https://user-images.githubusercontent.com/15314521/239695690-90ef7e7b-48f3-4f46-8d4a-5b5bcc3254b3.png)

4. Follow the instructions in the [Single-Camera Tutorial](/getting_started/single_camera_recording/) (and/or [Multi-Camera Calibration Guide](/getting_started/multi_camera_calibration/) guide) section for next steps!


## Install from source code 


Open an [Anaconda-enabled command prompt](https://www.anaconda.org) (or equivalent) and enter the following commands:

1) Create a `python` environment (Python 3.9 or 3.10 recommended) 
```bash
conda create -n freemocap-env python=3.10
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
freemocap
```