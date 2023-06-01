
## Lighting Conditions

Lighting is crucial for a camera-based system like FreeMoCap. For best results, use bright environments, such as near open windows during the day. Be cautious, as environments that appear bright to our eyes may be quite dim (Human eyes are exceptionally good at adapting to different lighting conditions). When setting the exposure on the GUI, aim for a setting of at most -6, but better results can be achieved at -7 or -8. Examples of proper exposure settings will be provided later in the documentation.

!!! tip-full-width Pro-tip - Empathize with The Machine 
    Consider the task you are asking the software to perform empathetically. If you, as a human, would struggle to accurately identify joint centers in the camera images, the software will likely struggle too.

On a more technical level, the goal is to have enough light in the scene to allow for short exposure times on the cameras. Short exposure times reduce the blur recorded in each image, as the shutter won't be open long enough to record motion blur. Example images will be included in the tutorial later.

## Background Considerations

A solid-colored backdrop is not strictly necessary, but using one can improve the quality of recordings. Covering complex visual textures in the camera's field of view makes tracking the human in the scene easier, leading to better outcomes. Start with a simple setup first, and add complexity once you've established that the simple version works.

Similarly, it is better for subjects to wear tight-fitting clothes that expose joints like elbows and knees. While not strictly necessary, it will lead to better quality recordings. Consider the machine's perspective: if the subject is wearing baggy pants and the software is asked to identify the knee, it will struggle. It may produce an estimate close to the correct position, but tracking the knee will be easier if it is visible or if the subject is wearing tight-fitting pants.

## Camera Placement and Configuration

Camera placement is critical. Ensure that the subject is in full view of each camera. In multi-camera setups, ensure that at least two, preferably three, cameras can see every part of the subject's body at any given time. Cameras can be rotated 90° to portrait mode to capture a standing human in a tighter space.

Ideally, the person should occupy as much of the camera screen as possible, providing more information for the software to track the person. Most testing has been done on low-quality webcams, with some tests on GoPros. A separate how-to guide can be created to handle asynchronous recordings from devices like GoPros.

In multi-camera situations, separate the cameras enough to provide different points of view on the subject. If multiple cameras are positioned too close together, they won't add much information to the scene. Separating them by a sufficient angle improves triangulation.

High-quality recordings can be ensured by adjusting camera settings for optimal image results, mainly by setting the appropriate exposure for the lighting conditions and having good lighting. A successful calibration is also necessary, which will be covered in a separate how-to guide.
