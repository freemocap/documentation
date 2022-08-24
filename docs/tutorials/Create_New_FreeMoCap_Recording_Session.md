
 ##  HOW TO CREATE A *NEW* `FreeMoCap` RECORDING SESSION
 
**Short Story** 

tl;dr- **Activate the the freemocap Python environment** and run the following lines of code (either in a script or in a console)

```python
import freemocap
freemocap.RunMe()
```

But COOL KIDS will install Blender ([blender.org](https://blender.org) and generate an awesome `.blend` file animation by setting `useBlender=True`: 

```python
import freemocap
freemocap.RunMe(useBlender=True)
```




This two-line script is a copy of the `freemocap_runme_script.py` file, which can be run by entering the following command into a command prompt or powershell: 
```
(freemoocap-env)$ python freemocap_runme_script.py
```

---

**Long story**

 ### 1)  In an Anaconda enabled Command Prompt, PowerShell, or Windows Terminal window 
- You will know if it's `Anaconda Enabled` because you will see a little `(base)` to the left of each line, which denotes that your `(base)` environment is currently active.
-  We recommend Windows Terminal so you can enjoy all the [Rich](https://github.com/willmcgugan/rich)✨ formatted text output, but you'll need to do a bit of work to connect it to Anaconda (e.g. [these instructions](https://dev.to/azure/easily-add-anaconda-prompt-in-windows-terminal-to-make-life-better-3p6j) )
   - If that seems intimidating (or just too much work), just press the `Windows` key, type `Anaconda Prompt` and run everything from there.
   
 ###  2) Activate your freemocap environment 
  - e.g. if your freemocap environment is named `freemocap-env`, type:
  ```
  (base)$ conda activate freemocap-env
  ```
  - If successful, the `(base)` to the left of each line will change to `(freemocap-env)`, indicating that your freemocap environment is now active (type `conda info --envs` or `conda info -e` for a list of all available environments)

### 3) Activate an `ipython` console
   - Activate  an instance of an `ipython` console by typing `ipython` into the command window and pressing 'Enter'
```
(freemocap-env)$ ipython
```
### 4)  Within the `ipython` console, import the `freemocap` package

```Python
[1]: import freemocap
```

### 5) Execute the `freemocap.RunMe()` command (with default parameters, see [#runme-input-parameters](#runme-input-parameters) for more info)

```python
[2]: freemocap.RunMe() #<-this is where the magic happens!
```

### 6) Follow instructions in the Command window and pop-up GUI windows!
