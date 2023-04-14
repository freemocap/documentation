## First-Time  -Single-Camera Recording

### Introduction
For this first tutorial, we recommend that everybody starts by creating a single-camera recording and reconstruction of their movement. This is to make sure that the full pipeline is working on your computer and to give you a sense of what the full process looks like before moving on to more complex tasks like multi-camera calibration and reconstruction. Remember, Skelly says "simple pimple first".

### Launching FreeMoCap
(Add a tutorial on how to install the software, including creating a separate environment and a promise of a single-click download on the website once the software stabilizes)

Launch FreeMoCap from the terminal by activating the relevant Python environment and typing `free mocap` into the terminal, then press Enter. At that point, the GUI should show up, which will look like this:
[Add a screenshot of the view here]

Click the friendly button that says "Start a New Recording" and then click the button that says "Detect Cameras" (or whatever it says):
[Add a screenshot of the view here]

### Camera Detection
The software should locate your cameras, and once they're connected, it will show a viewpoint from the connected camera in the GUI. You can adjust the settings in the sidebar and then click "Apply Settings to Cameras" to apply them. The most important setting to look at right now is the exposure setting, which you should make as low as possible to decrease blur. We generally like to keep it below -6. Adjust it downwards until the image looks crisp, which will probably make it look slightly darker than you would normally expect. For this simple single-camera recording, this isn't a crucial step. As long as you can see yourself in the image, you should be tracked okay, but it's good to keep in mind for the future.

### Recording
This is the place where if you were using multiple cameras, you would need to perform a Charuco board-based calibration. But for now, we can move past it.

Click "Record" and go into the field of view to perform some kind of movement. Then click "Stop", and it should process automatically from there. When it's done, it will pop up a Blender scene if Blender was properly detected (add a troubleshooting tip if that doesn't happen) and populate the folder with the output files:
[Add a screenshot of the view here]
