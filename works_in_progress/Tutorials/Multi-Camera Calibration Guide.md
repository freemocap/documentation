## Multi-Camera Calibration Guide

**Note:** This calibration process describes the use of an any-pose-based calibration method. We will soon be updating our method to use a more flexible and interactive interface.

### Preparing the Charuco Board
To perform a multi-camera calibration, you'll need to print out a Charuco board from [this link](URL). For smaller spaces, a simple printout from a standard printer should work just fine. For larger spaces, you might need to print this on a poster board so that it can be viewed from the cameras.

### Recording Calibration Videos
In the camera view section of the GUI, select the calibration videos option:
[Add a screenshot of the view here]

Begin the recording, and then move until your Charuco board can be seen in the overlapping fields of view of at least two cameras at a time. Move the Charuco board up and down so that you are "painting" each camera's view with images of the board. Make sure that every camera has shared views of the board with at least one other camera. We will be using the corresponding views of that board with the other cameras to help localize the camera positions relative to each other, which is necessary for the 3D triangulation step later.

### Processing the Calibration
Once you have given each camera a good view of the board shared with another camera, click "Stop Recording," and it will begin the calibration process automatically. Be sure to keep an eye on the terminal that launched the GUI for helpful output, as the log at the bottom of the screen does not capture all of the outputs yet.
