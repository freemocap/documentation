# Reprojection Error Outlier Rejection

Reprojection error outlier rejection is an optional postprocessing step to the 3D triangulation stage of processing. It retriangulates outlier data from the 3d triangulation with the cameras contributing the most error removed. Reprojection error outlier rejection is most effective when there is poor skeleton detection in one or more camera views. It is turned on and off in "Process Data" tab with the checkbox "Use Outlier Rejection Method?". It is turned off by default.

![Detail of Reprojection Error Outlier Rejection Options](reprojection_filtering_crop_detail.png){ width="450" }

## What is Reprojection Error?
"Reprojection error" is the distance between the originally measured point (i.e. a joint on the 2d skeleton) and the reconstructed 3d point reprojected back onto the original image. The intuition is that if the 3d reconstruction and original 2d track are perfect, then reprojection error will be zero. If it isn't, then there is some inaccuracy in either: the original 2d tracks (i.e. bad skeleton detection from one or more cameras), in the 3d reconstruction (i.e. bad camera calibration), or a combination of the two.

## How Does Reprojection Error Outlier Rejection Work?
Reprojection error outlier rejection can help when there is poor skeleton detection in one or more camera views. After running the standard triangulation on a marker with all cameras, it calculates the reprojection error. If the error is above the target threshold, it iteratively tests subsets of cameras by dropping on or more cameras at a time, up to a configurable maximum. During this process, it tests each combination of cameras and calculates an exponential weight based on the reprojection error for that subset. If any combination within one loop achieves an error below the target threshold, the search stops early to prevent dropping more cameras than necessary. The result is the weighted average 3D point, with points that have lower reprojection error being weighted higher. If no subset of cameras achieves an error below the target, then the returned value is the one with the lowest error between the weighted result and the initial triangulation.


## What are the Parameters and What Do They Do?
The first parameter is "Use Outlier Rejection Method?", a checkbox that sets whether to run the reprojection error outlier rejection process. It is turned off by default.

The second parameter is "Maximum Cameras to Drop", which sets the maximum number of cameras that can be removed during the search. The default is set to 1. 

The third parameter is "Minimum Cameras for Triangulation", which sets the minimum number of cameras. If you are running 4 or more cameras, you may want to increase this number. The number of cameras used will be limited by both this parameter and the "Maximum Cameras to Drop". The default is set to 2.

The fourth parameter is "Target Reprojection Error", which sets the mean reprojection error to aim for when filtering each marker. Lowering this will lead to rejecting more outliers, and raising it will lead to accepting more outliers.
