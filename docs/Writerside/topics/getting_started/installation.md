# Installation

> If you're already familiar with Python environments and package installation, you can get started with FreeMoCap by
> simply:
>
>    **1. Create a Python environment (`python3.11` recommended)**
>
>    **2. Enter command: `pip install freemocap`**
>
>    **3. Enter command: `freemocap`**
>
>    ...and you're off to the races!

## Detailed Installation Instructions

<procedure title="Step 0 - Install Anaconda or Miniconda" collapsible="true">

If you haven't already, you need to install [Anaconda](https://www.anaconda.com/download)
or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) on your system. These tools make managing Python projects
and environments easier.

> We recommend using `conda` because it is the most beginner-friendly method to create a virtual environment.
> Any other method for creating a virtual environment (`venv`, `poetry`, etc) should work just as well.
> {style="note"}


> For those not familiar with Python environments, it's recommended to use `conda`. If you'd like more information, here
> is a helpful [guide from Real Python](https://realpython.com/python-virtual-environments-a-primer/) about Python
> virtual
> environments.

</procedure>


<procedure title="Step 1 -  Open a terminal window" collapsible="true">
  <tabs>
      <tab title="Windows">
          Press the `Windows key`, type "Anaconda Prompt", and press Enter.
      </tab>
      <tab title="Mac">
          Press `command + spacebar` and type "terminal" and press Enter.
      </tab>
      <tab title="Linux">
          Press `ctrl + alt + t` to open a terminal window.
      </tab>
  </tabs>
</procedure>


<procedure title="Step 2 -  Create a new Python environment" collapsible="true" id="Step2">

To create a new Python environment with the recommended version 3.11, type the following text into the terminal
and push `Enter`:

```Bash
conda create -n freemocap-env python=3.11 -y
```

> This is a `conda` command `create`s a `-n`ew isolated `python` (version `=3.11`) environment named `freemocap-env`.
> `-y` option automatically confirms the prompt to proceed with the environment setup.

After creating the environment, activate it using:

```Bash
conda activate freemocap-env
```

Now your terminal is set to operate within the `freemocap-env` environment.

</procedure>

<procedure title="Step 3 - Install FreeMoCap software" collapsible="true" >

<tabs>
<tab title="Install from pip">

> Recommended for beginners and non-programmers
> {style = "note"}

Type the text below into the Terminal and press `Enter`:
```Bash
pip install freemocap
```
A bunch of text should stream by for while, and when it is done, enter the command: 

```Bash
freemocap
```
 
With any luck, the GUI window should pop up!

Keep an eye on the Terminal window, as it will provide useful information as the software runs.

> This command downloads a pre-compiled copy of `freemocap` hosted PyPi - https://pypi.org/project/freemocap/.
> 
> The pip package manager automatically fetches the latest stable binary distribution, which is often in the Wheel format (.whl). A "Wheel: is a built-package format that can speed up the installation process, as it does not require compiling the software from source.
</tab>
<tab title = "Install from Source Code">

> Recommended for developers
> {style="note"}

To install FreeMoCap from the source code for development purposes, you will need to clone the repository from GitHub and install it in editable mode using pip. Here is the step-by-step procedure to do so:

1. Open a Terminal.
2. Clone the FreeMoCap repository using git:
```Bash
git clone https://github.com/freemocap/freemocap.git
```
3. Navigate to the cloned repository directory:
```Bash
cd freemocap
```
4. Install the package in editable mode with the following command:
```Bash 
pip install -e .
```

5. Run the software by entering the command: 

```Bash
freemocap
```

... or the equivalent
```Bash
python freemocap/__main__.py
```

> Installing the package in editable mode (-e flag) means that changes you make to the source code will immediately affect the installed package without needing a re-installation. This is especially useful for developers who are modifying the code and testing their changes frequently.
</tab>
</tabs>



</procedure>

If all goes well, a GUI Window with Skelly's face should pop up, looking something like this:

![freemocap-gui-welcome-screen.png](freemocap-gui-welcome-screen.png)


## Congrats, you're in! 😎

After following these steps, you should have FreeMoCap installed and ready to use!

You're ready to get 👉 [Your first recording!](your_first_recording.md)

> **Installation problem?** 😅
> 
> First thing - Did you make a [Python environment](#Step2)?
> 
> That is the root of most installation problems we see, so double check that part first!
> 
> If that didn't help,  check here for solutions to common problems: [Installation Troubleshooting](installation_troubleshooting.md)
> {style= "note"}
