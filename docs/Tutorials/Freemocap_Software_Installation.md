
## How to Install this Software

PLEASE NOTE: 
*This tutorial is for the pre-alpha version of freemocap and (version 0.0.54) and this was written November 2022.*

 ### 1)  In an Anaconda enabled Command Prompt, PowerShell, or Windows Terminal window 
- You will know if it's `Anaconda Enabled` because you will see a little `(base)` to the left of each line, which denotes that your `(base)` environment is currently active.
-  We recommend Windows Terminal so you can enjoy all the [Rich](https://github.com/willmcgugan/rich)✨ formatted text output, but you'll need to do a bit of work to connect it to Anaconda (e.g. [these instructions](https://dev.to/azure/easily-add-anaconda-prompt-in-windows-terminal-to-make-life-better-3p6j) )
   - If that seems intimidating (or just too much work), just press the `Windows` key, type `Anaconda Prompt` and run everything from there.
 ### 2) Create an Anaconda virtual environment for freemocap

 ``` 
 (base) conda create -n freemocap-env python=3.7
 ```

 ###  2) Activate your freemocap environment 
  - e.g. if your freemocap environment is named `freemocap-env`, type:
  ```
  (base)$ conda activate freemocap-env
  ```
  - If successful, the `(base)` to the left of each line will change to `(freemocap-env)`, indicating that your freemocap environment is now active (type `conda info --envs` or `conda info -e` for a list of all available environments)

### 3) Intall freemocap
   - This is the part where all the packages freemocap uses gets installed to your machine, likey NumPy, OpenCV, anipose, mediapipe, etc. (If you type 'pip list' into the terminal, you'll be able to see all the packages your just installed to this virtual environment).
```
(freemocap-env)$ pip install freemocap==0.0.54
```
### 4)  To use the current iteration of the GUI (pre alpha)
