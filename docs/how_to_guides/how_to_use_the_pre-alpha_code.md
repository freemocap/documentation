# How to use the `pre-alpha`


!!! info "We're in the process of launching our `alpha`..."

    We're switching over to the `alpha` phase of this project (`v0.1.0` and on) , which use full refactor code written with help from a professional experienced software architect. 

    Until the new code stabilizes, you may have more luck using the `pre-alpha` code (e.g. `v0.0.54`). If you'd like to try and use the `alpha` GUI, you can start [with this How-To-Guide](how_to_run_the_alpha_gui.md).

## Installing the `pre-alpha`

!!! take-note "Note: Our `pre-alpha` is frozen"

    This will install the latest & last version from the `pre-alpha` phase of this project, frozen at release tag `v0.0.54` [here](https://github.com/freemocap/freemocap/releases/tag/v0.0.54)

Open an Anaconda-enabled command prompt or powershell window and enter the following commands:

1) Create a Python 3.7 Anaconda environment
```bash 
conda create -n freemocap-env python=3.7
``` 

2) Activate that newly created environment
```bash
conda activate freemocap-env
```
3) Install freemocap (version `0.0.54`)  from PyPi using `pip`
```bash
pip install freemocap==0.0.54
```

!!! warning "Warning: BUG FIX - Update `mediapipe` with `pip install mediapipe --upgrade`"

That should be it!
___
##  How to create a new `pre-alpha` recording session

tl;dr- **Activate the freemocap Python environment** and run the following lines of code (either in a script or in a console)

```python
import freemocap
freemocap.RunMe()
```

!!! blender "Be cool, use Blender"

    COOL KIDS will install Blender ([blender.org](https://blender.org) and generate an awesome `.blend` file animation by setting `useBlender=True`: 

```python
import freemocap
freemocap.RunMe(useBlender=True)
```

**For additional, more detailed instructions (including methods to re-process recorded sessions), [refer to the `OLD_README.md` document](https://github.com/freemocap/freemocap/blob/main/OLD_README.md))**

