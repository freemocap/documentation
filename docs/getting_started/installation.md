___
# QUICKSTART:
In a Python 3.9 or 3.10 environment, enter: 
```
pip install freemocap   
freemocap
```
## :sparkles: :skull: :sparkles:

___
___
# Not So Quick Start:

## Open a terminal window
!!! tip ""

    === "Windows"
    
        Press the `Windows key`, type "Anaconda Prompt", and press Enter.
    
    === "Mac"
    
        Press `command + spacebar` and type "terminal" and press Enter. 
    
    === "Linux"
    
        Press `ctrl + alt + t` to open a terminal window.
    

## Create a new Python (v3.9 or v3.10) environment 
- Install [Anaconda](https://www.anaconda.com/download) (or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)) if you haven't already.

!!! info inline end "Python Environments" 
    This step creates a new installation of Python on your system that will be used to run the code behind the `freemocap` software!

    For more information about Python environments, [check out this guide from `realpython`](https://realpython.com/python-virtual-environments-a-primer/)
    


- Create a new `python` environment (Python 3.9 or 3.10 recommended). In your Terminal window, enter the following command: 
```bash
conda create -n freemocap-env python=3.10
```

- Activate that newly created environment
```bash
conda activate freemocap-env
```


## Install software

=== "PyPi (pip)"

    ```bash
    pip install freemocap~=1.0.13rc0
    ```

=== "Github (source code)" 

    ```
    git clone https://github.com/freemocap/freemocap
    cd freemocap
    pip install -e .    
    ```

## Launch the GUI by entering the command:
```
freemocap
```

## GUI should pop up that looks something like this
![image](https://user-images.githubusercontent.com/15314521/239695690-90ef7e7b-48f3-4f46-8d4a-5b5bcc3254b3.png)


You're in! :sunglasses:

Follow the instructions in the [Single-Camera Tutorial](/getting_started/single_camera_recording/) (and/or [Multi-Camera Calibration Guide](/getting_started/multi_camera_calibration/) guide) section for next steps!

