
!!! tip-full-width "Grip it & Rip it :sparkles:"
    
    The best way to learn how this works it is to do it a lot!
    
    Use this section as a reference, but don't be afraid to just dive in and start recording! If things don't come out right, fiddle with your cameras and your settings and try it again! You don't have to understand how it works to use it, and you'll learn how it works by using it ✨

    Start by recording A LOT of SHORT recordings, so that you can iterate quickly and get a feel for how the system works and the things the determine the quality of your output.
    
    If you get stuck, [join our Discord](https://discord.gg/P2nyraRYjb) and ask for help in the #help-requests channel!

## [Video Tutorial](https://www.youtube.com/watch?v=GxKmyKdnTy0&t=872s)

This video uses an older version of the software, but the discussion of hardware, lighting, and camera placement is still relevant (use the timestamps to jump to specific sections):


# Detailed Setup Guide
## Lighting Conditions

Lighting is crucial for a camera-based system like FreeMoCap. For best results, use bright environments, such as near open windows during the day. Be cautious, as environments that appear bright to our eyes may be quite dim (Human eyes are exceptionally good at adapting to different lighting conditions).

On a technical level, **we want enough light in our scene that we can set our camera's Exposure times to be as short as possible**. 

A short exposure time means that the camera's (digital) shutter will be open for a shorter time on each recorded frame. That means that your subject will have less time to move during the exposure, which will reduce motion blur and make it easier to identify the subject's joints in each frame.

When setting the exposure on the GUI, aim for a setting of at most `-6`, but better results can be achieved at `-7` or `-8` or lower. For information on how these number map onto actual time measurements, see [this article](https://www.kurokesu.com/main/2020/05/22/uvc-camera-exposure-timing-in-opencv/).


## Background Considerations

A solid-colored backdrop is not strictly necessary, but using one can improve the quality of recordings. Covering complex visual textures in the camera's field of view makes tracking the human in the scene easier, leading to better outcomes. Start with a simple setup first, and add complexity once you've established that the simple version works.

Similarly, it is better for subjects to wear tight-fitting clothes that expose joints like elbows and knees. While not strictly necessary, it will lead to better quality recordings. Consider the machine's perspective: if the subject is wearing baggy pants and the software is asked to identify the knee, it will struggle. It may produce an estimate close to the correct position, but tracking the knee will be easier if it is visible or if the subject is wearing tight-fitting pants.

## Camera Placement and Configuration

Camera placement is critical. Ensure that the subject is in full view of each camera. In multi-camera setups, ensure that at least two, preferably three, cameras can see every part of the subject's body at any given time. Cameras can be rotated 90° to portrait mode to capture a standing human in a tighter space.

Ideally, the person should occupy as much of the camera screen as possible, providing more information for the software to track the person. Most testing has been done on low-quality webcams, with some tests on GoPros. A separate how-to guide can be created to handle asynchronous recordings from devices like GoPros.

In multi-camera situations, separate the cameras enough to provide different points of view on the subject. If multiple cameras are positioned too close together, they won't add much information to the scene. Separating them by a sufficient angle improves triangulation.

High-quality recordings can be ensured by adjusting camera settings for optimal image results, mainly by setting the appropriate exposure for the lighting conditions and having good lighting. A successful calibration is also necessary, which will be covered in a separate how-to guide.

