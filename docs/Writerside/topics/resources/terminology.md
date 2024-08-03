# Terminology

## Capture Volume
3-dimensional area (volume) with sufficient camera coverage to support 3D tracking.

## Calibration

Calibration is the process of measuring information about the cameras used for a recording.
We measure the camera "intrinsics", like the focal length and lens distortion, 
as well as "extrinsics", like where the cameras are in space and where they are pointed.
Having the cameras calibrated is necessary to triangulate the 2-dimensional data from each camera into 3-dimensional data. 

[Link to a section of the 'braindump' video discussing capture volume calibration](https://www.youtube.com/watch?v=GxKmyKdnTy0&t=1785s)

## ChArUco Board

A ChArUco board is a combination of a chessboard and ArUco markers, two common tools for calibrating cameras.
The ChArUco is a known object that is easily detected in images, 
and allows the software to figure out where the camera is in relation to the board 
and correct for distortions from the camera.

[Link to a section of the 'braindump' video discussing capture volume calibration](https://www.youtube.com/watch?v=GxKmyKdnTy0&t=1615s)

## Mediapipe

An open source machine learning library from Google. Mediapipe is the default pose estimation solution for FreeMoCap.

[Mediapipe Documentation](https://google.github.io/mediapipe/solutions/holistic)

## YOLO

An open source machine learning library from Ultralytics. Currently used as [a preprocessing step](yolo_cropping.md).

[YOLO Documentation](https://docs.ultralytics.com/)
     
## Reprojection Error
"Reprojection error" is the distance (in pixels?) between the originally measured point (i.e. the 2d skeleton) and the reconstructed 3d point reprojected back onto the image plane. 

The intuition is that if the 3d reconstruction and original 2d track are perfect, then reprojection error will be Zero. If it isn't, then there is some inaccurate in either:

-  the original 2d tracks (i.e. bad skeleton detection in one or more cameras), 
-  in the 3d reconstruction (i.e. bad camera calibration), 
- a combination of the two

[Click here to follow a conversation about reprojection error on discord](https://discord.com/channels/760487252379041812/760489602917466133/989189718203838505)
