## `freemocap.RunMe()` Specify recording session  paramters 

The `freemocap.RunMe()` function takes a number of parameters that can be used to alter it's default behavior in important ways. Here are the default parameters along with a followed by a brief description of each one. 

---
### RunMe - Default parameters
```python
#in `freemocap/fmc_runme.py`
def RunMe(sessionID=None,
        stage=1,
        useOpenPose=False, 
        runOpenPose = True, 
        useMediaPipe=True,
        runMediaPipe=True,
        useDLC=False,
        dlcConfigPath=None,
        debug=False,
        setDataPath = False,
        userDataPath = None,
        recordVid = True,
        showAnimation = True,
        reconstructionConfidenceThreshold = .7,
        charucoSquareSize = 36, #mm
        calVideoFrameLength = .5,
        startFrame = 0,
        useBlender = False,
        resetBlenderExe = False,
      	get_synced_unix_timestamps = True,
        good_clean_frame_number = 0,
        bundle_adjust_3d_points=False
        ):
```

### [RunMe input parameters](#runme-input-parameters)
- `sessionID`
  - Type - (str) 
  - [Default] - None.
  - Indentifying string to use for this session. 
  - If creating a new session, default behavior is to autogerate SessionID is based on date and time that the session was recorded
  - If re-processing a previously recorded session, this value specifies which session to reprocess (must be the name of a folder within the `FreeMoCap_Data` folder)
  - 
- `stage`
  - [Type] - Int 
  - [Default] - 1
  - Which processing stage to start from. Processing stages are deined in more  detail in [#processing-stages](#processing-stages) 
  
  ```
  stage 1 - Record Raw Videos
  stage 2 - Synchronize Videos
  stage 3 - Camera Calibration
  stage 4 - 2d Tracking and 3d Calibration
  stage 5 - Create output files (using Blender)
  stage 6 - Create output animation (Matplotlib)
  ```  
- `useMediaPipe`
  - [Type] - BOOL
  - [Default] - False, 
  - Whether or not to use the MediaPipe tracking method in `stage=4`

- `runMediaPipe`
  -	[Type] - BOOL
  - [Default] - False, 
  - Whether or not to RUN the MediaPipe tracking method in `stage=4`  (will use previously processed data. This can save a lot of time when re-processing long videos) 
    
- `useOpenPose`
  -	[Type] - BOOL
  - [Default] - False, 
  - Whether or not to use the OpenPose tracking method in `stage=4`

- `runOpenPose`
  -	[Type] - BOOL
  - [Default] - False, 
  - Whether or not to RUN the OpenPose tracking method in `stage=4`  (will use previously processed data. This can save a lot of time when re-processing long videos) 
  
-  `useDeepLabCut`
    - [Type] - BOOL
    - [Default] - False, 
    - Whether or not to use the DeepLabCut model/project specified at `dlcConfigPath`  to track objects in `stage=4`


-  `setDataPath`
	-	[Type] - BOOL
   - [Default] - False, 
   - Trigger the GUI that prompts user to specify location of `FreeMoCap_Data`

-  `userDataPath`
	-	[Type] - BOOL
     - [Default] - False, 
     - path to the location of `FreeMoCap_Data`

-  `recordVid`
	-	[Type] - BOOL
     - [Default] - False, 
     - wehether to save the matplotlib animation to an `.mp4` file

-  `showAnimation`
	-	[Type] - BOOL
     - [Default] - False, 
     - wehether to save the matplotlib animation to an `.mp4` file

- `reconstructionConfidenceThreshold`
  - [Type] - float in range(0,1),
  - [Default] - .7
  - Threshold 'confidence' value to include a point in the 3d reconstruction step
  
- `charucoSquareSize`
  - [Type]  = int
  - [Default] = 36,
  - The size of a side of a black square in the Charuco board used in this calibration. The default value of 36 is approximately appropriate for a print out on an 8 in bu 10 in paper (US Letter, approx A4)
  
- `calVideoLength`
  - [Type]  = int, float in range (0,1), or [int, int]
  - [Default] = .5,
  - What portion of the videos to use in the Anipose calibration step in `stage=3`. `-1` uses the whole recording, a number between 0 and 1 defines a proprotion of the video to use, and a tuple of two numbers defines the start and end frame


- `startFrame`
  - [Type]  = int
  - [Default] = 0,
  - what frame of the video to start the animation in `stage=6`

- `useBlender`
  - [Type]  = BOOL
  -  [Default] = True,
  -  Whether to use Blender to create output `.blend`, `.fbx`,`.usd`,and `.gltf` files

- `resetBlenderExe`
  - [Type]  = BOOL
  -  [Default] = False,
  -  Whether to launch GUI to set Blender .exe path (usually something like `C:/Program Files/Blender Foundation/2.95/`)

- `get_synced_unix_timestamps`
  - [Type]  = BOOL
  -  [Default] = True,
  -  Whether to save camera timestamps in `Unix Epoch Time` in addition to the default 'counting up from zero' timestamps. Very helpful for synchronizing FreeMoCap with other softwares

- `good_clean_frame_number`
  - [Type]  = int
  -  [Default] = 0,
  -  A frame where the subject is standing in something like a T-pose or an A-pose, which will be used to scale the armature created via the `useBlender=True` option. If set to default (`0`) the software will attempt to locate this frame automatically by looking for a frame where all markers are visible with high `confidence` values (but this is buggy)

- `bundle_adjust_3d_points` [EXPERIMENTAL as of May 2022]
  - [Type]  = BOOL
  -  [Default] = False,
  -  When set to `True`, the system will run a bundle adjust optimization of all recorded 3d points produced in `stage=4` using `aniposelib`'s `optim_points` method. This takes a rather long time, but can signicantly clean up the resulting recordings. However,it may also "over smooth" the data. We're in the process of testing this method out now
  
- `use_previous_calibration`
  - [Type]  = BOOL
  -  [Default] = False,
  -  Choose whether to use a calibration file from a previous session. When `False`, FreeMoCap will automatically save out calibration data whenever stage 3 is successfully completed. Only one saved calibration file is stored, so running another session will overwrite the currently saved calibration file. When `True` , FreeMoCap will instead load in the saved calibration data, which allows users to create recordings without needing to show the cameras the Charuco board. 


____
____