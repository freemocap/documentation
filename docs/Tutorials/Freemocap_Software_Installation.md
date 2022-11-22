
## How to Install this Software

PLEASE NOTE: 
*This tutorial is for the pre-alpha version of freemocap and (version 0.0.54) and this was written November 2022. So we're gonna be using the pre alpha to record the synchronized videos, and then we'll be loading them into the alpha to process them.*

 ### 1)  In an Anaconda enabled Command Prompt, PowerShell, or Windows Terminal window 
- You will know if it's `Anaconda Enabled` because you will see a little `(base)` to the left of each line, which denotes that your `(base)` environment is currently active.
-  We recommend Windows Terminal so you can enjoy all the [Rich](https://github.com/willmcgugan/rich)✨ formatted text output, but you'll need to do a bit of work to connect it to Anaconda (e.g. [these instructions](https://dev.to/azure/easily-add-anaconda-prompt-in-windows-terminal-to-make-life-better-3p6j) )
   - If that seems intimidating (or just too much work), just press the `Windows` key, type `Anaconda Prompt` and run everything from there.
 ### 2) Create an Anaconda virtual environment for freemocap

 ``` 
 (base) conda create -n freemocap-env python=3.7
 ```

 ###  3) Activate your freemocap environment 
  - e.g. if your freemocap environment is named `freemocap-env`, type:
  ```
  (base)$ conda activate freemocap-env
  ```
  - If successful, the `(base)` to the left of each line will change to `(freemocap-env)`, indicating that your freemocap environment is now active (type `conda info --envs` or `conda info -e` for a list of all available environments)

### 4) Intall freemocap
   - This is the part where all the packages freemocap uses gets installed to your machine, likey NumPy, OpenCV, anipose, mediapipe, etc. (If you type 'pip list' into the terminal, you'll be able to see all the packages your just installed to this virtual environment).
```
(freemocap-env)$ pip install freemocap==0.0.54
```
Again, please note: *This tutorial is for the pre-alpha version of freemocap and (version 0.0.54) and this was written November 2022. So we're gonna be using the pre alpha to record the synchronized videos, and then we'll be loading them into the alpha to process them.*

### 5) Create an environment for the alpha GUI

**We are actively working to clean this part up.**

- GUI stands for graphic user interface. 
- Deactivate the environment you just made by typing. Doing so will bring you back to your base environment, as you can see with (base) re-appearing on the left. 
- Next, create and activate the new environment for the alpha GUI. You'll see (base) switch to (freemocap-gui)
```
(freemocap-env)$ conda deactivate
(base)$ conda create -n freemocap-gui python=3.9
(base)$ conda activate freemocap-gui
(freemocap-gui)$
```
### 6) Install the GUI
**We are actively working to clean this part up. Git needs to be installed on your machine to do this.**

- So, this alpha version of the GUI isn't on PyPI yet (the python package index), so we can't use the usual command (pip install xyz). We'll need to clone our repo on github onto your machine. This is basically a fancy way of downloading a folder of freemocap files and then being able to use those files. 
- Once you clone the repository, you'll change directories so that you're inside the freemocap folder. 
- Next, you'll install the all the required packages from the freemocap folder.  

```
(freemocap-gui)$ git clone https://github.com/freemocap/freemocap
(freemocap-gui)$ cd freemocap
(freemocap-gui)$ pip install -r requirements.txt
```
- Finally, we have to run a specific .py file inside this repo. If that works correcly, you'll see the GUI pop up in its own window on your machine. 

```
(freemocap-gui)$ python src/gui/main/main.py
```
---

Okay! everything is installed and now you're ready to [create and process freemocap recordings.](Create_New_FreeMoCap_Recording_Session.md)

