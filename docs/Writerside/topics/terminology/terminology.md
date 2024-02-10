# Terminology

## Capture Volume
3-dimensional area (volume) with sufficient camera coverage to support 3D tracking.

## Calibration
[Link to a section of the 'braindump' video discussing capture volume calibration](https://www.youtube.com/watch?v=GxKmyKdnTy0&t=1785s)
## Charuco Board
[Link to a section of the 'braindump' video discussing capture volume calibration](https://www.youtube.com/watch?v=GxKmyKdnTy0&t=1615s)

## Mediapipe

https://google.github.io/mediapipe/solutions/holistic

     
## Reprojection Error
"Reprojection error" is the distance (in pixels?) between the originally measured point (i.e. the 2d skeleton) and the reconstructed 3d point reprojected back onto the image plane. 

The intuition is that if the 3d reconstruction and original 2d track are perfect, then reprojection error will be Zero. If it isn't, then there is some inaccurate in either:

-  the original 2d tracks (i.e. bad skeleton detection in one or more cameras), 
-  in the 3d reconstruction (i.e. bad camera calibration), 
- a combination of the two
 


[Click here to follow a conversation about reprojection error on discord](https://discord.com/channels/760487252379041812/760489602917466133/989189718203838505)
