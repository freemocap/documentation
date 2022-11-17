
# How to process pre-recorded synchronized videos with `alpha` GUI

This is a workflow you can use to process **any** pre-recorded & synchronized videos.

??? take-note "Note: Rebooting the GUI"

    You can re-start the GUI at any time by pressing `CTRl+R` and then press `Ctrl-D` to reload the the most recent session

!!! tip-full-width "Follow for `pre-alpha` Tips"

    If you've pre-recorded videos using freemocap `pre-alpha (<=v0.0.54)`, these blue boxes with our little skele-friend will contain info to specifically address a "`pre-alpha` -> `alpha GUI`" workflow!

## Step 1 - Run the GUI
??? Info "One-click installation coming soon"

    This software is still very much a work in progress and not quite as stable and performant as it could be. 

    As soon as it is, you will be able to install and run the GUI from the [freemocap website](https://freemocap.org) without the needing to crate `python` environments or run anything from the terminal/command line'

- Make sure you're using the most recent version of the `freemocap` software by entering the command `git pull` in the terminal before running `main.py`

 - Prepare a `python` environment using [these instructions from`README` on the `freemocap` GitHub repository](https://github.com/freemocap/freemocap#how-to-run-the-alpha-gui). 

- Once you have set up and activated your environment, run  `python src/gui/main/main.py` in a terminal with the proper environment activated.


-  A GUI should pop up that looks like this: 
  
![freemocap gui screenshot](https://user-images.githubusercontent.com/62706609/202561983-eaa16963-423c-47dd-990c-72385378b0e6.png)

## Step 2 - Import Videos
- Select `Import Synchronized Videos ` (or `ctrl+I`).

![Import Synch'd Videos Button](https://user-images.githubusercontent.com/15314521/201449317-e91de387-7bb2-45a2-9313-d267b2b84b4f.png)

### 2.1 - Create `session_id`
!!! info inline end 

    Throughout each step of this process, watch terminal for valuable feedback about the processing steps and progress bars.

This `session_id` is created based on the date and time that you began this session (format: `session_YYYY-MM-DD_HH_MM_SS`) will be the name of the folder that will house the data from this session. It will be located in your user directory in a folder called `freemocap_data/[session_id]`

- **Optional** - add a tag to the `session_id` dialog to identify which videos you will import. 

!!! warning "Warning: Do not use spaces in the `session_id`, use underscores `_` or dashes `-` to break up words instead."

![eample of session_id and tag](https://user-images.githubusercontent.com/15314521/201449323-7298a998-2a8f-416e-a00f-245721a9c862.png)

### 2.2 - Select folder of synchronized videos

!!! tip-full-width "`pre-alpha` tip"

    If re-processing a `pre-alpha` session, select the `[freemocap_data]/[session_id]/SyncedVideos` folder

- Click `Select set of synchronized videos...` button.
- Select the folder full of synchronized (`.mp4`) videos.

??? info "Converting videos to `.mp4`"

    You can convert your videos to `.mp4` format with   [Handbrake](https://handbrake.fr/).


??? info "Synchronize your own videos"
     
    Videos should all have *exactly* the same number of frames and the frames should be synchronized with each other (for example, `frame#120` of one camera should show an image from the same time-point as `frame#120` of the other cameras) 

    Where perfect synchronization is not possible, just do your best. As a rule of thumb, try to ensure that the frames from the different cameras within a single 'frame duration' of eachother (so +/- 33ms for 30fps videos)

    If your videos have an audio track (e.g. GoPro videos), you may be able to synchronize them using your preferred Video Editor. 


## Step 3 - Calibration
- Open the `2-Capture Volume` tab.
##### Option #1 - Load the `camera_calibration.toml` from a prior freemocap session
!!! tip-full-width "`pre-alpha` tip"

    If re-processing a `pre-alpha` session, select the `[freemocap_data]/[session_id]/[session_id]_camera_calibration.toml` file

- Select `Load Camera Calibration .toml file...` option.
- Load in the `...camera_calibration.toml` file from a previously recorded session.
##### Option #2 - Process calibration videos in `GUI`
- With `Calibrate 'from synchronized_videos' folder` option selected, click `Calibration Capture Volume from Videos` button.

??? Warning "Warning: Only select **Option #2** if your videos include a Charuco Board calibration procedure." 

    For more information about the `charuco board` and camera calibration, [check out this (section of) this video.](https://www.youtube.com/watch?v=GxKmyKdnTy0&t=1785s) 
    

## Step 4 - Process Videos
- Open the `3-Motion Capture Data` tab.
- Set processing parameters however you like.

??? blender "Recommended - Install Blender" 

    Blender is the current best method to view and explore the data produced by the `freemocap` software. You can install blender, [here](https://www.blender.org/download/). 

    The base data will be loaded as a set of keyframed empty objects with names that match the `landmarks` tracked by the [`mediapipe` 'holistic' solution](https://google.github.io/mediapipe/solutions/holistic), which roughly correspond to major joint centers. 

    For help navigating in Blender, check out [this video](https://www.youtube.com/watch?v=nIoXOplUvAw) from @BlenderGuru. 
    
    
??? Warning "Warning: You may need to manually specify the location of the Blender executable in the GUI."

     using the `Locate Blender Executable` button in the `Motion Capture Data` panel



- Click `Process All Steps Below` button. 

  Clicking this button will automatically run through every other option on this tab, and you wont need to click anything else!


## Step 5 - Visualize Recording

- If all went well, the GUI may have automatically opened Blender with your motion capture data pre-loaded, and you should be done!
    - If not, double check to make sure the blender executable location is specified correctly.
    - You can re-launch the `Export to Blender` process with the `Generate '.blend' file` button.

[def]: docs/
