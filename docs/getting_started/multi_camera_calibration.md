## Multi-Camera Calibration Guide
!!! tip
     [Check out this video for more information and directed guidance in the calibration process](https://youtu.be/GxKmyKdnTy0?t=1615)

**Note:** This calibration process describes the use of an anipose-based calibration method. We will soon be updating our method to use a more flexible and interactive interface.

### Preparing the Charuco Board
To perform a multi-camera calibration, you'll need to print out a [Charuco board image](https://github.com/freemocap/freemocap/blob/main/assets/charuco/charuco_board_image.png). For smaller spaces, a simple printout from a standard printer should work just fine. For larger spaces, you might need to print this on a poster board so that it can be viewed from the cameras.

### Recording Calibration Videos
In the camera view section of the GUI, select the calibration videos option:
![image](/assets/images/freemocap_calibration_window_w_text_overlay.png)


Begin the recording, and then move until your Charuco board can be seen in the overlapping fields of view of at least two cameras at a time. Move the Charuco board up and down so that you are "painting" each camera's view with images of the board. Make sure that every camera has shared views of the board with at least one other camera. We will be using the corresponding views of that board with the other cameras to help localize the camera positions relative to each other, which is necessary for the 3D triangulation step later.

For more information about how to use the board to get a high quality calibration, [see this video](https://www.youtube.com/watch?v=GxKmyKdnTy0&t=1786s) (it uses a different version of this software, but the same principles apply)

### Processing the Calibration
Once you have given each camera a good view of the board shared with another camera, click "Stop Recording," and it will begin the calibration process automatically. 

!!! tip
     Be sure to keep an eye on the terminal that launched the GUI for helpful output, as the log at the bottom of the  GUI screen does not capture all of the outputs yet.
