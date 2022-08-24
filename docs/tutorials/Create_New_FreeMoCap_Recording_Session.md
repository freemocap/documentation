# Basic   Usage



 ##  HOW TO CREATE A *NEW* `FreeMoCap` RECORDING SESSION

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