
# How to process pre-recorded synchronized videos with `alpha` GUI

Here's a workflow you can use to pre-process videos recorded with the `pre-alpha (<=v0.0.54)` using the `alpha` 

> NOTE: This software is a work-in-progress, you'll likely have to click around and test things out to get this process to work for the first time. Often, you might click a button and want to go back, but the GUI doesn't have "go-back" capabilities yet :) So in order to go back, simply restart the GUI.

## Step 1 - Run the GUI  
Instructions here - https://github.com/freemocap/freemocap#how-to-run-the-alpha-gui 

- run  `python src/gui/main/main.py` in a terminal with the proper environment activated
> NOTE: If the GUI fails to run, your version of freemocap might be out of date. You can `git fetch` to make sure your repository is up to date, or you can re-clone the freemocap `main` repository.
-  a GUI should pop up that looks like this: 
  
![image](https://user-images.githubusercontent.com/15314521/201449304-4a26d703-e971-404f-81f4-a70d042f9e66.png)

## Step 2 - Import videos
- Select `Import Synchronized Videos ` (or `ctrl+I`)

![image](https://user-images.githubusercontent.com/15314521/201449317-e91de387-7bb2-45a2-9313-d267b2b84b4f.png)

## Step 2a - Create `session_id`

- Optional - Add a tag to the `session_id` dialog to identify which videos you will import. 

> **WARNING**: Don't use spaces in the `session_id`, use underscores `_` or dashes `-` to break up words instead

![image](https://user-images.githubusercontent.com/15314521/201449323-7298a998-2a8f-416e-a00f-245721a9c862.png)

## Step 2b - Select folder of synchronized videos
- click `Select set of synchronized videos...` button
- Select the folder full of synchronized videos

 > HINT: To import the videos from a `freemocap` session recorded with the pre-alpha, select the `[freemoap_data]/[session_id]/SynchedVideos` folder

 > NOTE: Videos should all have *exactly* the same number of frames and the frames should be synchronized with each other

## Step 3 - Calibration
### Option 1 - Load the `camera_calibration.toml`
- Go to the `2-Capture Volume Calibration` tab
- Select `Load Camera Calibration .tomle file...` option
- Load in the `...camera_calibration.toml` file from a previously recorded session 
### Option 2 - Process calibration videos in `GUI`
- With `Calibrate 'from synchronized_videos' folder` option selected, click `Calibration Capture Volume from Videos` button

> You should only select this option if your video contains a charuco board calibration within it. TRENT NOTE: link to the part of the youtube video that talks about the charuco board

## Step 4 - Process Videos
- set processing parameters however you like 
    - RECOMMENDED - Make sure there something present in the `Locate Blender Executable` section, it's the best method we have to visualize the data from the `alpha` GUI (we're working on a new version of the `_animVid.mp4` output from the `pre-alpha`)

- click `Process All` button (it will run through each of the steps below)
- Watch terminal for output infromation

## Step 5 - Visualize data!

### Option #1 - If all went well, the GUI may have automatically opened Blender with your motion capture data pre-loaded
- if not, make sure the blener executable location is specified correclty
- You can re-launch the `blender export` process with the `Export to Blender` button

### Option #2 - Enter the `4-Visualize Motion Capture Data` tab

 - click the `Load Session Data` button
 - NOTE - at the moment there is no way to pause or stop the animation, so when you get sick of looking at it just re-load the GUI with `ctrl-R`:sweat_smile: 


[def]: docs/