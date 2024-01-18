___



!!! tip-full-width "QUICKSTART"
    If you're already familiar with Python environments and package installation, you can get started with FreeMoCap by simply:
    
    ### 1. Create a a Python 3.9 through 3.11 environment (`python3.11` recommended) 
    
    ### 2. Enter command: `pip install freemocap`
        

    ### 3. Enter command: `freemocap`
        
    ...and you're off to the races!
___
___
# Detailed Installation Instructions:
## 0.  Install [Anaconda](https://www.anaconda.com/download) (or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)) if you haven't already.
!!! tip "Python Environments"

    If you are not familiar with Python environments, here's a nice [guide from Real Python](https://realpython.com/python-virtual-environments-a-primer/).
    
    We recomend low XP folk use `conda` to manage their python environment because its the easiest to set up, but you can use whatever method you like.

    Personally, I use `poetry` :dizzy:

## 1. Open a terminal window
!!! tip ""

    === "Windows"
    
        Press the `Windows key`, type "Anaconda Prompt", and press Enter.
    
    === "Mac"
    
        Press `command + spacebar` and type "terminal" and press Enter. 
    
    === "Linux"
    
        Press `ctrl + alt + t` to open a terminal window.
    
## 2. Create a new Python environment 

- Create a new Python environment (verions 3.9 through 3.11 recommended). To do so, enter the following command in your terminal: 
```bash
conda create -n freemocap-env python=3.11 -y
```
![conda create -n freemocap-env python=3.11 -y](../assets/images/carbon_conda_create_freemocap-env.png)

??? info "Breakdown of the `conda create` command" 
    This step creates a new installation of Python on your system that will be used to run the code behind the FreeMoCap software!
    
    Here's a breakdown of what's happening in this command:

    **conda create -n freemocap-env python=3.11 -y`**

    - **`conda`**:    The `conda` package manager (i.e. the program that will execute the command that we send it)

    - **`create`**:    The command to create a new environment

    - **`-n freemocap-env`**:  Set the name of the new environment to `freemocap-env`(note: `-n` is short for `--name`)
    
    - **`python=3.11`**:    Install Python version 3.11 into the new environment

    - **`-y`**:    Automatically answer "yes" to any prompts that come up during the installation process

    So, all together, this command is saying:

    "Hey, Conda! Please create a new environment named `freemocap-env` and install Python version 3.11 into it. If you need to ask me any questions during the process, just answer 'Yes' for me."

    ---
    Enter `conda --help` or `conda create --help` into your terminal to learn more about the `conda` command and its options.

    For more information about Python environments, [check out this guide from Real Python](https://realpython.com/python-virtual-environments-a-primer/)
    

- Activate that newly created environment
```bash
conda activate freemocap-env
```
![conda activate freemocap-env](../assets/images/carbon_conda_activate_freemocap-env.png)

## 3. Install software

=== "PyPi (pip)"

    ```bash
    pip install freemocap
    ```

=== "Github (source code)" 

    ```
    git clone https://github.com/freemocap/freemocap
    cd freemocap
    pip install -e .    
    ```

## 4. Launch the GUI
To launch FreeMoCap, enter the command `freemocap` into the terminal, like this:
```
freemocap
```
Put together, steps 3 & 4 should look like this in your terminal:
![pip install freemocap / freemocap](../assets/images/carbon_pipinstall_freemocap.png)


Once `freemocap` is entered into your terminal, a GUI should pop up that looks something like this:

![view of GUI](https://user-images.githubusercontent.com/15314521/239695690-90ef7e7b-48f3-4f46-8d4a-5b5bcc3254b3.png)


# Congrats, you're in! :sunglasses:

Now that you've got FreeMoCap installed, you're ready to record your first motion capture session!

The first step is to set up your environment for motion capture and connect your cameras

:point_right: [Set up your environment](./your_first_recording.md)
