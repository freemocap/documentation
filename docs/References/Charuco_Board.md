# Charuco Board Information

What is a charuco board? 
- The charuco board is a known object of known shape and geometry that is designed to be very easily tracked by computer vision. This is essential for calibrating the different camera's to each be "measuring" the same thing and allows us to quantify the movement of the person. 
- The software figures out how many pixels long each side of the square is and then uses the charuco board of known square size to create a pixel to distance measurement/conversion. This is what allows us to know how many inches your hand moved. 

**When you run your calibration, you'll need to specify the size of the charuco squares (one of the sides of one of the black squares), in milimeters.** 

To do this: 

- (By the way, we're assuming you've already [installed the freemocap software](../Tutorials/Freemocap_Software_Installation.md) , and are essentially following this [calibration protocol](../Tutorials/Create_New_FreeMoCap_Recording_Session.md). )

In an ipython instance in your terminal (or in the RunMe.py schript in whateve IDE you're using) type: 

```
In [2]: freemocap.RunMe(charucoSquareSize=xxx)
```

The default values in freemocap assume your charuco board is printed on an 8.5 x 11 inch sheet of paper (standard printer paper). 

  * Our calibration method relies on [Anipose](https://anipose.org)'s [Charuco-based](https://docs.opencv.org/3.4/df/d4a/tutorial_charuco_detection.html) calibration method to determine the location of each camera during a recording session. This information is later used to create the 3d reconstruction of the tracked points

  * IMPORTANT The Charuco board shown to the camera MUST be generated with the `cv2.aruco.DICT_4X4_250` dictionary! 
  
  * A high resoultion `png` of this Charuco board is in this repository at `/charuco_board_image_highRes.png`

## Generate your own charuco board
  * Use the following python commands (or equivalent). DO NOT CHANGE THE PARAMETERS OR THE CALIBRATION WILL NOT WORK:
	``` python
	import cv2
	
	aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_250) #note `cv2.aruco` can be installed via `pip install opencv-contrib-python`
	
	board = cv2.aruco.CharucoBoard_create(7, 5, 1, .8, aruco_dict)
	
	charuco_board_image = board.draw((2000,2000)) #`2000` is the resolution of the resulting image. Increase this number if printing a large board (bigger is better! Esp for large spaces!
	
	cv2.imwrite('charuco_board_image.png',charuco_board_image)
	
	```
