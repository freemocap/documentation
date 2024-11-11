# Multi-Camera Calibration Guide

> This calibration process describes the use of an anipose-based calibration method. We will soon be updating our method to use a more flexible and interactive interface.
{style="note"}

<procedure title="Video Guidance" collapsible="true">

[Check out this video for more information and directed guidance in the calibration process](https://youtu.be/GxKmyKdnTy0?t=1615)

</procedure>

## Preparing the Charuco Board
To perform a multi-camera calibration, you'll need to print out a [Charuco board image](https://github.com/freemocap/freemocap/blob/main/freemocap/assets/charuco/charuco_board_image.png). 

For smaller spaces, a simple printout from a standard printer should work just fine. Make sure to mount the printout on something rigid like cardboard - the calibration process requires a *flat* charuco board.

For larger spaces, you might need to print this on a larger poster board so that it can be seen well by the cameras.

## Setting up Cameras
To get a multiple camera recording, you'll need multiple cameras set up and connected to your computer. There's detailed instructions on multiple camera setups in the [Detailed Setup Guide](detailed_setup.md), but for now it will suffice to have two or more (three or more is best) cameras connected directly to your computer. We don't recommend using a USB hub to connect cameras. The cameras should be set up so they all see the subject at the same time, and have a 40-60 degree angle between each camera from the subject's viewpoint.

## Recording Calibration Videos
In the camera view section of the GUI, select the calibration videos option:

![image](freemocap_calibration_window_w_text_overlay.png)

Begin the recording, and then move until your Charuco board can be seen in the overlapping fields of view of at least two cameras at a time. Move the Charuco board up and down so that you are "painting" each camera's view with images of the board. Make sure that every camera has shared views of the board with at least one other camera. We will be using the corresponding views of the board with the other cameras to help localize the camera positions relative to each other, which is necessary for the 3D triangulation step later.

For more information about how to use the board to get a high quality calibration, [see this video](https://www.youtube.com/watch?v=GxKmyKdnTy0&t=1786s) (it uses a different version of this software, but the same principles apply).

## Processing the Calibration
Once you have given each camera a good view of the board shared with another camera, click "Stop Recording," and it will begin the calibration process automatically. 

> Be sure to keep an eye on the terminal that launched the GUI for helpful output, as the log at the bottom of the  GUI screen does not capture all of the outputs yet. 
> *Note: The terminal only launches in this way on Windows*.
{style="note"}

## Recording Motion Capture Videos

Once you have completed the calibration process, you are are ready to record motion capture videos!

Select "Record Motion Capture Videos" from the camera view section of the GUI, and then click "Record." Perform your movement, and then click "Stop." The software will automatically process the videos and generate a Blender scene with the output data!

To manually process/re-process the videos, use the `Process Motion Capture Videos` button in the `Processing` tab of the GUI.

