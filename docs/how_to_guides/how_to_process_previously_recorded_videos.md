
# How to process pre-recorded synchronized videos with `alpha` GUI

This is a workflow you can use to process **any** pre-recorded & synchronized videos.

!!! take-note "Note"

    This software is a work-in-progress, you'll likely have to click around and test things out to get this process to work for the first time. Often, you might click a button and want to go back, but the GUI doesn't have "go-back" capabilities yet :) So in order to go back, simply restart the GUI. You can quickly restart the GUI at any time by selecting the GUI and pressing `ctrl-R`

??? pre-alpha "pre-alpha tips"

    If you've pre-recorded videos using freemocap `pre-alpha (<=v0.0.54)`, these "pre-alpha tips" boxes will contain info to specifically address a "`pre-alpha` -> `alpha GUI`" workflow!

## Step 1 - Run the GUI  
Detailed instructions on how to run the GUI using anaconda can be found [on our GitHub](https://github.com/freemocap/freemocap#how-to-run-the-alpha-gui). 

- Once you have the GUI set up and ready to go, run  `python src/gui/main/main.py` in a terminal with the proper environment activated.

!!! take-note "Note"
    
    If the GUI fails to run, your version of freemocap might be out of date. You can `git fetch` to make sure your repository is up to date, or you can re-clone the freemocap `main` repository.
-  A GUI should pop up that looks like this: 
  
![image](https://user-images.githubusercontent.com/15314521/201449304-4a26d703-e971-404f-81f4-a70d042f9e66.png)

## Step 2 - Import videos
- Select `Import Synchronized Videos ` (or `ctrl+I`).

![image](https://user-images.githubusercontent.com/15314521/201449317-e91de387-7bb2-45a2-9313-d267b2b84b4f.png)

### 2.1 - Create `session_id`

- Optional - add a tag to the `session_id` dialog to identify which videos you will import. 

!!! warning

    Do not use spaces in the `session_id`, use underscores `_` or dashes `-` to break up words instead.

![image](https://user-images.githubusercontent.com/15314521/201449323-7298a998-2a8f-416e-a00f-245721a9c862.png)

### 2.2 - Select folder of synchronized videos
- Click `Select set of synchronized videos...` button.
- Select the folder full of synchronized videos.

!!! take-note "Note"
 
    Videos should all have *exactly* the same number of frames and the frames should be synchronized with each other.

??? pre-alpha "pre-alpha tips"
 
    To import the videos from a `freemocap` session recorded with the pre-alpha, select the `[freemoap_data]/[session_id]/SynchedVideos` folder.

## Step 3 - Calibration
- Open the `2-Capture Volume` tab.
### Option #1 - Load the `camera_calibration.toml`
- Select `Load Camera Calibration .toml file...` option.
- Load in the `...camera_calibration.toml` file from a previously recorded session.
### Option #2 - Process calibration videos in `GUI`
- With `Calibrate 'from synchronized_videos' folder` option selected, click `Calibration Capture Volume from Videos` button.

!!! take-note "Note" 

    You should only select this option if your video contains a Charuco Board calibration within it. To learn more about Charuco Boards, check out [this video](https://youtu.be/GxKmyKdnTy0?t=1615).

## Step 4 - Process Videos
- Open the `3-Record/Process/Vizualize Motion Capture Data` tab.
- Set processing parameters however you like.

!!! recommended "Recommendation for Visualizing Data" 

    We highly recommend that you connect freemocap to Blender in the `Locate Blender Executable` section, Blender is still the best method we have to visualize data! Don't have Blender? Download it [here](https://www.blender.org/download/).

- Click `Process All Steps Below` button. Clicking this button will automatically run through every other option on this tab, and you wont need to click anything else!
- Watch terminal for output information.

## Step 5 - Visualize Recording

- If all went well, the GUI may have automatically opened Blender with your motion capture data pre-loaded, and you should be done!
    - If not, double check to make sure the blender executable location is specified correctly.
    - You can re-launch the `Export to Blender` process with the `Generate '.blend' file` button.

[def]: docs/