# Triangulation

The **3D Triangulation Methods** panel controls how FreeMoCap combines the per-camera 2D skeleton tracks into 3D points. At its simplest, triangulation takes the 2D detections of a given keypoint from every camera that saw it and solves for the 3D position that best matches those views. FreeMoCap also offers an optional reprojection-error-based outlier-rejection step that can substantially improve reconstruction quality on 4+ camera rigs.

![Detail of Reprojection Error Outlier Rejection Options](reprojection_filtering_crop_detail.png)

## Top-Level Parameters

**Minimum Cameras for Triangulation** — sets the minimum number of cameras that must have a valid 2D detection of a given keypoint for that keypoint to be included in the 3D output. Points with fewer valid detections than this threshold are left out. This parameter applies to **both** the simple triangulation path and the outlier-rejection path. The default is **3**. If you set this value higher than the number of cameras in your recording (e.g. `min=3` on a 2-camera rig), FreeMoCap will emit a warning in the logs and automatically adjust the value down to the number of cameras available so processing still runs.

**Flatten Single Camera Data** - Setting this to True flattens single-camera data to the XY plane by setting all Z data to 0. Setting it False uses the tracker XYZ estimates for the keypoints (single camera depth estimates are usually quite bad, we recommend setting up a multi-camera system if you care about 3d data)

**Use Outlier Rejection Method?** — a checkbox that toggles the reprojection-error outlier rejection step (described below). It is **off by default**. We recommend enabling it for any recording with 4+ cameras. For the method to have any effect, the number of cameras in your recording must be *greater than* "Minimum Cameras for Triangulation" — otherwise there are no camera subsets left to test.

## Reprojection Error Outlier Rejection

Reprojection error outlier rejection is an optional postprocessing step to the 3D triangulation stage of processing. It retriangulates outlier data with the cameras contributing the most error removed. It is most effective when there is poor skeleton detection in one or more camera views.

### What is Reprojection Error?
"Reprojection error" is the distance between the originally measured point (i.e. a joint on the 2d skeleton) and the reconstructed 3d point reprojected back onto the original image. The intuition is that if the 3d reconstruction and original 2d track are perfect, then reprojection error will be zero. If it isn't, then there is some inaccuracy in either: the original 2d tracks (i.e. bad skeleton detection from one or more cameras), in the 3d reconstruction (i.e. bad camera calibration), or a combination of the two.

### How Does Reprojection Error Outlier Rejection Work?
After running the standard triangulation on a marker with all cameras, it calculates the reprojection error. If the error is above the target threshold, it iteratively tests subsets of cameras by dropping one or more cameras at a time, up to a configurable maximum. During this process, it tests each combination of cameras and calculates an exponential weight based on the reprojection error for that subset. If any combination within one loop achieves an error below the target threshold, the search stops early to prevent dropping more cameras than necessary. The result is the weighted average 3D point, with points that have lower reprojection error being weighted higher. If no subset of cameras achieves an error below the target, then the returned value is the one with the lowest error between the weighted result and the initial triangulation.

Each tested subset is assigned a weight that falls off exponentially with its reprojection error:

$$
w = e^{-5 \cdot \varepsilon / \varepsilon_{\text{target}}}
$$

- *w* — weight assigned to a given camera subset
- *ε* — mean reprojection error (in pixels) for that subset
- *ε<sub>target</sub>* — the user-configurable target error threshold; subsets well below it get weight ≈ 1, subsets near or above it get weight ≈ 0
- The factor of 5 sets the sharpness of the decay: a subset with ε = ε<sub>target</sub> gets weight e<sup>−5</sup> ≈ 0.007 (nearly zero)

The final 3D point is the weighted average of the points from each tested subset, normalised by the sum of weights:

$$
\hat{p} = \frac{\sum_i w_i \cdot p_i}{\sum_i w_i}
$$

- *p̂* — final estimated 3D point
- *p<sub>i</sub>* — 3D point triangulated from camera subset *i*
- *w<sub>i</sub>* — the weight for subset *i*
- Dividing by Σw<sub>i</sub> normalises the result, so well-behaved subsets dominate while noisy ones contribute almost nothing

This smooth blending avoids sharp frame-to-frame jumps that would otherwise occur if the method simply picked the single "best" subset each frame.

### Outlier-Rejection Sub-Options

**Maximum Cameras to Drop** — sets the maximum number of cameras that can be removed during the subset search. The default is **1**. The effective number of cameras used is bounded by both this parameter and "Minimum Cameras for Triangulation".

**Target Reprojection Error** — the target mean reprojection error (*ε<sub>target</sub>* in the weight formula above) used when filtering each marker. Lowering this will reject more outliers; raising it will accept more.

### Code Reference
The Outlier REjection method was introduced in [FreeMoCap PR#758](https://github.com/freemocap/freemocap/pull/758). Follow the link to see the code behind the implementation 
