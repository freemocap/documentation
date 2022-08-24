# Glossary

## Capture Volume
3-dimensional area (volume) with sufficient camera coverage to support 3D tracking.

## Calibration

## Charuco Board

## Media pipe

## Processing Stages

 - **Stage 1 - Record Videos**
   -  Record raw videos from attached USB webcams and timestamps for each frame 
   -  Raw Videos saved to `FreeMoCap_Data/[Session Folder]/RawVideos`

 - **Stage 2 - Synchronize Videos**
   - Use recorded timestamps to re-save raw videos as synchronized videos (same start and end and same number of frames). Videos saved to 
   - Synchronized Videos saved to `FreeMoCap_Data/[Session Folder]/SynchedVideos`


 - **Stage 3 - Calibrate Capture Volume**
   -   Use [Anipose](https://anipose.org)'s [Charuco-based](https://docs.opencv.org/3.4/df/d4a/tutorial_charuco_detection.html) calibration method to determine the location of each camera during a recording session and calibrate the capture volume
   -   Calibration info saved to `[sessionID]_calibration.toml` and `[sessionID]_calibration.pickle` 


-   **Stage 4 - Track 2D points in videos and Reconstruct 3D** <-This is where the magic happens ✨
    -   Apply user specified tracking algorithms to Synchronized videos (currently supporting MediaPipe, OpenPose, and DeepLabCut) to generate 2D data 
        -   Save to `FreeMoCap_Data/[Session Folder]/DataArrays/` folder (e.g. `mediaPipeData_2d.npy`)
    -   Combine 2d data from each camera with calibration data from Stage 3 to reconstruct the 3d trajectory of each tracked point
        -   Save to `/DataArrays` folder (e.g. `openPoseSkel_3d.npy`)
    -   NOTE - you might think it would make sense to separate the 2d tracking and 3d reconstruction into different stages, but the way the code is currently set up it's cleaner to combine them into the same processing stage ¯\\\_(ツ)_/¯

-   **Stage 5 - Use Blender to generate output data files (optional, requires [Blender](https://blender.org) installed. set `freemocap.RunMe(useBlender=True)` to use)**
    -   Hijack a user-installed version of [Blender](https://blender.org) to format raw mocap data into  a `.blend` file including the raw data as keyframed emtpies with a (sloppy,  inexpertly) rigged and meshed armatured based on the [Rigify](https://docs.blender.org/manual/en/2.81/addons/rigging/rigify.html) Human Metarig
    -   Save `.blend` file to `[Session_Folder]/[Session_ID]/[Session_ID].blend` 
    -   You can double click that `.blend` file to open it in Blender. 
    -   For instructions on how to navigate a Blender Scene, try this [YouTube Tutorial](https://www.youtube.com/watch?v=nIoXOplUvAw)


-   **Stage 6 - Save Skeleton Animation!**
    -   Create a [Matplotlib](https://matplotlib.org) based output animation video.
     -  Saves Animation video to: `[Session Folder]/[SessionID]_animVid.mp4`
     -  Note - This part takes for-EVER 😅
     
## Reprojection Error
"Reprojection error" is the distance (in pixels?) between the originally measured point (i.e. the 2d skeleton) and the reconstructed 3d point reprojected back onto the image plane. 

The intuition is that if the 3d reconstruction and original 2d track are perfect, then reprojection error will be Zero. If it isn't, then there is some inaccurate in either:

-  the original 2d tracks (i.e. bad skeleton detection in one or more cameras), 
-  in the 3d reconstruction (i.e. bad camera calibration), 
- a combination of the two



[Click here to follow a conversation about reprojection error on discord](https://discord.com/channels/760487252379041812/760489602917466133/989189718203838505)
