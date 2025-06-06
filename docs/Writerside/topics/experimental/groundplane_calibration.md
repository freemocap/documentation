# Ground Plane Calibration

### Default Calibration
![image](cam0_as_origin_v2.png) {width = 400}

By default, the world coordinate system is defined by the location and orientation of **Camera 0**— which tends to be the camera that took the first video in the `synchronized_videos` folder. This means:
- The origin `(0, 0, 0)` is placed at the optical center of Camera 0
- The world axes align with Camera 0’s coordinate frame: +Z points outward from the lens, +X to the right, and +Y downward in the image

As a result, reconstructed 3D data (e.g. skeletons) often comes in aligned to the camera's perspective rather than to the physical environment— which means subjects may come in lying sideways instead of standing upright.
While we rotate the reconstructed 3D data to make it appear upright and place the feet on the ground before exporting to Blender, it’s far more reliable to ensure the data is aligned correctly from the start.

### Ground plane calibration
Ground plane calibration redefines the world coordinate system using the orientation of the **ChArUco board**.

- The origin `(0, 0, 0)` is set to **corner 0** of the ChArUco board
- The **X** and **Y** axes are defined by the edges of the board
- The **Z** axis is computed as the normal vector pointing up from the board surface (using the right-hand rule)

![image](charuco_as_groundplane.png){width=800}

This transformation ensures that:
- The world frame is aligned with the physical space
- The reconstructed subject stands upright, with their **feet on the ground (Z ≈ 0)** and **+Z pointing upward**
