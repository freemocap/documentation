# How to install and run the `alpha` GUI


!!! warning "This is a work-in-progress :D"

    No promises here, skele-friends! The `alpha` is in active development and so this is likely to change very soon. If you'd like to use the `alpha`, 

Most of the dev team runs the GUI through `PyCharm`, but its easier to write instructions on how to run from an anaconda prompt.
 
## Pre-requisites:
1. Install Anaconda
    - [https://anaconda.org](https://anaconda.org)
2. Install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (just use the defaults)
3. (OPTIONAL, but highly recommended) Install Blender - [https://blender.org](https://blender.org)

## Installation instructions

1. Open anaconda enabled terminal

2. Create a `python=3.9` environment
```bash
conda create -n freemocap-gui python=3.9
```

3. Activate that environment:
```
conda activate freemocap-gui
```

4. Clone the repository (i.e. download the code from github. It'll show up in the current working directory of your terminal session)
```
git clone https://github.com/freemocap/freemocap
```

5. Navigate into that newly cloned/downloaded `freemocap` folder with:
```
cd freemocap
```

6. Install the dependencies listed in the `requirements.txt` file:
```
pip install -r requirements.txt
```
7. Run the GUI by running the `src/gui/main/main.py` file by entering this command into the terminal:
```bash
python src/gui/main/main.py
```

8. Hopefully a GUI popped up! There are no docs on usage yet, so just click and see what you can figure out :joy:


## Current limitations

At the moment, the `alpha` GUI's method for connecting to the cameras is very innefficient and will experience framerate drops with more than ~3 cameras (even with a powerful PC). We're working on a fix, and should have it handled soon! In the mean time, you can still use the GUI to process videos recorded with other methods (workflow described in the next section!)