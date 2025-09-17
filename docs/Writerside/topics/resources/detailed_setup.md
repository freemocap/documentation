# Mocap Tips and Tricks

While FreeMoCap can record anywhere that's big enough to capture your entire body on video, some places and set ups will give better results than others. The tips below will help you configure your space to get the best recordings, whether you're working with high-end gear or simple webcams. 

Don't be afraid to start small and simple - any set up is better than no set up. You can always add complexity as you become more comfortable with the system.

## Video Tutorial

[This video](https://www.youtube.com/watch?v=GxKmyKdnTy0&t=872s) uses an older version of the software, but the discussion of hardware, lighting, and camera placement is still relevant (use the timestamps to jump to specific sections).

## Lighting Conditions

Lighting is crucial for a camera-based system like FreeMoCap. For best results, use bright environments, such as near open windows during the day. Be cautious, as environments that appear bright to our eyes may be quite dim (Human eyes are exceptionally good at adapting to different lighting conditions).

A short exposure time means that the camera's (digital) shutter will be open for a shorter time on each recorded frame. That means that your subject will have less time to move during the exposure, which will reduce motion blur and make it easier to identify the subject's joints in each frame.

<procedure title="Exposure Settings" collapsible="true">

When setting the exposure on the GUI, aim for a setting of at most `-6`, but better results can be achieved at `-7` or `-8` or lower.

On a technical level, **we want enough light in our scene that we can set our camera's Exposure times to be as short as possible**.

</procedure>

<procedure title="More on Exposure Settings" collapsible="true">

For information on how these camera exposure settings map onto actual time measurements, see [this article](https://www.kurokesu.com/main/2020/05/22/uvc-camera-exposure-timing-in-opencv/).
{style="note"}

</procedure>

## Background Considerations

A solid-colored backdrop is not strictly necessary, but using one can improve the quality of recordings. Covering complex visual textures in the camera's field of view makes tracking the human in the scene easier, leading to better outcomes. Start with a simple setup first, and add complexity once you've established that the simple version works.

Having visual contrast between your subject and the background will help your subject stand out in recordings. Example: wear dark clothing against a light background.

Similarly, it is better for subjects to wear tight-fitting clothes that expose joints like elbows and knees. While not strictly necessary, it will lead to better quality recordings. Consider the machine's perspective: if the subject is wearing baggy pants and the software is asked to identify the knee, it will struggle. It may produce an estimate close to the correct position, but tracking the knee will be easier if it is visible or if the subject is wearing tight-fitting pants.

## Camera Placement and Configuration

Camera placement is critical. Ensure that the subject is in full view of each camera. In multi-camera setups, ensure that at least two, preferably three, cameras can see every part of the subject's body at any given time. 

<procedure title="Working with small spaces" collapsible="true">

Cameras can be rotated 90° to portrait orientation to capture a standing human in a tighter space. You can even mix portrait and landscape views together to better capture your space.

</procedure>

Ideally, the person should occupy as much of the camera screen as possible, providing more information for the software to track the person. Most testing has been done on low-quality webcams, although successful recordings have been made with GoPros, DSLRs, and mobile phones.

In multi-camera situations, separate the cameras enough to provide different points of view on the subject. If multiple cameras are positioned too close together, they won't add much information to the scene. Separating them by a sufficient angle improves triangulation. Just make sure each camera can share a view of the Charuco board with another camera during calibration.

High-quality recordings can be ensured by adjusting camera settings for optimal image results, mainly by setting the appropriate exposure for the lighting conditions and having good lighting. A successful calibration is also necessary, which you can read about in our [Multi-Camera Calibration Tutorial](multi_camera_calibration.md).